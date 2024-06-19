from datetime import date

from django.db import models

CITIES = [
    ('Sofia', 'Sofia'),
    ('Plovdiv', 'Plovdiv'),
    ('Varna', 'Varna'),
    ('Burgas', 'Burgas')
]


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    works_full_time = models.BooleanField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email_address}"


class Department(models.Model):
    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField("Employees count", default=1)
    location = models.CharField(max_length=20, null=True, choices=CITIES)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True, blank=True)
    duration_in_days = models.PositiveIntegerField(
        "Duration in Days", null=True, blank=True)
    estimated_hours = models.FloatField(
        "Estimated Hours", null=True, blank=True)
    start_date = models.DateField(
        "Start Date", default=date.today)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)
