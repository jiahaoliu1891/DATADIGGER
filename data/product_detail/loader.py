import pickle
import json
import argparse

def load_products_pkl(filename):
    with open(filename, 'rb') as f:
        products_str = pickle.load(f) # product data is stored in str format
    products = []
    for s in products_str:
        products.append(json.loads(s))
    return products


class Product():
    def __init__(self, product_dict):
        # ten attributes
        self.title = product_dict['product_title'] # 1
        self.id = product_dict['product_id'] # 2
        self.price = None # 3
        self.overview = None # 4
        self.discount = None # 5
        self.country = None # 6
        # "rank": 7
        # "cate": 8
        # "ratings_count": 9
        # "rating": 10
        self.quantity = None # 11
        load_keys = {'price_information', 'product_overview', 'discount', 'country', 'available_quantity'}
        self.load(product_dict, load_keys)

    def load(self, product_dict, load_keys):
        product_keys = product_dict.keys()
        load_keys = load_keys & product_keys
        if 'price_information' not in load_keys:
            self.missPrice = True
        else:
            if 'app_sale_price' not in product_dict['price_information']\
                    or product_dict['price_information']['app_sale_price'] == None:
                self.missPrice = True
            else:
                self.price = float(product_dict['price_information']['app_sale_price'])

        if 'product_overview' not in load_keys:
            self.missOverview = True
        else:
            self.overview = product_dict['product_overview']
            
        if 'discount' not in load_keys:
            self.missDiscount = True
        else:
            self.discount = float(product_dict['discount'])
            if self.discount < 0:
                # print('Error! price:{} discount:{}'.format(self.price, self.discount))
                self.discount = None
                self.missDiscount = True
    
        if 'country' not in load_keys:
            self.missCountry = True
        else:
            self.country = product_dict['country']

        if 'available_quantity' not in load_keys:
            self.missQuantity = True
        else:
            self.quantity = product_dict['available_quantity']


    def __str__(self):
        string = '### Product title\n{}\n'.format(self.title)
        string += '### Product ID\n{}\n'.format(self.id)
        string += '### Product country\n{}\n'.format(self.country)
        string += '### Product price\n{}\n'.format(self.price)
        string += '### Product discount\n{}\n'.format(self.discount)
        string += '### Product overview\n{}\n'.format(self.overview)
        string += '### Product Quantity\n{}\n'.format(self.quantity)
        return string
    
    def insert_sql(self, table):
        # generate insert SQL clause 
        # TODO
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, default='./office_1_detail.pkl')
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--stat', action='store_true')
    args = parser.parse_args()

    # get list of product data, each one is a dict obj
    product_list = load_products_pkl(args.filename)

    if args.demo:
        for i in range(50):
            print(f'=== Demo Product {i} ===')
            print(product_list[i]['available_quantity']) 
            product = Product(product_list[i])
            print(product)

"""
product keys:
    noResults
    modificationDate
    product_small_image_urls
    product_information_html
    feature_bullets
    _id
    variantAsin
    variantImages
    variantSizes
    isPrime
    product_id
    product_title
    message
    product_detail_url
    original_price
    app_sale_price
    currency
    discount
    product_overview
    product_details
    product_technical_spec
    product_main_image_url
    available_quantity
    breadcrumbs
    price_information
    country
    competitors_history
    sales_history
    reviews_history
    __v
"""