import os
import django
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eve.settings")
django.setup()

import requests
from django.db import transaction
from eve.industry.models import MarketGroups

url_categories = 'https://esi.evetech.net/markets/groups/'

TIMEOUT = (15, 30)

session = requests.Session()
pages = int(session.get(url_categories, timeout=TIMEOUT).headers.get('X-Pages', 1))
market_groups_id_list = []
for page in tqdm(range(1, pages + 1)):
    market_groups_id_list += session.get(f'{url_categories}?page={page}', timeout=TIMEOUT).json()


with transaction.atomic():
    object_list = []
    for group_id in tqdm(market_groups_id_list):
        obj_json = session.get(f'{url_categories}{group_id}/', timeout=TIMEOUT).json()
        object_list.append(MarketGroups(
            market_group_id=obj_json.get('market_group_id'),
            name=obj_json.get('name'),
            description=obj_json.get('description'),
        ))
    MarketGroups.objects.bulk_create(object_list,
                                     update_conflicts=True,
                                     update_fields=['name', 'description', 'created_at'],
                                     unique_fields=['market_group_id',],
                                     batch_size=1000)
