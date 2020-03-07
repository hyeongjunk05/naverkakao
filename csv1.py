import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myfaketrip.settings")

import django

django.setup()

from product.models import *
from review.models import *
from account.models import *



'''
추천 검색어
'''
CSV_PATH = '/Users/wave/Desktop/csv/recommend.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Recommendation.objects.create(
			recommendation_list = row['recommendation']
		)


'''
국가 정보 입력
'''

CSV_PATH = '/Users/wave/Desktop/csv/countries.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Country.objects.create(
			name = row['name'],
			english_name = row['english_name'],
            number = row['number'],
		)

'''
도시 정보 입력
'''

CSV_PATH = '/Users/wave/Desktop/csv/cities.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		City.objects.create(
			name = row['name'],
			english_name = row['english_name'],
			image = row['image'],
            country_id = row['country_id'],
		)


'''
메인 카테고리 입력
'''
CSV_PATH = '/Users/wave/Desktop/csv/main_theme.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		MainTheme.objects.create(
			name 		 = row['name'],
			key = row['english_name']
		)

'''
서브 카테고리 입력
'''
CSV_PATH = '/Users/wave/Desktop/csv/sub_theme.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		SubTheme.objects.create(
			name 		  = row['name'],
			main_theme_id = row['main_theme_id']
		)

'''
가이드 정보 입력
'''
CSV_PATH = '/Users/wave/Desktop/csv/guide.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Guide.objects.create(
			name = row['name'],
            description = row['description'],
            image = row['image']
		)

'''
투어&티켓 상품 입력
'''
CSV_PATH = '/Users/wave/Desktop/csv/tour_product.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		TourProduct.objects.create(
			name = row['name'],
            number = row['number'],
            category = row['category'],
            group = row['group'],
            duration = row['duration'],
            language = row['language'],
            transportation = row['transportation'],
            description_title = row['description_title'],
            description = row['description'],
            notice_title = row['notice_title'],
            notice = row['notice'],
            amenity = row['amenity'],
            non_amenity = row['non_amenity'],
            meeting_time = row['meeting_time'],
            address = row['address'],
            address_map = row['address_map'],
            latitude = row['latitude'],
            longitude = row['longitude'],
            main_theme_id = row['main_theme_id'],
            sub_theme_id = row['sub_theme_id'],
            city_id = row['city_id'],
            country_id = row['country_id'],
            guide_id = row['guide_id']
		)

'''
이미지 입력
'''
CSV_PATH = '/Users/wave/Desktop/csv/image.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Image.objects.create(
			thumnail = row['thumnail'],
            product_image = row['product_image'],
            tour_product_id = row['tour_product_id'],
		)


'''
코스 정보 입력
'''
CSV_PATH = '/Users/wave/Desktop/csv/course.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Course.objects.create(
			name = row['name'],
            description = row['description'],
            image = row['image'],
            tour_product_id = row['tour_product_id']
		)


'''
가이드
'''
CSV_PATH = '/Users/wave/Desktop/csv/guide.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Guide.objects.create(
			name = row['name'],
            description = row['description'],
            image = row['image'],
		)


'''
가격 
'''
CSV_PATH = '/Users/wave/Desktop/csv/price.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Price.objects.create(
			origin_price = row['origin_price'],
            price = row['price'],
            discount_percent = row['discount_percent'],
            tour_product_id = row['tour_product_id'],
		)


'''
여행 목적
'''

CSV_PATH = '/Users/wave/Desktop/csv/object.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		TravelObject.objects.create(
			travel_object = row['object'],
		)



'''
연령대 입력
'''

CSV_PATH = '/Users/wave/Desktop/csv/age.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		Age.objects.create(
			user_age = row['age'],
		)







