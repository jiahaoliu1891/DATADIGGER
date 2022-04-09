import numpy as np
import pandas as pd
import json
import os

DATAPATH_JSON = './bsData'

bs_rows = []
bs_overview = {}
for filename in os.listdir(DATAPATH_JSON):
    with open(f'{DATAPATH_JSON}/{filename}', 'r') as f:
        bs = json.load(f)
        # remove child_categories, next and url from the list
        bs.pop('child_categories')
        bs.pop('next')
        bs.pop('url')
        # now only category and product_listings left
        _category, _product_listings = bs['category'], bs['product_listings']
        for product_listing in _product_listings:
            _id, _rank, _name, _ratings_count, _rating = product_listing['asin'], product_listing['rank'], product_listing['name'], product_listing[
                'ratings_count'], product_listing['rating']
            if _id == None:
                continue
            temp = [_id, _rank, _name, _ratings_count, _rating, _category]
            bs_rows.append(temp)
# print(bs_rows)

df_bs = pd.DataFrame(bs_rows)
df_bs.columns = ['asin', 'rank', 'name', 'ratings_count', 'rating', 'category']
print(df_bs)

# flatten the df
# df_bs = pd.json_normalize(
#     df_bs_nested,
#     record_path=['product_listings'],
#     meta=['category']
# )