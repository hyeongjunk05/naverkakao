from django.db import models


class SocialLog(models.Model):
    social = models.CharField(max_length = 50)

    class Meta:
        db_table = 'social_platform'

class Account(models.Model):
    social_platform = models.ForeignKey(SocialLog, on_delete = models.CASCADE, null=True)
    sns_id = models.IntegerField(null=True)
    username = models.CharField(max_length=50, null=True)
    # 여기서 unique = True 하면 이메일의 고유성 확립되나 확인하기
    email = models.EmailField(max_length=50, unique=True, null=True)
    password = models.CharField(max_length=500)
    agree_location = models.NullBooleanField()
    agree_promotion = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.URLField(max_length=500, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    refund_account = models.IntegerField(null=True, blank=True)
    refund_bank = models.CharField(max_length=45, null=True, blank=True)
    account_holder = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'accounts'
