from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


# Create your models here.
def validate_no_digits(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Поле не должно содержать цифры.')


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')


class Product(models.Model):
    name = models.CharField('Название:', max_length=30)
    small_text = models.TextField('Краткое описание:', max_length=50)
    category = models.CharField('Категория:', max_length=50, validators=[validate_no_digits])
    full_text = models.TextField('Развернутое описание:', max_length=2000)
    count_of = models.IntegerField('Количество товаров на складе:')
    price = models.FloatField('Цена:', max_length=10)
    images = models.ForeignKey(ProductImage, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField('Комментарий:', max_length=200)
    date = models.DateTimeField('Дата публикации:')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_comment')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comment')


class Rating(models.Model):
    mark = models.IntegerField('Оценка:')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_rating')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rating')


class RegistrationModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration')
    code_word = models.TextField('Кодовое слово:', max_length=20, blank=True)
    role = models.CharField('Роль:', max_length=20, blank=True, default='user')
    city = models.CharField('Введите ваш город:', max_length=100, blank=True)
