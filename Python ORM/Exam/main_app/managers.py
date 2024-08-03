from django.db import models


class CustomAstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return self.annotate(
            missions_count=models.Count('mission_astronaut')
        ).order_by(
            '-missions_count',
            'phone_number'
        )