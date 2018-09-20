import requests

from settings import GITLAB_PRIVATE_TOKEN

if __name__ == '__main__':
    if GITLAB_PRIVATE_TOKEN is None:
        raise ValueError('GITLAB_PRIVATE_TOKEN is None, stopping here.')

    r = requests.get(
        'https://gitlab.citymeo.fr/api/v4/groups/5/merge_requests',
        headers={
            'Private-Token': GITLAB_PRIVATE_TOKEN,
        },
        params={
            'state': 'opened',
            'scope': 'assigned_to_me',
        },
    )

    mr_count = int(r.headers.get('X-Total', '?'))
    label = "📪" if mr_count == 0 else "📬"

    message = "{label} {mr_count}".format(
        label=label,
        mr_count=mr_count,
    )

    print(message)
