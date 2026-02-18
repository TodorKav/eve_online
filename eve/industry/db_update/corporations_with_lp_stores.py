import os
import django
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eve.settings")
django.setup()

import requests
from django.db import transaction
from eve.industry.models import CorporationsWithLPStores

npc_corp_url = 'https://esi.evetech.net/corporations/npccorps'
corp_url = 'https://esi.evetech.net/corporations/'
url_loyalty_stores = 'https://esi.evetech.net/loyalty/stores/'

TIMEOUT = (15, 30)

session = requests.Session()
pages = int(session.get(npc_corp_url, timeout=TIMEOUT).headers.get('X-Pages', 1))
corp_list = []
for page in tqdm(range(1, pages +1)):
    corp_list += session.get(f'{npc_corp_url}?page={page}', timeout=TIMEOUT).json()


with transaction.atomic():
    object_list = []
    # we filter and add in DB only the corporations that have LP stores
    for corporation in tqdm(corp_list):
        temp = session.get(f'{url_loyalty_stores}{corporation}/offers/', timeout=TIMEOUT).json()
        if temp:
            object_json = session.get(f'{corp_url}{corporation}/', timeout=TIMEOUT).json()
            object_list.append(CorporationsWithLPStores(
                corporation_id=corporation,
                description=object_json.get('description'),
                home_station_id=object_json.get('home_station_id'),
                name=object_json.get('name'),
                ticker=object_json.get('ticker'),
                war_eligible=object_json.get('war_eligible'),
                ))
    CorporationsWithLPStores.objects.bulk_create(object_list,
                                                 update_conflicts=True,
                                                 update_fields=['description', 'home_station_id',
                                                                'name', 'ticker', 'war_eligible'],
                                                 unique_fields=['corporation_id',],
                                                 batch_size=1000)


