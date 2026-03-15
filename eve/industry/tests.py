# import os
# import django
# from tqdm import tqdm
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eve.settings')  # Adjust to your settings module path
# django.setup()
# from eve.industry.models import CorporationsLpItemTypes, Types
#
# #
# #
# # xx = CorporationsLpItemTypes.objects.all()
# # x = CorporationsLpItemTypes.objects.all().count()
# # y = CorporationsLpItemTypes.objects.filter(required_items=[]).count()
# #
# # count = 0
# # for i in xx:
# #     if (len(i.required_items)) > 0:
# #         count += 1
# #
# #
# # print(f'Общ брой елементи: {x}')
# # print(y)
# # print(count)
#
# print("Calculating material costs...")
# all_lp_items = (CorporationsLpItemTypes.objects.exclude(required_items=[]).exclude(required_items__isnull=True).select_related('type_id'))
# all_type_ids = set() # set af all type_id's in the required_items: {type_id, ...}
# for obj in all_lp_items:
#     for content in obj.required_items:
#         all_type_ids.add(content.get('type_id'))
#
# # Fetch all needed Types + their market prices in one query: {type_id: price}
# type_prices = {
#     t.type_id: t.market_prices.adjusted_price
#     for t in Types.objects.filter(type_id__in=all_type_ids).select_related('market_prices')
#     if hasattr(t, 'market_prices') and t.market_prices
# }
#
# # Compute material_cost per LP item and bulk update
# to_update = []
# content_list = [] # column analog to required_items but with type_id.name and quantity, for template representation
# for obj in tqdm(all_lp_items, desc="Computing material costs"):
#     material_cost = 0.0
#     has_missing_price = False
#
#     for content in obj.required_items:
#         type_id = content.get('type_id')
#         quantity = content.get('quantity', 0)
#         price = type_prices.get(type_id)
#
#         if price is None:
#             has_missing_price = True
#             break
#         material_cost += price * quantity
#
#         content_list.append(f'Item: {obj.type_id.name} quantity: {quantity}.')
#
#     obj.required = ', '.join(content_list)
#     obj.material_cost = None if has_missing_price else material_cost
#
#
