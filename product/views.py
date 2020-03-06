import json

from .models       import TourProduct, MainTheme, SubTheme, Image, Price, Course, Guide, City, Country, Recommendation
from review.models import Review

from django.views     import View
from django.http      import HttpResponse, JsonResponse
from django.db.models import Avg, Count


class MainView(View):
    def get(self, request, category):

        product_list = []

        if category == 'tour':
            main_object = MainTheme.objects.get(key=category)

            product_list = [
                {
                    'sub_theme' : sub_theme['name'], 
                    'offers'    : [
                        {
                            'name'           : product_data.name,
                            'type'           : product_data.category,
                            'id'             : product_data.number,
                            'city_name'      : product_data.city.name,
                            'country_name'   : product_data.country.name,
                            'price'          : Price.objects.filter(tour_product = product_data.id)[0].price,
                            'origin_price'   : Price.objects.filter(tour_product = product_data.id)[0].origin_price,
                            'thumnail'       : Image.objects.filter(tour_product = product_data.id)[0].thumnail,
                            'review_count'   : Review.objects.filter(tour_product = product_data.id).aggregate(Count('rating'))['rating__count'],
                            'average_rating' : Review.objects.filter(tour_product = product_data.id).aggregate(Avg('rating'))['rating__avg'],
                        } for product_data in TourProduct.objects.filter(sub_theme_id = sub_theme['id'])]
                } for sub_theme in SubTheme.objects.filter(main_theme = main_object.id).values()]
                
            return JsonResponse({'data' : product_list}, status=200)

        return JsonResponse({'data' : product_list}, status=200)
            


class ProductView(View):
    def get(self, request, product_id):

        product_info = []
     
        if TourProduct.objects.filter(number=product_id).exists():
            product_data = TourProduct.objects.get(number=product_id)

            product_info = {
                'name'                 : product_data.name,
                'city'                 : product_data.city.name,
                'country'              : product_data.country.name,
                'meeting_time'         : product_data.meeting_time,
                'guide_name'           : product_data.guide.name,
                'guide_description'    : product_data.guide.description,
                'guide_image'          : product_data.guide.image,
                'group'                : product_data.group,
                'duration'             : product_data.duration,
                'language'             : product_data.language,
                'transportation'       : product_data.transportation,
                'description_title'    : product_data.description_title,
                'description'          : product_data.description,
                'notice_title'         : product_data.notice_title,
                'notice'               : product_data.notice,
                'amenity'              : product_data.amenity,
                'non_amenity'          : product_data.non_amenity,
                'latitude'             : product_data.latitude,
                'longitude'            : product_data.longitude,
                'address'              : product_data.address,
                'address_map'          : product_data.address_map,
                'average_rating'       : Review.objects.filter(tour_product = product_data.id).aggregate(Avg('rating'))['rating__avg'],
                'course_info'          : [course_object for course_object in Course.objects.filter(tour_product_id = product_data.id).values()],
                'image_info'           : [image_object['product_image'] for image_object in Image.objects.filter(tour_product_id = product_data.id).values()],
                'price_info' : [
                    {
                        'price'            : Price.objects.get(tour_product_id = product_data.id).price,
                        'orgin_price'      : Price.objects.get(tour_product_id = product_data.id).origin_price,
                        'discount_percent' : Price.objects.get(tour_product_id = product_data.id).discount_percent
                    }
                ],
            }

            return JsonResponse({'data' : product_info}, status=200)
        return JsonResponse({'data' : []}, status=200)


class SearchView(View):
    def get(self, request, category):

        try:
            if category == 'search':
    
                main_object = MainTheme.objects.get(key=category)
                query = request.GET.get('query', '')

                product_object = TourProduct.objects.prefetch_related('city').filter(city__english_name__contains = query)
                
                background_list = [
                    {
                        'background_image'     : product_object[0].city.image,
                        'country_name'         : product_object[0].country.name,
                        'city_name'            : product_object[0].city.name,
                        'city_english_name'    : product_object[0].city.english_name,
                        'country_english_name' : product_object[0].country.english_name,
                        'city_list'            : [city_object['name'] for city_object in City.objects.filter(country = product_object[0].country.id).values()]    
                     }
                ]
            
                search_list = [element.name for element in product_object]


                recommendation_list = [
                    {
                        'local_list' : [product_object[0].city.name + ',' + product_object[0].country.name],
                        'place_list' : [object['recommendation_list'] for object in Recommendation.objects.values()]
                    }
                ]


                product_list = [
                    {
                        'sub_theme' : SubTheme.objects.get(main_theme = main_object.id).name, 
                        'offers'    : [
                            {
                                'id'             : product.id,
                                'name'           : product.name,
                                'country_name'   : product.country.name,
                                'city_name'      : product.city.name,
                                'city_eng_name'  : product.city.english_name,
                                'type'           : product.category,
                                'price'          : product.price_set.filter(tour_product = product.id)[0].price,
                                'thumnail'       : product.image_set.filter(tour_product = product.id)[0].thumnail,
                                'review_count'   : product.review_set.aggregate(Count('rating'))['rating__count'],
                                'average_rating' : product.review_set.aggregate(Avg('rating'))['rating__avg']

                            } for product in product_object 
                        ]
                    }
                ] 

                return JsonResponse({'background_data' : background_list, 'recommendation_data' : recommendation_list, 'product_data' : product_list}, status=200)
            return JsonResponse({'data' : []}, status=200)

        except IndexError:
            return JsonResponse({'message' : 'INVALID_QUERY'}, status=400)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)
