from django.db       import models
from account.models  import Account
from product.models  import TourProduct

class Review(models.Model):
    account         = models.ForeignKey('account.Account', on_delete=models.CASCADE, null=True) 
    travel_objet    = models.ForeignKey('TravelObject', on_delete=models.CASCADE, null=True)
    age             = models.ForeignKey('Age', on_delete=models.CASCADE, null=True)
    content         = models.TextField(null=True)
    grade           = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True, null=True)
    tour_product    = models.ManyToManyField('product.TourProduct', through='ReviewTourProduct', null=True)

    class Meta:
        db_table = 'reviews'

class TravelObject(models.Model):
    travel_object = models.CharField(max_length=100)

    class Meta:
        db_table = 'travel_objects'

class Age(models.Model):
    user_age = models.CharField(max_length=50)

    class Meta:
        db_table = 'age'

class ReviewTourProduct(models.Model):
    review = models.ForeignKey('Review', on_delete=models.SET_NULL, null=True)
    tour_product = models.ForeignKey('product.TourProduct', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'review_tourproduct'

