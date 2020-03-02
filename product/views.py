import json

from .models      import *

from django.views import View
from django.http  import HttpResponse, JsonResponse

class MainView(View):
    def get(self, request):
        product_list = []

        [product_list.append({'sub_theme' : sub_theme['name'], 'offers' : [{
            'product_name' : product_data.name,
            'product_type' : product_data.category,
            'product_id'   : product_data.id,
            'city_name'    : product_data.city.name,
            'country_name' : product_data.country.name,
            'price'        : Price.objects.filter(tour_product_id = product_data.id)[0].price,
            'origin_price' : Price.objects.filter(tour_product_id = product_data.id)[0].origin_price,
            'thumnail'     : Image.objects.filter(tour_product_id  = product_data.id)[0].thumnail
            }]
            }) for sub_theme in SubTheme.objects.values() for product_data in TourProduct.objects.filter(sub_theme_id = sub_theme['id'])]

   
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
                'course_info'          : [course_object for course_object in Course.objects.filter(tour_product_id = product_data.id).values()],
                'image_info'           : [image_object['product_image'] for image_object in Image.objects.filter(tour_product_id = product_data.id).values()],
                'price_info' : [{
                    'price'            : Price.objects.get(tour_product_id = product_data.id).price,
                    'orgin_price'      : Price.objects.get(tour_product_id = product_data.id).origin_price,
                    'discount_percent' : Price.objects.get(tour_product_id = product_data.id).discount_percent
                }],
            }

            return JsonResponse({'data' : product_info}, status=200)
        return JsonResponse({'data' : []}, status=200)


            
