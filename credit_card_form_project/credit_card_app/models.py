from django.db import models

class CreditCard(models.Model):
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)

    class Meta:
        app_label = 'credit_card_app'
