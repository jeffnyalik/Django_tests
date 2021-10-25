from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):

    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'published')
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    fullName = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    createdBy = models.ForeignKey(User, on_delete=models.PROTECT, related_name='createdBy', default=1)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Draft')

    objects = models.Manager()

    class Meta:
        verbose_name ='Customer'
        verbose_name_plural ='Customers'

    def __str__(self):
        return "{} {}".format(self.name, self.lastName)

