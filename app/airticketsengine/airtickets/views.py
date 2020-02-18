from django.shortcuts import render
from django.views.generic import View


from .utils import *
from .models import *
from .forms import *


def airlines_list(request):
    airlines = Airline.objects.all()
    return render(request, 'airtickets/index.html', context={'airlines': airlines})

class AirlineDetail(ObjectDetailMixin, View):
    model = Airline
    template = 'airtickets/airline_detail.html'

class AirlineCreate(ObjectCreateMixin, View):
    model_form = AirlineForm
    template = 'airtickets/airline_create_form.html'

class AirlineUpdate(ObjectUpdateMixin, View):
    model = Airline
    model_form = AirlineForm
    template = 'airtickets/airline_update_form.html'

class AirlineDelete(ObjectDeleteMixin, View):
    model = Airline
    template = 'airtickets/airline_delete_form.html'
    redirect_url = 'airlines_list_url'




def airports_list(request):
    airports = Airport.objects.all()
    return render(request, 'airtickets/airports_list.html', context={'airports': airports})

class AirportDetail(ObjectDetailMixin, View):
    model = Airport
    template = 'airtickets/airport_detail.html'



def flights_list(request):
    flights = Flight.objects.all()
    return render(request, 'airtickets/flights_list.html', context={'flights': flights})

class FlightDetail(ObjectDetailMixin, View):
    model = Flight
    template = 'airtickets/flight_detail.html'




def routes_list(request):
    routes = Route.objects.all()
    return render(request, 'airtickets/routes_list.html', context={'routes': routes})

class RouteDetail(ObjectDetailMixin, View):
    model = Route
    template = 'airtickets/route_detail.html'



def airplanes_list(request):
    airplanes = Airplane.objects.all()
    return render(request, 'airtickets/airplanes_list.html', context={'airplanes': airplanes})

class AirplaneDetail(ObjectDetailMixin, View):
    model = Airplane
    template = 'airtickets/airplane_detail.html'



def countries_list(request):
    countries = Country.objects.all()
    return render(request, 'airtickets/countries_list.html', context={'countries': countries})

class CountryDetail(ObjectDetailMixin, View):
    model = Country
    template = 'airtickets/country_detail.html'



def cities_list(request):
    cities = City.objects.all()
    return render(request, 'airtickets/cities_list.html', context={'cities': cities})

class CityDetail(ObjectDetailMixin, View):
    model = City
    template = 'airtickets/city_detail.html'
