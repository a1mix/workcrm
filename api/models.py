from django.db import models

from jwt_auth.models import CrmUser


class Profile(models.Model):
    user = models.OneToOneField(CrmUser, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    pass_seria = models.CharField(max_length=55)
    pass_num = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.user.username

class House(models.Model):
    price = models.FloatField()
    one_bed = models.IntegerField()
    name = models.CharField(max_length=55)
    two_bed = models.IntegerField()
    description = models.CharField(max_length=255)
    is_prepayment = models.BooleanField(default=False)
    min_prepayment = models.FloatField(default=0)

class House_Photo(models.Model):
    url = models.CharField()
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)

class Order_Status(models.Model):
    name = models.CharField(max_length=55)

class Order(models.Model):
    profile_id = models.ManyToManyField(Profile)
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(null=True, blank=True)
    departure_time = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(Order_Status, on_delete=models.CASCADE)
    admin_comment = models.CharField(null=True, blank=True)
    total_coast = models.FloatField()
    prepayment = models.FloatField()