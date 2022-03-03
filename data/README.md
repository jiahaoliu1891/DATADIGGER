# Data Description

API for best seller data: `get.scrapehero.com`

## Structure of json files:
**Best Seller Data**:
* `category`: name of category
* `child_categories`: list of child categories
* `product_listings`: list of best seller products within this category, and each contains:
    * `asin`: unique id of the product
    * `name`: product name
    * `rank`: rank of the product
    * `rating`: overall product rating
    * `image`: product image
    * `is_prime`: a boolean flag indicates if it is a Amazon Prime product
    * `product_url`: product url

**Product Detail Data**:
* `title`: product name
* `id`: unique id of the product
* `price`: product price (US dollar)
* `overview`: product overview which contains product feature such as brand, style etc. The feature attribute may vary from category to category.
* `discount`: product discount (US dollar)
* `country`: manufacturing country
* `quantity`: available quantity
* `missOverview`: a boolean flag indicates overview value is missing 
* `missDiscount`: a boolean flag indicates discount value is missing 
* `missCountry`: a boolean flag indicates country value is missing 
* `missQuantity`:  a boolean flag indicates quantity value is missing 
* `missPrice`: a boolean flag indicates price value is missing 

