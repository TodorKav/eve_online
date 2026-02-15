import os
import django
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eve.settings")
django.setup()

import requests
from django.db import transaction
from eve.industry.models import Groups

url_categories = 'https://esi.evetech.net/universe/groups/'

TIMEOUT = (15, 30)

group_list = requests.get(url_categories, timeout=TIMEOUT).json()

with transaction.atomic():
    object_list = []
    for group_id in tqdm(group_list):
        obj_json = requests.get(f'{url_categories}{group_id}/', timeout=TIMEOUT).json()
        object_list.append(Groups(
            group_id=obj_json.get('group_id'),
            category_id_id=obj_json.get('category_id'),
            name=obj_json.get('name'),
            published=obj_json.get('published'),
        ))
    Groups.objects.bulk_create(object_list,
                               update_conflicts=True,
                               update_fields=['category_id', 'name', 'published'],
                               unique_fields=['group_id'],
                               batch_size=1000)


