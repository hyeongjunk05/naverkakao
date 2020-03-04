import json

from django.views   import View
from django.http    import HttpResponse, JsonResponse
from datetime       import datetime,timedelta,timezone

from .models        import Review, TravelObject, Age, ReviewTourProduct
from product.models import TourProduct
from account.models import Account
from account.utils  import login_requested

class ReviewView(View):
    @login_requested
    def post(self, request, product_id):
        try:
            if TourProduct.objects.filter(number=product_id).exists():
                data = json.loads(request.body)

                Review.objects.create(
                    content    = data['content'],
                    grade      = data['grade'],
                    account    = request.agent
                )

                last_review = Review.objects.latest('created_at')

                ReviewTourProduct.objects.create(
                    review_id       = last_review.id,
                    tour_product_id = TourProduct.objects.get(number = product_id).id
                )

                return HttpResponse(status=200)
            return JsonResponse({'message' : 'INVALID_PRODUCT'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)

    def get(self, request, product_id):
        review_list = [{
            'id'      : review_data.review.id,
            'name'    : review_data.review.account.username,
            'content' : review_data.review.content,
            'grade'   : review_data.review.grade,
            'date'    : review_data.review.created_at
            } for review_data in ReviewTourProduct.objects.select_related('review').filter(tour_product__number = product_id)]

        return JsonResponse({'Review_list' : review_list}, status=200)

class ReviewDetail(View):
    @login_requested
    def post(self, request, product_id, review_id):
        try:
            if TourProduct.objects.filter(number=product_id).exists() and Review.objects.filter(id = review_id).exists():
                if Review.objects.get(id = review_id).account == request.agent:

                    data      = json.loads(request.body)
                    edit_time = datetime.now(timezone.utc) 

                    Review.objects.filter(id=review_id).update(
                        content = data['content'], 
                        updated_at = edit_time, 
                    )

                    return HttpResponse(status=200)

                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            return JsonResponse({'message' : 'INVALID_PRODUCT_OR_REVIEW'}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)

    @login_requested
    def delete(self, request, product_id, review_id): 
        try:
            if TourProduct.objects.filter(number=product_id).exists() and Review.objects.filter(id = review_id).exists():
                if Review.objects.get(id = review_id).account == request.agent:
                    deleted_review = ReviewTourProduct.objects.get(
                        tour_product = TourProduct.objects.get(number = product_id).id, 
                        review = review_id
                    )

                    deleted_review.delete()

                    return HttpResponse(status=200)
                    
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            return JsonResponse({'message' : 'INVALID_PRODUCT_OR_REVIEW'}, status=200)

        except ReviewTourProduct.DoesNotExist:
            return HttpResponse(status=404)





