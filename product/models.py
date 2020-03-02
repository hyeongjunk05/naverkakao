from django.db import models

class TourProduct(models.Model):
    name              = models.CharField(max_length = 200)
    number            = models.IntegerField(null=True)
    category          = models.CharField(max_length = 200)
    group             = models.CharField(max_length = 45, null=True)
    duration          = models.CharField(max_length = 45, null=True)
    language          = models.CharField(max_length = 45, null=True)
    transportation    = models.CharField(max_length = 45, null=True)
    description_title = models.TextField(null=True)
    description       = models.TextField(null=True)
    notice_title      = models.TextField(null=True)
    notice            = models.TextField(null=True)
    amenity           = models.TextField(null=True)
    non_amenity       = models.TextField(null=True)
    meeting_time      = models.CharField(max_length = 100, null=True)
    address           = models.CharField(max_length = 100, null=True)
    latitude          = models.DecimalField(max_digits = 20, decimal_places = 10, null=True)
    longitude         = models.DecimalField(max_digits = 20, decimal_places = 10, null=True)
    main_theme        = models.ForeignKey('MainTheme', on_delete = models.CASCADE, null=True, blank=True)
    sub_theme         = models.ForeignKey('SubTheme', on_delete = models.CASCADE, null=True, blank=True)
    city              = models.ForeignKey('City', on_delete = models.CASCADE, null=True, blank=True)
    country           = models.ForeignKey('Country', on_delete = models.CASCADE, null=True, blank=True)
    guide             = models.ForeignKey('Guide', on_delete = models.CASCADE, null=True, blank=True)

    class Meta:
         db_table = 'tour_products'

class MainTheme(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'main_themes'

class SubTheme(models.Model):
    name           = models.CharField(max_length = 45)
    
    class Meta:
        db_table = 'sub_themes'

class Image(models.Model):        
    thumnail       = models.URLField(max_length = 500)
    product_image  = models.URLField(max_length = 500)
    tour_product   = models.ForeignKey('TourProduct', on_delete = models.CASCADE)

    class Meta:
        db_table = 'images'

class Price(models.Model): 
    origin_price     = models.IntegerField()
    price            = models.IntegerField()
    discount_percent = models.IntegerField()
    tour_product     = models.ForeignKey('TourProduct', on_delete = models.CASCADE)

    class Meta:
        db_table = 'price'

class Course(models.Model):
    name            = models.TextField(null=True)
    description     = models.TextField(null=True)
    image           = models.URLField(max_length = 500)
    tour_product    = models.ForeignKey('TourProduct', on_delete = models.CASCADE)

    class Meta:
        db_table = 'courses'


class Guide(models.Model):
    name          = models.TextField(null=True)
    description   = models.TextField(null=True)
    image         = models.URLField(max_length = 500)

    class Meta:
        db_table = 'guides'

class City(models.Model):
    name    = models.CharField(max_length = 45)
    country = models.ForeignKey('Country', on_delete = models.CASCADE)

    class Meta:
        db_table = 'cities'

class Country(models.Model):
    name   = models.CharField(max_length = 45)
    number = models.CharField(max_length = 45)

    class Meta:
        db_table = 'countries'
