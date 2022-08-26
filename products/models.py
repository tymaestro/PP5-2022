from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Guide(models.Model):
    name = models.CharField(max_length=254)
    certificates = models.CharField(max_length=254)
    description = models.TextField()
    experience = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    nationality = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    location = models.CharField(max_length=254, null=True, blank=True)
    meeting_time = models.CharField(max_length=254, null=True, blank=True)
    scheduled_day = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.location


class Tour(models.Model):
    level = models.ForeignKey(
        'Level', null=True, blank=True, on_delete=models.SET_NULL
        )
    guide = models.ForeignKey(
        'Guide', null=True, blank=True, on_delete=models.SET_NULL
        )
    schedule = models.ForeignKey(
        'Schedule', null=True, blank=True, on_delete=models.SET_NULL
        )
    tour_title = models.CharField(max_length=254)
    tour_distance = models.PositiveSmallIntegerField()
    tour_description = models.TextField()
    tour_time_length = models.PositiveSmallIntegerField(
        null=True, blank=True
        )
    tour_speed = models.PositiveSmallIntegerField(
        null=True, blank=True
        )
    tour_price = models.DecimalField(max_digits=6, decimal_places=2)
    tour_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.tour_title
