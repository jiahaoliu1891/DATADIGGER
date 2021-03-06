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
        if 'product_title' not in product_info.keys(): # only one data sample do not have product title 
            self.title = 'UNK' # 1
        else:
            self.title = product_info['product_id']

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
            self.price = 0
        else:
            if 'app_sale_price' not in product_info['price_information']\
                    or product_info['price_information']['app_sale_price'] == None:
                self.missPrice = True
                self.price = 0
            else:
                self.price = float(product_info['price_information']['app_sale_price'])

        if 'product_overview' not in load_keys:
            self.missOverview = True
            self.overview = "MISS"
        else:
            self.overview = product_info['product_overview']
            
        if 'discount' not in load_keys:
            self.missDiscount = True
            self.discount = 0.0
        else:
            self.discount = float(product_info['discount'])
            if self.discount < 0:
                # print('Error! price:{} discount:{}'.format(self.price, self.discount))
                self.discount = 0.0
                self.missDiscount = True
    
        if 'country' not in load_keys:
            self.missCountry = True
            self.country = 'UNK'
        else:
            self.country = product_info['country']

        if 'available_quantity' not in load_keys:
            self.missQuantity = True
            self.quantity = 0
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

def statistics():
    import numpy as np
    import matplotlib.pyplot as plt

    misses = {'missPrice': 0, 'missOverview': 0, 'missCountry': 0, 'missQuantity': 0, 'missDiscount': 0}
    prices, quantities, discount = [], [], []

    cnt = 0

    for filename in os.listdir('./json'):
        with open(f'./json/{filename}', 'r') as f:
            cnt += 1
            product = json.load(f)
            # miss data stat
            for key in misses.keys():
                if product[key]:
                    misses[key] += 1
            # range of price
            if not product['missPrice']:
                prices.append(product['price'])
            
            if not product['missQuantity']:
                quantities.append(product['quantity'])

            if not product['missDiscount']:
                discount.append(product['discount'])
    
    print(f'Total Product Number: {cnt}')
    print(f'Miss Data Stat:\n{misses}')
    print(f'Price Range: {np.min(prices)} ~ {np.max(prices)}, mean:{np.mean(prices)}, std: {np.std(prices)}, median:{np.median(prices)}')
    print(f'Quantity Range: {np.min(quantities)} ~ {np.max(quantities)}, mean:{np.mean(quantities)}, std: {np.std(quantities)}, median:{np.median(quantities)}')
    print(f'Discount Range: {np.min(discount)} ~ {np.max(discount)}, mean:{np.mean(discount)}, std: {np.std(discount)}, median:{np.median(discount)}')

    plt.hist(quantities, bins=100, range=(0, 500))
    plt.show()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, default='./office_1_detail.pkl')
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--stat', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()

    if args.stat:
        statistics()

    if args.json:
        pid_set = set() # record product id
        # iterate through all the .pkl file and load into Product(), then put them into json file
        for filename in os.listdir('./pickle'):
            if filename[-3:] == 'pkl':
                product_list = load_products_pkl(filename)
                N = len(product_list) # number of products in the file
                print(f'--- Dealing with {filename}, num:{N}')
                for product_info in product_list:
                    product = Product(product_info)
                    if product.id in pid_set:
                        print('Duplicated!')
                        print(product)
                    else:
                        pid_set.add(product.id)
                        # print(product)
                        to_json(product)

        print(f'number :{len(pid_set)}')
    
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