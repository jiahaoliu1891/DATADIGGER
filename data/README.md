# Tech Report:

### How many data points are there in total?

We collected the bestseller rankings for ten major categories, as well as specific information on the top 100 items under each category. In short, that's 10 times 100 for a thousand products and 10 lists of bestsellers. We divide the above two kinds of data into two data sets for collection and sorting, which take a total of about 745kb of disk space.

### Where is the data from?

In order for the project to have sufficient data for analysis, we collected two datasets. 

#### 1. Product Detail

The Product Detail dataset contains a subset of product information on Amazon. To ensure the accuracy of the data, we used the Product Advertising API officially maintained by Amazon to extract the raw data. Considering this data comes from Amazon itself, we believe it is credible in terms of effectiveness and authenticity. 

As the world's largest e-commerce platform, Amazon has a huge number of products. Considering that our project goal is mainly to predict how likely a product is to be the best seller in its category. We mainly select those products that are on the list of top 100 bestsellers. This can effectively help us analyze the reasons for the success of these products, and avoid receiving too many useless factors. That is to say, we will only select those products with bestseller quality among the vast number of products for analysis, and the quantity of these products will account for a very low proportion of the whole.

We currently have no plans to make special treatment of the ethical issues of these data. Because we believe that Amazon, as a huge public company, must have a more professional team that has already helped us deal with potential ethical issues.

#### 2. Bestseller

The bestseller dataset contains the best-selling ranking information of ten popular categories on Amazon. We use the API provided by scrapehero.com to get the latest ranking data. scrapehero.com is the industry's leading information provider and has been in operation for many years and has a very good reputation on the Internet. 

Since we only analyzed 10 major categories this time, through manual inspection, we found that the information obtained through the API is consistent with the information seen by humans.  Because the data itself also comes from Amazon, we believe that there is no need for us to do additional processing on ethical issues.

### How clean is the data?

We know that for data analysis, the cleanliness of the data is just as important as the accuracy. So we put a lot of effort into cleaning data. We wrote a script specifically to compare whether the data from the two datasets can be successfully matched. For example, if an item on the bestseller list for a category cannot be retrieved via Amazon's API, we will discard the entire category. In other words, our requirements for data integrity are very high.

In the meanwhile, when we extracted the data, we also noticed that the situation of missing values also occurred from time to time. For products with missing data, we will deal with them in two cases according to their impact on the analysis results. For example, if the discount information for an item is missing, we will fill in a default value and mark this item. In some cases, some product information will be seriously missing, such as quantity and price. At this time, we will discard the entry of this product and give up the analysis of the category containing this product, so as to avoid inaccurate analysis results.

It is also worth mentioning that we encountered a lot of duplicate data when collecting data. For example, the same data but stored in different data structures. Fortunately, our script handles this duplication fairly well.

Because we are using an API provided by others, there are not many adjustments we can make on our side. Our guess for missing data and duplication of data is that the API is unstable. So if possible, we will consider looking for alternatives in the future.

### Summary

The problems we encountered with data collection and cleaning were basically as described above. It is mainly reflected in how to select data and how to eliminate the impression of missing data on the analysis results. Our next plan is to try to use more different APIs to improve data consistency and add more fields to each product to improve the accuracy of the upcoming data analysis.



# Data Spec

API for bestseller data: `get.scrapehero.com`

## Structure of JSON files:
**Best Seller Data**:
* `category`: name of the category. Type: `string`. Range: 10 selected categories. Required: True.
* `child_categories`: list of child categories. Type: list of `string`. 
* `product_listings`: list of best seller products within this category, and each contains:
    * `asin`: *unique* id of the product. Type: `string`. Required: True.
    * `name`: product name. Type: `string`. Required: True.
    * `rank`: rank of the product. Type: `int`. Range: 1 ~ 100. Required: True.
    * `rating`: overall product rating. Type: `float`. Range: 1.0 ~ 5.0.
    * `ratings_count`: number of ratings. Type: `int`. Range: 1 ~ max.
    * `image`: product image URL. Type: `string`.
    * `is_prime`: a boolean flag indicates if it is an Amazon Prime product. Type: `boolean`. 
    * `product_url`: product URL. Type: `string`.

**Product Detail Data**:
* `title`: product name. Type: `string`. Required: True.
* `id`: unique id of the product. Type: `string`. Required: True.
* `price`: product price (US dollar). Type: `float`. Range: 0.0 ~ max. 
* `overview`: product overview which contains product features such as brand, style, etc. The feature attribute may vary from category to category. Type: `string`. 
* `discount`: product discount (US dollar). Type: `float`. Range: 0.0 ~ price. 
* `country`: manufacturing country. Type: `string`. Range: countries.
* `quantity`: available quantity.  Type: `int`. Range: 0 ~ max.
* `missOverview`: a boolean flag indicates the overview value is missing. Type: `boolean`.
* `missDiscount`: a boolean flag indicates the discount value is missing. Type: `boolean`. 
* `missCountry`: a boolean flag indicates the country value is missing. Type: `boolean`.
* `missQuantity`:  a boolean flag indicates quantity value is missing. Type: `boolean`.
* `missPrice`: a boolean flag indicates price value is missing. Type: `boolean`. 

#### Product detail sample:

| Field        | Value                                                        |
| ------------ | ------------------------------------------------------------ |
| title        | Texas Instruments TI-30XIIS Scientific Calculator, Black with Blue Accents |
| id           | B00000JBNX                                                   |
| price        | 12.5                                                         |
| overview     | "_Power_Source_": "Solar",  "_Brand_": "Texas Instruments", "_Color_": "Black","_Number_of_Batteries_": "1 CR123A batteries required. (included)","_Model_Name_": "TI-30XIIS\u2122, Black" |
| discount     | 0.0                                                          |
| country      | US                                                           |
| quantity     | 4                                                            |
| missOverview | false                                                        |
| missDiscount | true                                                         |
| missCountry  | false                                                        |
| missQuantity | false                                                        |
| missPrice    | false                                                        |





















