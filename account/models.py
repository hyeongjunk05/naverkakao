from django.db import models


class Account(models.Model):
    social_id        = models.CharField(max_length=50, null=True)
    username         = models.CharField(max_length=50, null=True)
    email            = models.EmailField(max_length=50, unique=True, null=True)
    password         = models.CharField(max_length=500)
    agree_location   = models.NullBooleanField()
    agree_promotion  = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    profile          = models.URLField(max_length=500, null=True, blank=True)
    phone            = models.IntegerField(null=True, blank=True, default=31874599)

    class Meta:
        db_table = 'accounts'
