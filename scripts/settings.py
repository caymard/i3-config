FOOTBALL_DATA_API_KEY = None

GITLAB_PRIVATE_TOKEN = None

SNCF_API_KEY = None

OWM_KEY = None


try:
    from local_settings import *  # noqa: F401,F402,F403
except ModuleNotFoundError:
    pass
