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

group_list = requests.get(url_categories, timeout=TIMEOUT).json()

with transaction.atomic():
    object_list = []
    for group_id in tqdm(group_list):
        obj_json = requests.get(f'{url_categories}{group_id}/', timeout=TIMEOUT).json()
        object_list.append(MarketGroups(
            market_group_id=obj_json.get('market_group_id'),
            name=obj_json.get('name'),
            description=obj_json.get('description'),
        ))
    MarketGroups.objects.bulk_create(object_list,
                                     update_conflicts=True,
                                     update_fields=['name', 'description',],
                                     unique_fields=['market_group_id',],
                                     batch_size=1000)
