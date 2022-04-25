import logging
import requests
import json
import datetime
import os.path
import publicsuffix2
import socket
import re
import dateutil.parser

# operations.py
from connectors.core.connector import Connector, get_logger, ConnectorError

logger = get_logger('usom')


def ioc_update(config, params):
    url = config.get("url").replace("\"", "").strip()
    key = config.get("company_key").replace("\"", "").strip()
    verify = config.get("verify")
    ioc = params.get("ioc").replace("\"", "").strip()
    now = datetime.datetime.now()
    response = ""
    if os.path.exists(f'/tmp/socradarioc.{ioc}.cache.json'):
        f = open(f'/tmp/socradarioc.{ioc}.cache.json')
        content = json.load(f)
        f.close()
        old = dateutil.parser.isoparse(content['date'])
        if (now - old) < datetime.timedelta(minutes=60 * config["expire_hours"]):
            return False
    try:
        response = requests.get(f"{url}/threat/intelligence/feed_list/{ioc}.json?key={key}&v=2", verify=verify)
        content = json.loads(response.text)
        content = {"list": content, 'date': now.isoformat()}
        out_file = open(f'/tmp/socradarioc.{ioc}.cache.json', "w")
        json.dump(content, out_file, indent=6)
        out_file.close()
        return True
    except requests.exceptions.RequestException as ex:
        if response.status_code != 200:
            logger.error(f"SOCRadar returned bad status code: {response.status_code}")
    return False


def query(config, params):
    ioc_update(config, params)
    search = params.get("search").replace("\"", "").strip()
    ioc = params.get("ioc").replace("\"", "").strip()
    search = search.strip().lower()
    # search = re.sub("https?://", "", search)
    path = search
    fqdn = search.split("/")[0]
    domain = ""
    found = ""
    try:
        socket.inet_aton(search)
    except socket.error:
        domain = publicsuffix2.get_sld(fqdn)

    try:
        f = open(f'/tmp/socradarioc.{ioc}.cache.json')
        content = json.load(f)
        f.close()
        content = content["list"]
        found = [d for d in content if
                 (domain == d['feed'].lower() or path == d['feed'].lower() or fqdn == d['feed'].lower())]
    except Exception as e:
        logger.error(f"SOCRadar returned error: {str(e)}")
    if len(found) > 0:
        f = {"found": True}
        f.update(found[0])
        return f
    else:
        return {"found": False}


def malware_analysis(config, params):
    key = config.get("malware_key").replace("\"", "").strip()
    url = config.get("url").replace("\"", "").strip()
    verify = config.get("verify")

    entity = params.get("entity").replace("\"", "").strip()
    advance_investigation = params.get("advance_investigation")
    force_new_analysis = params.get("force_new_analysis")

    try:
        response = requests.get(
            f"{url}/threat/analysis?key={key}&entity={entity}&advance_investigation={advance_investigation}&force_new_analysis={force_new_analysis}",
            verify=verify)
        content = json.loads(response.text)
        return content
    except Exception as e:
        logger.error(f"SOCRadar returned error: {str(e)}")
        raise ConnectorError("{0}".format(e))
        return {"found": False, "error": str(e)}


def _check_health(config):
    verify = config.get("verify")
    try:
        response = requests.get("https://platform.socradar.com/", verify=verify)
        return True
    except requests.exceptions.RequestException as ex:
        return False
