import json

from .models      import TourProduct, SubTheme, Image, Price, Course, Guide, City, CityImage, Country

from django.views import View
from django.http  import HttpResponse, JsonResponse

class MainView(View):
    def get(self, request):

        product_list = [
            {
                'sub_theme' : sub_theme['name'], 
                'offers'    : [
                    {
                        'name'         : product_data.name,
                        'type'         : product_data.category,
                        'id'           : product_data.number,
                        'city_name'    : product_data.city.name,
                        'country_name' : product_data.country.name,
                        'review_count' : product_data.review_count,
                        'review_grade' : product_data.review_grade,
                        'price'        : Price.objects.filter(tour_product_id = product_data.id)[0].price,
                        'origin_price' : Price.objects.filter(tour_product_id = product_data.id)[0].origin_price,
                        'thumnail'     : Image.objects.filter(tour_product_id  = product_data.id)[0].thumnail
                    } for product_data in TourProduct.objects.filter(sub_theme_id = sub_theme['id'])]
            } for sub_theme in SubTheme.objects.values()[:3]]
 
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
                'address'              : product_data.address,
                'address_map'          : product_data.address_map,
                'meeting_time'         : product_data.meeting_time,
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
    def get(self, request):
        try:
            query = request.GET.get('query', '')
            product_list = TourProduct.objects.select_related('city').filter(city__name__contains = query)    

            if len(product_list) == 0:
                return JsonResponse({'message' : 'PRODUCT_DOES_NOT_EXISTS'}, status=400)

            background_list = [
                {
                    'background_image'    : CityImage.objects.get(city = product_list[0].city.id).image,
                    'country_name'        : product_list[0].country.name,
                    'city_name'           : product_list[0].city.name,
                    'city_english_name'   : product_list[0].city.english_name,
                    'country_english_name' : product_list[0].country.english_name,
                    'city_list'           : [city_object['name'] for city_object in City.objects.filter(country = product_list[0].country.id).values()]    
                 }
            ]
            
            search_list = [
                {
                    'sub_theme' : SubTheme.objects.get(id=4).name, 
                    'offers'    : [
                        {
                            'id'           : product.id,
                            'name'         : product.name,
                            'country_name' : product.country.name,
                            'city_name'    : product.city.name,
                            'type'         : product.category,
                            'review_count' : product.review_count,
                            'review_grade' : product.review_grade,
                            'price'        : Price.objects.filter(tour_product = product.id)[0].price,
                            'thumnail'     : Image.objects.filter(tour_product = product.id)[0].thumnail
                        } for product in product_list 
                    ]
                }
            ] 

            return JsonResponse({'background_data' : background_list, 'product_data' : search_list}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)
