import http.client
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--page', type=int)
parser.add_argument('--cate1', type=str)
parser.add_argument('--cate2', type=str)

args = parser.parse_args()

page_num, cate1, cate2 = args.page, args.cate1, args.cate2

# page_num, cate1, cate2 = 1, 'Best-Sellers-Baby', 'baby-products'

conn = http.client.HTTPSConnection("get.scrapehero.com")
api_key = 'jZc3AEzkhWaVOBUfBbCoNSYaQQP3f3Bg'
# Best-Sellers-Baby/zgbs/baby-products
url = '/amz/best-sellers/?x-api-key={}&url=https%3A%2F%2Fwww.amazon.com%2F{}%2Fzgbs%2F{}%2Fref%3Dzg_bs_nav_0&page={}'.format(api_key, cate1, cate2, page_num)
# url = '/amz/best-sellers/?x-api-key={}&url=https%3A%2F%2Fwww.amazon.com%2FBest-Sellers-Appstore-Android%2Fzgbs%2Fmobile-apps%2Fref%3Dzg_bs_nav_0&page={}'.format(api_key,page_num)
conn.request("GET", url)
res = conn.getresponse()
data = res.read()

print(data)
