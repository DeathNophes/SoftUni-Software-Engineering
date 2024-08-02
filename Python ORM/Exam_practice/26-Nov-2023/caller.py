import os

import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review

# Create queries within functions


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ''

    if search_name is not None and search_email is None:
        query = Q(full_name__icontains=search_name)
    elif search_name is None and search_email is not None:
        query = Q(email__icontains=search_email)
    else:
        query = (
            Q(full_name__icontains=search_name) &
            Q(email__icontains=search_email)
        )

    authors = Author.objects.filter(query).order_by('-full_name')
    result = []
    for a in authors:
        result.append(
            f"Author: {a.full_name}, "
            f"email: {a.email}, "
            f"status: {'Banned' if a.is_banned else 'Not Banned'}"
        )

    return '\n'.join(result)


def get_top_publisher():
    author = Author.objects\
        .get_authors_by_article_count()\
        .first()

    if not author or author.article_count == 0:
        return ''

    return (f"Top Author: {author.full_name} "
            f"with {author.article_count} published articles.")


def get_top_reviewer():
    reviewer = Author.objects\
        .annotate(reviews_count=Count('review_author'))\
        .filter(reviews_count__gt=0)\
        .order_by('-reviews_count', 'email')\
        .first()

    if not reviewer:
        return ''

    return (f"Top Reviewer: {reviewer.full_name} "
            f"with {reviewer.reviews_count} published reviews.")


def get_latest_article():
    article = Article.objects\
        .annotate(reviews_count=Count('review_article'), avg_rating=Avg('review_article__rating'))\
        .order_by('published_on').last()

    if not article:
        return ''

    authors = article.authors.order_by('full_name').values_list('full_name', flat=True)
    # We get them in a list

    reviews = article.reviews_count or 0
    avg_rating = article.avg_rating or 0.00
    # We need to handle the cases where it might return None or 0

    return (f"The latest article is: {article.title}. "
            f"Authors: {', '.join(authors)}. "
            f"Reviewed: {reviews} times. "
            f"Average Rating: {avg_rating:.2f}.")


def get_top_rated_article():
    top_article = Article.objects\
        .annotate(reviews_count=Count('review_article'), avg_rating=Avg('review_article__rating'))\
        .order_by('-avg_rating', 'title')\
        .first()

    if not Review.objects.all():
        return ''

    reviews = top_article.reviews_count or 0
    avg_rating = top_article.avg_rating or 0.00
    # We need to handle the cases where it might return None or 0

    return (f"The top-rated article is: {top_article.title}, "
            f"with an average rating of {avg_rating:.2f}, "
            f"reviewed {reviews} times.")


def ban_author(email=None):
    if email is None or not Author.objects.all():
        return "No authors banned."

    author = Author.objects\
        .annotate(reviews=Count('review_author'))\
        .filter(email=email)\
        .first()

    if not author:
        return "No authors banned."

    author.is_banned = True
    author.save()

    author.review_author.all().delete()

    return f"Author: {author.full_name} is banned! {author.reviews} reviews deleted."
