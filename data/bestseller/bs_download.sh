# Best Seller
# https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_unv_mobile-apps_0_1

echo '1. Best-Sellers-Baby...'
# https://www.amazon.com/Best-Sellers-Baby/zgbs/baby-products/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 Best-Sellers-Baby  --cate2 baby-products | tee ./bestseller/baby_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Baby  --cate2 baby-products | tee ./bestseller/baby_2.json

echo '2. Best-Sellers-Office-Products...'
python bestseller.py --page 1 --cate1 Best-Sellers-Office-Products  --cate2 office-products | tee ./bestseller/office_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Office-Products  --cate2 office-products | tee ./bestseller/office_2.json

echo '3. Best-Sellers-Kitchen-Dining...'
python bestseller.py --page 1 --cate1 Best-Sellers-Kitchen-Dining  --cate2 kitchen | tee ./bestseller/kitchen_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Kitchen-Dining  --cate2 kitchen | tee ./bestseller/kitchen_2.json

echo '4. Best-Sellers-Industrial-Scientific...'
#https://www.amazon.com/Best-Sellers-Industrial-Scientific/zgbs/industrial/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 Best-Sellers-Industrial-Scientific  --cate2 industrial | tee ./bestseller/industrial_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Industrial-Scientific  --cate2 industrial | tee ./bestseller/industrial_2.json

echo '5. best-sellers-camera-photo...'
# https://www.amazon.com/best-sellers-camera-photo/zgbs/photo/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 best-sellers-camera-photo  --cate2 photo | tee ./bestseller/photo_1.json
python bestseller.py --page 2 --cate1 best-sellers-camera-photo  --cate2 photo | tee ./bestseller/photo_2.json

echo '6. Best-Sellers-Musical-Instruments...'
# https://www.amazon.com/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 Best-Sellers-Musical-Instruments  --cate2 musical-instruments | tee ./bestseller/musical_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Musical-Instruments  --cate2 musical-instruments | tee ./bestseller/musical_2.json

echo '7. Best-Sellers-Electronics...'
# https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 Best-Sellers-Electronics  --cate2 electronics | tee ./bestseller/electronics_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Electronics  --cate2 electronics | tee ./bestseller/electronics_2.json

echo '8. Best-Sellers-Magazine-Subscriptions...'
# https://www.amazon.com/Best-Sellers-Magazine-Subscriptions/zgbs/magazines/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 Best-Sellers-Magazine-Subscriptions  --cate2 magazines | tee ./bestseller/magazines_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Magazine-Subscriptions  --cate2 magazines | tee ./bestseller/magazines_2.json

echo '9. Best-Sellers-Sports-Collectibles...'
# https://www.amazon.com/Best-Sellers-Sports-Collectibles/zgbs/sports-collectibles/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 Best-Sellers-Sports-Collectibles  --cate2 sports-collectibles | tee ./bestseller/sports_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Sports-Collectibles  --cate2 sports-collectibles | tee ./bestseller/sports_2.json

echo '10. Best-Sellers-Digital-Educational-Resources...'
# https://www.amazon.com/Best-Sellers-Digital-Educational-Resources/zgbs/digital-educational-resources/ref=zg_bs_nav_0
python bestseller.py --page 1 --cate1 Best-Sellers-Digital-Educational-Resources  --cate2 digital-educational-resources | tee ./bestseller/digital_educational_resources_1.json
python bestseller.py --page 2 --cate1 Best-Sellers-Digital-Educational-Resources  --cate2 digital-educational-resources | tee ./bestseller/digital_educational_resources_2.json
