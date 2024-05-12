from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



"""class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile_images/', default='media/profile_images/base/user.svg')"""







class Vacation(models.Model):
    class Types(models.TextChoices):
        PAID = 'PD', _('Paid')
        UNPAID = 'UD', _('Unpaid')
        DAY_OFF = 'DO', _('Day off')

    class Status(models.TextChoices):
        ON_GROUP_LEADER = 'GL', _('On group leader')
        ON_HEAD_DEPARTMENT = 'HD', _('On head department')
        ON_HR = 'HR', _('On HR')
        ON_SIGNING = 'SG', _('On signing')
        ON_READY = 'RD', _('On ready')
        APPROVED = 'AP', _('Approved')

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=Types.choices)
    start = models.DateField()
    end = models.DateField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.ON_GROUP_LEADER)
