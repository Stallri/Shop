from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime


class Discount(models.Model):
    percentRegex = RegexValidator(regex=r'^[1-9][0-9]?$|^99$')

    percent = models.PositiveIntegerField(validators=[percentRegex])
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.percent}% скидка с ({self.start.strftime("%H:%M %d-%m-%Y")})' \
               f' до ({self.end.strftime("%H:%M %d-%m-%Y")})'

    class Meta:
        ordering = ('-end',)
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
