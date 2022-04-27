from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations, _check_health

##sudo -u nginx /opt/cyops-integrations/.env/bin/pip install -r /opt/cyops-integrations/integrations/connectors/socradar_1_0_0/requirements.txt

logger = get_logger('socradar')

class SOCRadar(Connector):
    def execute(self, config, operation_name, params, **kwargs):
        logger.info("operation_name: {0}".format(operation_name))
        action = operations.get(operation_name)
        return action(config, params)

    def check_health(self, config):
        try:
            return _check_health(config)
        except Exception as e:
            raise ConnectorError(e)
