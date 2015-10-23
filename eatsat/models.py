from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    estimated_wait_time = models.IntegerField()
    def __str__(self):
        return self.name
class Account(models.Model):
    account_id = models.PositiveIntegerField()
    last_name = models.CharField(max_length=200)
    payment_info = models.CharField(max_length=200)
    def __str__(self):
        return str(self.account_id)

class Eatsat(models.Model):
    account = ForeignKey(Account)
    restaurant = ForeignKey(Restaurant)
    party_size = models.PositiveIntegerField()
    wait_time = models.PositiveIntegerField(null=True, blank=True)
    meal_time = models.DateTimeField(null=True, blank=True
)
    def __str__(self):
        return str(self.account.account_id) + " " + self.restaurant.name
