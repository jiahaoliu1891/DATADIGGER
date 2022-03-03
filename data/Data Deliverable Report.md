## Tech Report:

### How many data points are there in total?

We collected the bestseller rankings for ten major categories, as well as specific information on the top 100 items under each category. In short, that's 10 times 100 for a thousand products and 10 lists of bestsellers. We divide the above two kinds of data into two data sets for collection and sorting, which take a total of about 745kb of disk space.

### Where is the data from?

In order for the project to have sufficient data for analysis, we collected two datasets. 

#### 1. Product Detail

The Product Detail dataset contains a subset of product information on Amazon. To ensure the accuracy of the data, we used the Product Advertising API officially maintained by Amazon to extract the raw data. Considering this data comes from Amazon itself, we believe it is credible in terms of effectiveness and authenticity. 

As the world's largest e-commerce platform, Amazon has a huge number of products. Considering that our project goal is mainly to predict how likely a product is to be the best seller in its category. We mainly select those products that are on the list of top 100 bestsellers. This can effectively help us analyze the reasons for the success of these products, and avoid receiving too many useless factors. That is to say, we will only select those products with bestseller quality among the vast number of products for analysis, and the quantity of these products will account for a very low proportion of the whole.

We currently have no plans to make special treatment of the ethical issues of these data. Because we believe that Amazon, as a huge public company, must have a more professional team that has already helped us deal with potential ethical issues.

#### 2. Bestseller

The bestseller dataset contains the best-selling ranking information of ten popular categories on Amazon. We use the API provided by scrapehero.com to get the latest ranking data. scrapehero.com is the industry's leading information provider and has been in operation for many years and has a very good reputation on the Internet. Because we only analyzed 10 major categories this time, through manual inspection, we found that the information obtained through the API is consistent with the information seen by humans.  Because the data itself also comes from Amazon, we believe that there is no need for us to do additional processing on ethical issues.

### How clean is the data?

How did you check for the cleanliness of your data? 

What was your threshold reference?

Did you implement any mechanism to clean your data? If so, what did you do?

Are there missing values? Do these occur in fields that are important for your project's goals?

Are there duplicates? Do these occur in fields that are important for your project's goals?

How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)Are there any data type issues (e.g. words in fields that were supposed to be numeric)? 

Where are these coming from? (E.g. a bug in your scraper? User input?) 

How will you fix them?

Do you need to throw any data away? 

What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?



## Data Spec

#### bestseller

10 Category, each category has its subcategories. And top 100 bestseller products.

#### product detail sample:

| Field        | Value                                                        |
| ------------ | ------------------------------------------------------------ |
| title        | Texas Instruments TI-30XIIS Scientific Calculator, Black with Blue Accents |
| id           | B00000JBNX                                                   |
| price        | 12.5                                                         |
| overview     | "_Power_Source_": "Solar",  "_Brand_": "Texas Instruments", "_Color_": "Black","_Number_of_Batteries_": "1 CR123A batteries required. (included)","_Model_Name_": "TI-30XIIS\u2122, Black" |
| discount     | -1.0                                                         |
| country      | US                                                           |
| quantity     | 4                                                            |
| missOverview | false                                                        |
| missDiscount | true                                                         |
| missCountry  | false                                                        |
| missQuantity | false                                                        |
| missPrice    | false                                                        |

























