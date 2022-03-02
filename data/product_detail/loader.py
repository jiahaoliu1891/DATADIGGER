import pickle
import json
import argparse
import os
import json

def load_products_pkl(filename):
    with open('./pickle/'+filename, 'rb') as f:
        products_str = pickle.load(f) # product data is stored in str format
    products = []
    for s in products_str:
        products.append(json.loads(s))
    return products


class Product():
    def __init__(self, product_info):
        self.title = product_info['product_title'] # 1
        self.id = product_info['product_id'] # 2
        self.price = None # 3
        self.overview = None # 4
        self.discount = None # 5
        self.country = None # 6
        # "rank": 7
        # "cate": 8
        # "ratings_count": 9
        # "rating": 10
        self.quantity = None # 11

        self.missOverview = False
        self.missDiscount = False
        self.missCountry = False
        self.missQuantity = False
        self.missPrice = False

        load_keys = {'price_information', 'product_overview', 'discount', 'country', 'available_quantity'}
        self.load(product_info, load_keys)

    def load(self, product_info, load_keys):
        product_keys = product_info.keys()
        load_keys = load_keys & product_keys
        if 'price_information' not in load_keys:
            self.missPrice = True
            self.price = -1
        else:
            if 'app_sale_price' not in product_info['price_information']\
                    or product_info['price_information']['app_sale_price'] == None:
                self.missPrice = True
                self.price = -1
            else:
                self.price = float(product_info['price_information']['app_sale_price'])

        if 'product_overview' not in load_keys:
            self.missOverview = True
            self.overview = "MISS"
        else:
            self.overview = product_info['product_overview']
            
        if 'discount' not in load_keys:
            self.missDiscount = True
            self.discount = -1.0
        else:
            self.discount = float(product_info['discount'])
            if self.discount < 0:
                # print('Error! price:{} discount:{}'.format(self.price, self.discount))
                self.discount = -1.0
                self.missDiscount = True
    
        if 'country' not in load_keys:
            self.missCountry = True
            self.country = 'UNK'
        else:
            self.country = product_info['country']

        if 'available_quantity' not in load_keys:
            self.missQuantity = True
            self.quantity = -1
        else:
            self.quantity = product_info['available_quantity']

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

def to_json(product):
    json_str = json.dumps(product.__dict__, indent=4)
    with open(f'./json/{product.id}.json', 'w') as f:
        f.write(json_str)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, default='./office_1_detail.pkl')
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--stat', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()

    if args.json:
        # iterate through all the .pkl file and load into Product(), then put them into json file
        for filename in os.listdir('./pickle'):
            if filename[-3:] == 'pkl':
                product_list = load_products_pkl(filename)
                for product_info in product_list:
                    product = Product(product_info)
                    print(product)
                    to_json(product)
    
    if args.demo:
        product_list = load_products_pkl(args.filename)
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