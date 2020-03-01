from django.shortcuts import render
from django.views.generic import View


from .utils import *
from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin


def airlines_list(request):
    airlines = Airline.objects.all()
    return render(request, 'airtickets/airlines_list.html', context={'airlines': airlines})

class AirlineDetail(ObjectDetailMixin, View):
    model = Airline
    template = 'airtickets/airline_detail.html'

class AirlineCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Airline
    model_form = AirlineForm
    raise_exception = True

class AirlineUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Airline
    model_form = AirlineForm
    raise_exception = True

class AirlineDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Airline
    redirect_url = 'airlines_list_url'
    raise_exception = True




def airports_list(request):
    airports = Airport.objects.all()
    return render(request, 'airtickets/airports_list.html', context={'airports': airports})

class AirportDetail(ObjectDetailMixin, View):
    model = Airport
    template = 'airtickets/airport_detail.html'

class AirportCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Airport
    model_form = AirportForm
    raise_exception = True

class AirportUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Airport
    model_form = AirportForm
    raise_exception = True

class AirportDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Airport
    redirect_url = 'airports_list_url'
    raise_exception = True




def flights_list(request):
    flights = Flight.objects.all()
    return render(request, 'airtickets/flights_list.html', context={'flights': flights})

class FlightDetail(ObjectDetailMixin, View):
    model = Flight
    template = 'airtickets/flight_detail.html'

class FlightCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Flight
    model_form = FlightForm
    raise_exception = True

class FlightUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Flight
    model_form = FlightForm
    raise_exception = True

class FlightDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Flight
    redirect_url = 'flights_list_url'
    raise_exception = True




def routes_list(request):
    routes = Route.objects.all()
    return render(request, 'airtickets/routes_list.html', context={'routes': routes})

class RouteDetail(ObjectDetailMixin, View):
    model = Route
    template = 'airtickets/route_detail.html'

class RouteCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Route
    model_form = RouteForm
    raise_exception = True

class RouteUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Route
    model_form = RouteForm
    raise_exception = True

class RouteDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Route
    redirect_url = 'routes_list_url'
    raise_exception = True




def airplanes_list(request):
    airplanes = Airplane.objects.all()
    return render(request, 'airtickets/airplanes_list.html', context={'airplanes': airplanes})

class AirplaneDetail(ObjectDetailMixin, View):
    model = Airplane
    template = 'airtickets/airplane_detail.html'

class AirplaneCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Airplane
    model_form = AirplaneForm
    raise_exception = True

class AirplaneUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Airplane
    model_form = AirplaneForm
    raise_exception = True

class AirplaneDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Airplane
    redirect_url = 'airplanes_list_url'
    raise_exception = True




def countries_list(request):
    countries = Country.objects.all()
    return render(request, 'airtickets/countries_list.html', context={'countries': countries})

class CountryDetail(ObjectDetailMixin, View):
    model = Country
    template = 'airtickets/country_detail.html'

class CountryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Country
    model_form = CountryForm
    raise_exception = True

class CountryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Country
    model_form = CountryForm
    raise_exception = True

class CountryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Country
    redirect_url = 'countries_list_url'
    raise_exception = True



def cities_list(request):
    cities = City.objects.all()
    return render(request, 'airtickets/cities_list.html', context={'cities': cities})

class CityDetail(ObjectDetailMixin, View):
    model = City
    template = 'airtickets/city_detail.html'

class CityCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = City
    model_form = CityForm
    raise_exception = True

class CityUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = City
    model_form = CityForm
    raise_exception = True

class CityDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = City
    redirect_url = 'cities_list_url'
    raise_exception = True
