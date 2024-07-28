import os
from decimal import Decimal

import django
from django.db.models import Q, Count, F, Case, When, Value

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order

# Create queries within functions


def get_profiles(search_string: str or None):
    if search_string is None:
        return ''

    query = (
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    )

    profiles = Profile.objects.filter(query).order_by('full_name')

    if not profiles.exists():
        return ''

    result = []
    for p in profiles:
        result.append(
            f"Profile: {p.full_name}, "
            f"email: {p.email}, "
            f"phone number: {p.phone_number}, "
            f"orders: {p.order_profile.count()}"
        )

    return '\n'.join(result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles.exists():
        return ''

    result = []
    for p in profiles:
        result.append(
            f"Profile: {p.full_name}, orders: {p.order_profile.count()}"
        )

    return '\n'.join(result)


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()

    if not last_order or not last_order.products:
        return ''

    products = last_order.products.order_by('name').values_list('name', flat=True)

    return f"Last sold products: {', '.join(products)}"


def get_top_products():
    top_products = Product.objects\
        .annotate(orders_count=Count('order_product'))\
        .filter(orders_count__gt=0)\
        .order_by('-orders_count', 'name')[:5]

    if not top_products.exists():
        return ''

    product_lines = [f"{p.name}, sold {p.orders_count} times" for p in top_products]

    return f"Top products:\n" + "\n".join(product_lines)


def apply_discounts():
    orders = Order.objects\
        .annotate(products_count=Count('products'))\
        .filter(products_count__gt=2, is_completed=False)

    orders.update(total_price=F('total_price') * 0.9)

    return f"Discount applied to {len(orders)} orders."


def complete_order():
    order = Order.objects\
        .filter(is_completed=False)\
        .order_by('creation_date')\
        .first()

    if not order:
        return ''

    order.is_completed = True
    order.save()
    # We can't use order.update() because update in not an attribute of order

    order.products.update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),
            default=F('is_available'),
            # output_field=BooleanField()
        )
    )

    # products = order.products.all()
    # products.update(in_stock=F('in_stock') - 1)
    # for p in products:
    #     if p.in_stock == 0:
    #         p.is_available = False
    #         p.save()

    return "Order has been completed!"
