import os
import pickle
import requests
import json

url = "https://amazon24.p.rapidapi.com/api/product/"

querystring = {"country":"US"}

headers = {
    'x-rapidapi-host': "amazon24.p.rapidapi.com",
    'x-rapidapi-key': "65e0bc754emshb0e232a4c83aee5p1fd330jsndc6e45398c64"
    }


for filename in os.listdir(os.getcwd() + '/bestseller'):
    with open(os.path.join(os.getcwd() + '/bestseller', filename), 'r') as f: # open in readonly mode
        data = json.load(f)

        product_info = []
        for d in data['product_listings']:
            asin = d["asin"]
            if not asin:
                continue
            product_url = url + asin
            response = requests.request("GET", product_url, headers=headers, params=querystring)
            product_info.append(response.text)
            print(filename)
        json_str = json.dumps(product_info)
        output_name = filename.replace(".json", "")+"_detail"+".pkl"
        with open(output_name, 'wb') as outfile:
            pickle.dump(product_info, outfile)