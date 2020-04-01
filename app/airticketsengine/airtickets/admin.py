from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.forms import ValidationError

from datetime import datetime
from .models import *
from re import match

# Register your models here.

class CountryResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Country

class CityResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = City

class AirportResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Airport

    def check_phone(self, new_phone):
        pattern = r"^\+[0-9]+$"
        res = match(pattern, new_phone)
        if res is None:
            return False
        return True


    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for row in dataset:
            if self.check_phone(row[4]) == False:
                raise ValidationError('Incorrect data')


class AirlineResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Airline


    def check_appearanceYear(self, year):
        if year < 1909 or year > datetime.now().year:
            return False
        return True


    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for row in dataset:
            if self.check_appearanceYear(row[3]) == False:
                raise ValidationError('Incorrect data')



class FlightResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Flight


    def check_price(self, price):
        if price < 0:
            return False
        return True

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for row in dataset:
            if self.check_price(row[5]) == False:
                raise ValidationError('Incorrect data')


class RouteResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Route


    def check_route(self, airport_from, airport_to):
        
        if airport_from == airport_to:
            return False
        elif Airport.objects.get(id=airport_from).city == Airport.objects.get(id=airport_to).city:
            return False
        return True

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for row in dataset:
            if self.check_route(row[2], row[3]) == False:
                raise ValidationError('Incorrect data')

class AirplaneResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Airplane


    def check_capacity(self, capacity):
        if capacity <= 0:
            return False
        return True
    
    def check_numberRows(self, numberRows):
        if numberRows <= 0:
            return False
        return True


    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for row in dataset:
            if self.check_capacity(row[3]) == False or self.check_numberRows(row[4]) == False:
                raise ValidationError('Incorrect data')


class SeatResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Seat


    #def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #    for row in dataset:
    #        if self.check_route(row[2], row[3]) == False:
    #            raise ValidationError('Incorrect data')



class TicketResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('id',)
        model = Ticket




class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource



admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(Airplane)
admin.site.register(Route)
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Ticket)

