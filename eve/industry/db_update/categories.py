import os
import django
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eve.settings")
django.setup()

import requests
from django.db import transaction
from eve.industry.models import Categories

url_categories = 'https://esi.evetech.net/universe/categories/'

TIMEOUT = (15, 30)

session = requests.Session()
category_list = session.get(url_categories, timeout=TIMEOUT).json()

with transaction.atomic():
    object_list = []
    for category in tqdm(category_list):
        obj_json = session.get(f'{url_categories}{category}/', timeout=TIMEOUT).json()
        object_list.append(Categories(
                                    category_id=obj_json.get('category_id'),
                                    name=obj_json.get('name'),
                                    published=obj_json.get('published'),
        ))
    Categories.objects.bulk_create(object_list,
                                   update_conflicts=True,
                                   update_fields=['name', 'published', 'created_at'],
                                   unique_fields=['category_id'],
                                   batch_size=1000)

