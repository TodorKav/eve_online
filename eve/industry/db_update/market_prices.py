import os
import django
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eve.settings")
django.setup()

import requests
from django.db import transaction
from eve.industry.models import MarketPrices

url_categories = 'https://esi.evetech.net/markets/prices'

TIMEOUT = (15, 30)

market_prices_list = requests.get(url_categories, timeout=TIMEOUT).json()

with transaction.atomic():
    object_list = []
    for item in tqdm(market_prices_list):
        object_list.append(MarketPrices(
            type_id_id=item.get('type_id'),
            adjusted_price=item.get('adjusted_price'),
            average_price=item.get('average_price'),
        ))
    MarketPrices.objects.bulk_create(object_list,
                                     update_conflicts=True,
                                     update_fields=['adjusted_price', 'average_price', 'created_at',],
                                     unique_fields=['type_id',],
                                     batch_size=1000)
