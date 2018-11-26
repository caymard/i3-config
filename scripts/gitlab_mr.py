import argparse

import requests

from settings import GITLAB_PRIVATE_TOKEN

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch Gitlab API about opened MR.')
    parser.add_argument('--target', metavar='TARGET', type=str, default='me', help='the target to fetch MR from')
    args = parser.parse_args()

    if GITLAB_PRIVATE_TOKEN is None:
        raise ValueError('GITLAB_PRIVATE_TOKEN is None, stopping here.')

    request_params = {'state': 'opened'}
    if args.target == 'sud':
        request_params['scope'] = 'all'
        request_params['labels'] = 'SUD'
    elif args.target == 'me':
        request_params['scope'] = 'assigned_to_me'
    
    r = requests.get(
        'https://gitlab.citymeo.fr/api/v4/groups/5/merge_requests',
        headers={
            'Private-Token': GITLAB_PRIVATE_TOKEN,
        },
        params=request_params,
    )

    mr_count = int(r.headers.get('X-Total', '?'))
    label = "📪" if mr_count == 0 else "📬"

    message = "{label} {mr_count}".format(
        label=label,
        mr_count=mr_count,
    )

    print(message)
