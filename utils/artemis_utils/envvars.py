# environment variables
import os

import ujson as json
from constants import DEFAULT_HIJACK_LOG_FIELDS
from constants import DEFAULT_MON_TIMEOUT_LAST_BGP_UPDATE


ARTEMIS_WEB_HOST = os.getenv("ARTEMIS_WEB_HOST", "artemis.com")
AUTO_RECOVER_PROCESS_STATE = os.getenv("AUTO_RECOVER_PROCESS_STATE", "true")
BULK_TIMER = float(os.getenv("BULK_TIMER", 1))
DB_NAME = os.getenv("DB_NAME", "artemis_db")
DB_USER = os.getenv("DB_USER", "artemis_user")
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_PASS = os.getenv("DB_PASS", "Art3m1s")
HASURA_GRAPHQL_ACCESS_KEY = os.getenv("HASURA_GRAPHQL_ACCESS_KEY", "@rt3m1s.")
HASURA_HOST = os.getenv("HASURA_HOST", "graphql")
HASURA_PORT = os.getenv("HASURA_PORT", 8080)
try:
    HIJACK_LOG_FIELDS = set(
        json.loads(os.getenv("HIJACK_LOG_FIELDS", DEFAULT_HIJACK_LOG_FIELDS))
    )
except Exception:
    HIJACK_LOG_FIELDS = set(DEFAULT_HIJACK_LOG_FIELDS)
HISTORIC = os.getenv("HISTORIC", "false")
GRAPHQL_URI = "http://{HASURA_HOST}:{HASURA_PORT}/v1alpha1/graphql".format(
    HASURA_HOST=HASURA_HOST, HASURA_PORT=HASURA_PORT
)
MON_TIMEOUT_LAST_BGP_UPDATE = int(
    os.getenv("MON_TIMEOUT_LAST_BGP_UPDATE", DEFAULT_MON_TIMEOUT_LAST_BGP_UPDATE)
)
RIS_ID = os.getenv("RIS_ID", "my_as")


# TODO: REST ENV VARS


RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", 5672)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)


WITHDRAWN_HIJACK_THRESHOLD = int(os.getenv("WITHDRAWN_HIJACK_THRESHOLD", 80))

RABBITMQ_URI = "amqp://{}:{}@{}:{}//".format(
    RABBITMQ_USER, RABBITMQ_PASS, RABBITMQ_HOST, RABBITMQ_PORT
)

RPKI_VALIDATOR_ENABLED = os.getenv("RPKI_VALIDATOR_ENABLED", "false")
RPKI_VALIDATOR_HOST = os.getenv("RPKI_VALIDATOR_HOST", "routinator")
RPKI_VALIDATOR_PORT = os.getenv("RPKI_VALIDATOR_PORT", 3323)
TEST_ENV = os.getenv("TEST_ENV", "false")


GUI_ENABLED = os.getenv("GUI_ENABLED", "true")
