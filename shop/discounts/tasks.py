from datetime import datetime

from celery import shared_task
from .models import Discount


@shared_task
def remove_discounts():
    for disc in Discount.objects.filter(end__date__lte=datetime.now()):
        disc.delete()

