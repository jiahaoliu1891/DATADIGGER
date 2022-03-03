# Data Description

API for best seller data: `get.scrapehero.com`

## Structure of json files:
**Best Seller Data**:
* `category`: name of category. Type: `string`. Range: 10 selected categories. Required: True.
* `child_categories`: list of child categories. Type: list of `string`. 
* `product_listings`: list of best seller products within this category, and each contains:
    * `asin`: *unique* id of the product. Type: `string`. Required: True.
    * `name`: product name. Type: `string`. Required: True.
    * `rank`: rank of the product. Type: `int`. Range: 1 ~ 100. Required: True.
    * `rating`: overall product rating. Type: `float`. Range: 1.0 ~ 5.0.
    * `ratings_count`: number of rating. Type: `int`. Range: 1 ~ max.
    * `image`: product image url. Type: `string`.
    * `is_prime`: a boolean flag indicates if it is a Amazon Prime product. Type: `boolean`. 
    * `product_url`: product url. Type: `string`.

**Product Detail Data**:
* `title`: product name. Type: `string`. Required: True.
* `id`: unique id of the product. Type: `string`. Required: True.
* `price`: product price (US dollar). Type: `float`. Range: 0.0 ~ max. 
* `overview`: product overview which contains product feature such as brand, style etc. The feature attribute may vary from category to category. Type: `string`. 
* `discount`: product discount (US dollar). Type: `float`. Range: 0.0 ~ price. 
* `country`: manufacturing country. Type: `string`. Range: countries.
* `quantity`: available quantity.  Type: `int`. Range: 0 ~ max.
* `missOverview`: a boolean flag indicates overview value is missing. Type: `boolean`.
* `missDiscount`: a boolean flag indicates discount value is missing. Type: `boolean`. 
* `missCountry`: a boolean flag indicates country value is missing. Type: `boolean`.
* `missQuantity`:  a boolean flag indicates quantity value is missing. Type: `boolean`.
* `missPrice`: a boolean flag indicates price value is missing. Type: `boolean`. 

