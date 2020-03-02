from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50)
    # 여기서 unique = True 하면 이메일의 고유성 확립되나 확인하기
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=500)
    agree_all = models.NullBooleanField()
    agree_rule = models.BooleanField(default=False)
    agree_info = models.BooleanField(default=False)
    agree_location = models.NullBooleanField()
    agree_promotion = models.NullBooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.URLField(max_length=500, null=True, blank=True)
    phone = models.IntegerField(blank=True)
    refund_account = models.IntegerField(null=True, blank=True)
    refund_bank = models.CharField(max_length=45, null=True, blank=True)
    account_holder = models.CharField(max_length=45, null=True, blank=True)
    facebook_id = models.CharField(max_length=45, null=True)
    naver_id = models.CharField(max_length=45, null=True)
    kakao_id = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'accounts'
