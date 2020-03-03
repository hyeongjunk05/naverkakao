import json

from .models        import *
from product.models import *

from django.views import View
from django.http  import HttpResponse, JsonResponse
from datetime     import datetime,timedelta,timezone

class CreateReview(View):
    def post(self, request, product_id):
        data = json.loads(request.body)

        Review.objects.create(
            content = data['content'],
            grade   = data['grade']
        )

        ReviewTourProduct.objects.create(
            review_id       = Review.objects.filter(content = data['content'])[0].id,
            tour_product_id = TourProduct.objects.filter(number = product_id)[0].id
        )
        
        return HttpResponse(status=200)

class UpadteReview(View):
    def post(self, request, product_id):
        
        return HttpResponse(status=200)

class DeleteReview(View):
    def post(self, request, product_id):

        return HttpResponse(status=200)

class ReadReview(View):
    def get(self, request, product_id):
        review_list = []
        [review_list.append({
            'text'  : review_data.review.content,
            'grade' : review_data.review.grade,
            'data'  : review_data.review.created_at
            }) for review_data in ReviewTourProduct.objects.select_related('review').filter(tour_product = TourProduct.objects.get(number = product_id).id)]

        return JsonResponse({'Review_list' : review_list}, status=200)