from django.db import models


class Account(models.Model):
<<<<<<< HEAD
    social_platform  = models.ForeignKey(SocialLog, on_delete = models.CASCADE, null=True)
=======
    social_id        = models.CharField(max_length=50, null=True)
>>>>>>> 5801240c9d54601e005ce713d08d425669d0691d
    username         = models.CharField(max_length=50, null=True)
    email            = models.EmailField(max_length=50, unique=True, null=True)
    password         = models.CharField(max_length=500)
    agree_location   = models.NullBooleanField()
    agree_promotion  = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    profile          = models.URLField(max_length=500, null=True, blank=True)
<<<<<<< HEAD
    phone            = models.CharField(max_length=50, null=True, blank=True)
=======
    phone            = models.IntegerField(null=True, blank=True, default=31874599)
>>>>>>> 5801240c9d54601e005ce713d08d425669d0691d

    class Meta:
        db_table = 'accounts'

class MarketingAgree(models.Model):
    email_receive = models.BooleanField(default=True)
    sms_receive   = models.BooleanField(default=True)
    app_receive   = models.BooleanField(default=True)

    class Meta:
        db_table = 'marketingagree'

class SnsConnection(models.Model):
    kakao_connection    = models.BooleanField(default=False)
    naver_connection    = models.BooleanField(default=False)
    facebook_connection = models.BooleanField(default=False)

    class Meta:
        db_table = 'snsconnection'

class RefundAccount(models.Model):
    refund_account  = models.IntegerField(null=True, blank=True)
    refund_bank     = models.CharField(max_length=45, null=True, blank=True)
    account_holder  = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'refundaccount'