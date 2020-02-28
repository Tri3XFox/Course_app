from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    imgpath = models.CharField(max_length=64)


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.CharField(max_length=64)


class Branch(models.Model):
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')


class Contact(models.Model):
    CONTACT_TYPES = (
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL')
    )
    type = models.IntegerField(choices=CONTACT_TYPES, max_length=10)
    value = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
