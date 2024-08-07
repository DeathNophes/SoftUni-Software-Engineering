from django.db import models
from django.db.models import Count


class ProfileCustomManager(models.Manager):
    def get_regular_customers(self):
        return self.annotate(orders_count=Count('order_profile'))\
            .filter(orders_count__gt=2).order_by('-orders_count')