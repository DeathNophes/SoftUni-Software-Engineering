from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import CustomAuthorManager

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )

    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)

    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005),
        ]
    )

    website = models.URLField(null=True, blank=True)

    objects = CustomAuthorManager()


class Article(models.Model):
    CATEGORY_CHOICES = [
        ("Technology", "Technology"),
        ("Science", "Science"),
        ("Education", "Education"),
    ]

    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)]
    )

    content = models.TextField(
        validators=[MinLengthValidator(10)]
    )

    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default="Technology",
    )

    authors = models.ManyToManyField(
        to='Author',
        related_name='article_author'
    )

    published_on = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    content = models.TextField(
        validators=[MinLengthValidator(10)]
    )

    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ]
    )

    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='review_author'
    )

    article = models.ForeignKey(
        to='Article',
        on_delete=models.CASCADE,
        related_name='review_article'
    )

    published_on = models.DateTimeField(auto_now_add=True)