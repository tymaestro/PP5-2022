from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Guide(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Tour(models.Model):
    level = models.ForeignKey(
        'Level', null=True, blank=True, on_delete=models.SET_NULL
        )
    guide = models.ForeignKey(
        'Guide', null=True, blank=True, on_delete=models.SET_NULL
        )
    tour_title = models.CharField(max_length=254)
    tour_distance = models.DecimalField(max_digits=5, decimal_places=2)
    tour_description = models.TextField()
    tour_time_length = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
        )
    tour_speed = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
        )
    tour_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name