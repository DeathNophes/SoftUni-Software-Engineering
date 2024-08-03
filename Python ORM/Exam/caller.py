import os
from datetime import date, datetime

import django
from django.db.models import Q, Count, Sum, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission

# Create queries within functions


def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)

    astronauts = Astronaut.objects.filter(query).order_by('name')

    if not astronauts:
        return ''

    result = []
    for a in astronauts:
        result.append(
            f"Astronaut: {a.name}, "
            f"phone number: {a.phone_number}, "
            f"status: {'Active' if a.is_active else 'Inactive'}"
        )

    return '\n'.join(result)


def get_top_astronaut():
    if not Astronaut.objects.all() or not Mission.objects.all():
        return "No data."

    astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    return (f"Top Astronaut: {astronaut.name} "
            f"with {astronaut.missions_count} missions.")


def get_top_commander():
    if not Astronaut.objects.all() or not Mission.objects.all():
        return 'No data.'

    commander = Astronaut.objects\
        .annotate(commanded_missions=Count('mission_commander'))\
        .filter(commanded_missions__gt=0)\
        .order_by('-commanded_missions', 'phone_number')\
        .first()

    if not commander:
        return 'No data.'

    return (f"Top Commander: {commander.name} "
            f"with {commander.commanded_missions} commanded missions.")


def get_last_completed_mission():
    if not Mission.objects.filter(status='Completed').all():
        return "No data."

    mission = Mission.objects\
        .prefetch_related('astronauts')\
        .annotate(spacewalks_count=Sum('astronauts__spacewalks'))\
        .filter(status="Completed")\
        .order_by('-launch_date')\
        .first()

    astronauts = mission.astronauts.order_by('name').values_list('name', flat=True)
    astronauts_list = ', '.join(astronauts)

    commander = mission.commander.name if mission.commander else 'TBA'

    return (f"The last completed mission is: {mission.name}. "
            f"Commander: {commander}. "
            f"Astronauts: {astronauts_list}. "
            f"Spacecraft: {mission.spacecraft.name}. "
            f"Total spacewalks: {mission.spacewalks_count}.")


def get_most_used_spacecraft():
    if not Mission.objects.all():
        return 'No data.'

    spacecraft = Spacecraft.objects\
        .annotate(missions=Count('mission_spacecraft'))\
        .order_by('-missions', 'name')\
        .first()

    missions = Mission.objects\
        .filter(spacecraft=spacecraft)\
        .all()

    astronauts = set()
    for m in missions:
        for a in m.astronauts.all():
            astronauts.add(a.name)

    return (f"The most used spacecraft is: {spacecraft.name}, "
            f"manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.missions} missions, "
            f"astronauts on missions: {len(astronauts)}.")


def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects\
        .filter(mission_spacecraft__status="Planned", weight__gte=200.0)\
        .distinct()

    affected_spacecrafts = spacecrafts.count()

    if affected_spacecrafts == 0:
        return "No changes in weight."

    spacecrafts.update(weight=F('weight') - 200.0)

    avg_weight = Spacecraft.objects.aggregate(Avg('weight'))['weight__avg']

    return (f"The weight of {affected_spacecrafts} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")
