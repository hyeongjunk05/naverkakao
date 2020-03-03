import json

from .models        import Review, TravelObject, Age, ReviewTourProduct
from product.models import TourProduct

from django.views import View
from django.http  import HttpResponse, JsonResponse
from datetime     import datetime,timedelta,timezone

class ReviewView(View):
    def post(self, request, product_id):
        if TourProduct.objects.filter(number=product_id).exists():
            data = json.loads(request.body)

            Review.objects.create(
                content    = data['content'],
                grade      = data['grade'],
            )

            last_review = Review.objects.latest('created_at')

            ReviewTourProduct.objects.create(
                review_id       = last_review.id,
                tour_product_id = TourProduct.objects.filter(number = product_id)[0].id
            )
        
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        return JsonResponse({'message' : 'INVALID_PRODUCT'}, status=200)

    def get(self, request, product_id):
        if TourProduct.objects.filter(number=product_id).exists():

            review_list = []
            [review_list.append({
                'id'      : review_data.review.id,
                'content' : review_data.review.content,
                'grade'   : review_data.review.grade,
                'date'    : review_data.review.created_at
                }) for review_data in ReviewTourProduct.objects.select_related('review').filter(tour_product = TourProduct.objects.get(number = product_id).id)]

            return JsonResponse({'Review_list' : review_list}, status=200)
        return JsonResponse({'message' : 'INVALID_PRODUCT'}, status=200)

class ReviewDetail(View):
    def post(self, request, product_id, review_id):
        if (TourProduct.objects.filter(number=product_id).exists()) and Review.objects.filter(id = review_id).exists():
            data      = json.loads(request.body)
            edit_time = datetime.now(timezone.utc) 

            Review.objects.filter(id=review_id).update(content = data['content'], updated_at = edit_time)

            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        return JsonResponse({'message' : 'INVALID_PRODUCT_OR_REVIEW'}, status=200)

    def delete(self, request, product_id, review_id):
        if (TourProduct.objects.filter(number=product_id).exists()) and Review.objects.filter(id = review_id).exists():
            deleted_review = ReviewTourProduct.objects.get(tour_product = TourProduct.objects.filter(number = product_id)[0].id, review = review_id)
            deleted_review.delete()
        
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        return JsonResponse({'message' : 'INVALID_PRODUCT_OR_REVIEW'}, status=200)









    