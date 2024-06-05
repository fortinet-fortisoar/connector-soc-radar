"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc Copyright end
"""

import logging
import requests
import json

from connectors.core.connector import Connector, get_logger, ConnectorError

logger = get_logger('socradar')

status_map = {"OPEN": 0,
              "INVESTIGATING": 1,
              "RESOLVED": 2,
              "PENDING_INFO": 4,
              "LEGAL_REVIEW": 5,
              "VENDOR_ASSESSMENT": 6,
              "FALSE_POSITIVE": 9,
              "DUPLICATE": 10,
              "PROCESSED_INTERNALLY": 11,
              "NOT_APPLICABLE": 13,
              "MITIGATED": 12
              }


def threat_analysis(config, params):
    key = config.get("threat_analysis_api_key").replace("\"", "").strip()
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
        return content["data"]
    except Exception as e:
        logger.error(f"SOCRadar returned error: {str(e)}")
        raise ConnectorError("{0}".format(e))


def get_incidents(config, params):
    company_key = config.get("company_key").strip()
    company_id = config.get("company_id")
    url = config.get("url").strip()
    verify = config.get("verify")
    start_date = params.get("start_date")
    end_date = params.get("end_date")
    status = params.get("status")
    limit = params.get("limit")
    page = params.get("page")
    headers = {"API-KEY": company_key}
    url = f"{url}/company/{company_id}/incidents/v4?start_date={start_date}&end_date={end_date}&status={status}&limit={limit}&page={page}"
    try:
        response = requests.get(url, headers=headers, verify=verify)
        content = json.loads(response.text)
        return content["data"]
    except Exception as e:
        logger.error(f"SOCRadar returned error: {str(e)}")
        raise ConnectorError("{0}".format(e))


def get_incident(config, params):
    company_key = config.get("company_key").strip()
    company_id = config.get("company_id")
    url = config.get("url").strip()
    verify = config.get("verify")
    alarm_id = params.get("alarm_id")
    headers = {"API-KEY": company_key}
    url = f"{url}/company/{company_id}/incidents/v4?alarm_ids={alarm_id}"
    try:
        response = requests.get(url, headers=headers, verify=verify)
        content = json.loads(response.text)
        return content["data"]
    except Exception as e:
        logger.error(f"SOCRadar returned error: {str(e)}")
        raise ConnectorError("{0}".format(e))


def change_status(config, params):
    company_key = config.get("company_key").strip()
    company_id = config.get("company_id")
    url = config.get("url").strip()
    verify = config.get("verify")
    alarm_id = params.get("alarm_id")
    status = params.get("status")
    status = status_map[status]
    comment = params.get("comment")
    data = {"alarm_ids": alarm_id, "status": status, "comment": comment}
    headers = {"API-KEY": company_key}
    url = f"{url}/company/{company_id}/alarms/status/change"

    try:
        response = requests.post(url, headers=headers, data=data, verify=verify)
        content = json.loads(response.text)
        return content
    except Exception as e:
        logger.error(f"SOCRadar returned error: {e}")
        raise ConnectorError("{0} ".format(e))


def _check_health(config):
    url = config.get("url").replace("\"", "").strip()
    verify = config.get("verify")
    company_id = config.get("company_id")
    company_key = config.get("company_key").strip()
    url = f"{url}/company/{company_id}/auditlogs?key={company_key}&limit=1"
    try:
        response = requests.get(url, verify=verify)
        if response.status_code != 200:
            raise ConnectorError("Unable to connect SOCRadar")
        return True
    except Exception as e:
        raise ConnectorError("Unable to connect SOCRadar {0}".format(e))


operations = {
    "get_incidents": get_incidents,
    "get_incident": get_incident,
    "threat_analysis": threat_analysis,
    "change_status": change_status
}
