## About the connector
Threat Intelligence enriched with External Attack Surface Management and Digital Risk Protection Services
<p>This document provides information about the SOCRadar Connector, which facilitates automated interactions, with a SOCRadar server using FortiSOAR&trade; playbooks. Add the SOCRadar Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with SOCRadar.</p>

### Version information

Connector Version: 1.0.0


Authored By: Community

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-socradar</pre>

## Prerequisites to configuring the connector
- You must have the credentials of SOCRadar server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the SOCRadar server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>SOCRadar</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the SOCRadar server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Company ID</td><td>Specify the Company ID used to access the SOCRadar server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Company API Key</td><td>Specify the Company API Key used to access the SOCRadar server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Threat Analysis API Key</td><td>Specify the Threat Analysis API Key used to access the SOCRadar server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Incidents</td><td>Retrieves a detailed list of incidents based on the start date, end date and pagination parameters that you have specified.</td><td>get_incidents <br/>Investigation</td></tr>
<tr><td>Get Incident</td><td>Retrieves a details of incidents based on the Alarm ID that you have specified.</td><td>get_incident <br/>Investigation</td></tr>
<tr><td>Threat Analysis</td><td>Retrieves a details of threat analysis based on the inputs that you have specified. You can obtain the 'trust' score (out of 100) of an entity that is calculated based on various threat feed evaluations conducted by SOCRadar.</td><td>threat_analysis <br/>Investigation</td></tr>
<tr><td>Change Status</td><td>Updates status of an incident based on the incident ID and status that you have specified.</td><td>change_status <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Incidents
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Date</td><td>(Optional) Specify the start date of the time range within which to search for and retrieve incidents.
Valid formats are Datetime format (1923-09-23) or Unix Timestamp format (1632355200)
</td></tr><tr><td>End Date</td><td>(Optional) Specify the end date of the time range within which to search for and retrieve incidents.
Valid formats are Datetime format (1923-09-23) or Unix Timestamp format (1632355200).
</td></tr><tr><td>Status</td><td>Specify the Status of the incident to filter the results from SOCRadar. you can choose from ON_HOLD, OPEN, CLOSED, INVESTIGATING, FALSE_POSITIVE and RESOLVED
</td></tr><tr><td>Limit</td><td>(Optional) Specify the maximum number of records to retrieve, per page. Default value is 50. Maximum value is 100
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number of records to retrieve from SOCRadar.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "alarm_asset": "",
        "alarm_assignees": "",
        "alarm_id": "",
        "alarm_related_assets": [],
        "alarm_related_entities": "",
        "alarm_response": "",
        "alarm_risk_level": "",
        "alarm_text": "",
        "alarm_type_details": {
            "alarm_compliance_list": [],
            "alarm_default_mitigation_plan": "",
            "alarm_default_risk_level": "",
            "alarm_detection_and_analysis": "",
            "alarm_generic_title": "",
            "alarm_main_type": "",
            "alarm_post_incident_analysis": "",
            "alarm_sub_type": ""
        },
        "approved_by": "",
        "content": {
            "date": "",
            "email": "",
            "password": "",
            "source": "",
            "type": ""
        },
        "date": "",
        "extra": "",
        "history": [],
        "is_approved": "",
        "last_notification_date": "",
        "notes": "",
        "notification_id": "",
        "status": "",
        "tags": []
    }
]</pre>
### operation: Get Incident
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alarm ID</td><td>Specify the alarm ID to fetch its details from SOCRadar.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "alarm_asset": "",
        "alarm_assignees": "",
        "alarm_id": "",
        "alarm_related_assets": [],
        "alarm_related_entities": "",
        "alarm_response": "",
        "alarm_risk_level": "",
        "alarm_text": "",
        "alarm_type_details": {
            "alarm_compliance_list": [],
            "alarm_default_mitigation_plan": "",
            "alarm_default_risk_level": "",
            "alarm_detection_and_analysis": "",
            "alarm_generic_title": "",
            "alarm_main_type": "",
            "alarm_post_incident_analysis": "",
            "alarm_sub_type": ""
        },
        "approved_by": "",
        "content": {
            "date": "",
            "email": "",
            "password": "",
            "source": "",
            "type": ""
        },
        "date": "",
        "extra": "",
        "history": [],
        "is_approved": "",
        "last_notification_date": "",
        "notes": "",
        "notification_id": "",
        "status": "",
        "tags": []
    }
]</pre>
### operation: Threat Analysis
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Entity</td><td>Specify the Intended entity to be analyzed in SOCRadar. Valid entity types: [IPv4, IPv6, Domain, Hash]
</td></tr><tr><td>Advance Investigation</td><td>(Optional) Specify the this parameter to have an advanced malware analysis over the entity.
</td></tr><tr><td>Force New Analysis</td><td>(Optional) Specify the Malware analysis results of an entity are being cached for 24 hours after result of the entity being obtained by SOCRadar.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "classification": "",
    "credit_details": {
        "max_daily_credit": "",
        "max_monthly_credit": "",
        "remaining_credit": "",
        "remaining_daily_credit": "",
        "remaining_monthly_credit": "",
        "total_api_credit": ""
    },
    "dns_info": {
        "PTR": []
    },
    "findings": [],
    "geo_location": [
        {
            "AsnCode": "",
            "AsnName": "",
            "Cidr": "",
            "CityName": "",
            "CountryCode": "",
            "CountryName": "",
            "Ip": "",
            "Latitude": "",
            "Longitude": "",
            "RegionName": "",
            "Timezone": "",
            "ZipCode": ""
        }
    ],
    "is_advance_investigation": "",
    "is_blacklisted": "",
    "is_whitelisted": "",
    "remaining_credit": "",
    "score": 0.0,
    "score_details": {},
    "value": "",
    "whitelist_hits": "",
    "whitelist_sources": [],
    "whois": {
        "asn": "",
        "asn_cidr": "",
        "asn_country_code": "",
        "asn_date": "",
        "asn_description": "",
        "asn_registry": "",
        "nets": [
            {
                "address": "",
                "cidr": "",
                "city": "",
                "country": "",
                "created": "",
                "description": "",
                "emails": [],
                "handle": "",
                "name": "",
                "postal_code": "",
                "range": "",
                "state": "",
                "updated": ""
            }
        ],
        "nir": "",
        "query": "",
        "raw": "",
        "raw_referral": "",
        "referral": ""
    }
}</pre>
### operation: Change Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alarm ID</td><td>Specify the ID of the Alarm to update it on SOCRadar.
</td></tr><tr><td>Status</td><td>Specify the Status of the Alarm to update it on SOCRadar. you can choose from OPEN, INVESTIGATING, PENDING_INFO, LEGAL_REVIEW, VENDOR_ASSESSMENT, FALSE_POSITIVE, DUPLICATE, PROCESSED_INTERNALLY, NOT_APPLICABLE, MITIGATED and RESOLVED
</td></tr><tr><td>Comments</td><td>Specify the comments about the incident to update it on SOCRadar. This will be shown under the Resolve Notes section in the incident details.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": "",
    "is_success": "",
    "message": "",
    "response_code": ""
}</pre>
## Included playbooks
The `Sample - socradar - 1.0.0` playbook collection comes bundled with the SOCRadar connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the SOCRadar connector.

- Close SOCRadar Alarm
- Get Reputation
- Get SOCRadar Alarm
- Ingest SOCRadar Alarms
- SOCRadar > Lookup

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
