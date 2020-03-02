from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time



def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('country_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('country_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('country_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('country_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    slug = models.CharField(max_length=50, unique=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    def get_absolute_url(self):
        return reverse('city_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('city_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('city_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('city_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')
    address = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('airport_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('airport_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('airport_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('airport_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Airline(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='airlines')
    appearanceYear = models.IntegerField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('airline_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('airline_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('airline_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('airline_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airplanes')
    capacity = models.IntegerField()
    numberRows = models.IntegerField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('airplane_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('airplane_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('airplane_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('airplane_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    airportFrom = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='routesFrom')
    airportTo = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='routesTo')
    slug = models.SlugField(max_length=100, unique=True, blank=True)


    def get_absolute_url(self):
        return reverse('route_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('route_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('route_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('route_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}-{}'.format(self.airportFrom, self.airportTo)


class Flight(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='flights')
    departureDateTime = models.DateTimeField()
    price = models.FloatField()
    duration = models.TimeField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('flight_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('flight_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('flight_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('flight_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}:{}'.format(self.route, self.departureDateTime)


class Seat(models.Model):
    name = models.CharField(max_length=5, db_index=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='seats')
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('seat_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('seat_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('seat_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('seat_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.TextField(max_length=100, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets')
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='tickets')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('ticket_detail_url', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('ticket_create_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('ticket_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('ticket_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(str(self.person.id) + '-' + str(self.seat.name))
        super().save(*args, **kwargs)
        self.name = str(self.id)
        super().save(*args, **kwargs)


    def __str__(self):
        return '{}:{}'.format(self.person, self.seat)

