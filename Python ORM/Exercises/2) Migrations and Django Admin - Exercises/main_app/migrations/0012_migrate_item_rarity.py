# Generated by Django 5.0.4 on 2024-06-24 18:20

from django.db import migrations


def get_item_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    all_items = item_model.objects.all()

    for item_record in all_items:
        if item_record.price <= 10:
            item_record.rarity = 'Rare'
        elif 11 <= item_record.price <= 20:
            item_record.rarity = 'Very Rare'
        elif 21 <= item_record.price <= 30:
            item_record.rarity = 'Extremely Rare'
        else:
            item_record.rarity = 'Mega Rare'

    item_model.objects.bulk_update(all_items, ['rarity'])


def set_item_rarity_default(apps, schema_editor):
    item = apps.get_model('main_app', 'Item')

    for curr_item in item.objects.all():
        curr_item.rarity = 'No rarity'
        curr_item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(get_item_rarity, reverse_code=set_item_rarity_default),
    ]