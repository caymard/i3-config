# pylint: disable=wildcard-import, unused-wildcard-import, import-error
API_KEY = None

GITLAB_PRIVATE_TOKEN = None


try:
    from local_settings import *  # noqa: F401,F402,F403
except ModuleNotFoundError:
    pass
