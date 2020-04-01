from django.views.generic import View


from .utils import *
from .models import *
from .forms import *

from django.views.generic import CreateView, DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db.models import Count

from django.http import HttpResponse
from .admin import *
from tablib import Dataset

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



def import_countries(request):
    if request.method == 'POST':
        countries_resource = CountryResource()
        dataset = Dataset()
        new_countries = request.FILES['myfile']

        imported_data = dataset.load(new_countries.read())
        result = countries_resource.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            countries_resource.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})


    return render(request, 'airtickets/import.html', context={'msg': ''})

def import_cities(request):
    if request.method == 'POST':
        cities_resource = CityResource()
        dataset = Dataset()
        new_cities = request.FILES['myfile']

        imported_data = dataset.load(new_cities.read())
        result = cities_resource.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            cities_resource.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})


def import_airports(request):
    if request.method == 'POST':
        res = AirportResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = res.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            res.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})

def import_airlines(request):
    if request.method == 'POST':
        res = AirlineResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = res.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            res.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})

def import_flights(request):
    if request.method == 'POST':
        res = FlightResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = res.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            res.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})

def import_routes(request):
    if request.method == 'POST':
        res = RouteResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = res.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            res.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})

def import_airplanes(request):
    if request.method == 'POST':
        res = AirplaneResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = res.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            res.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})

def import_seats(request):
    if request.method == 'POST':
        res = SeatResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = res.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            res.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})

def import_tickets(request):
    if request.method == 'POST':
        res = TicketResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = res.import_data(dataset, dry_run=True)

        if not result.has_errors() and not result.has_validation_errors():
            res.import_data(dataset, dry_run=False)
            return render(request, 'airtickets/import.html', context={'msg': 'Import is success'})
        else:
            return render(request, 'airtickets/import.html', context={'msg': 'Incorrect data, try again'})

    return render(request, 'airtickets/import.html', context={'msg': ''})





def export_countries(request):
    res = CountryResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="countries.xls"'
    return response

def export_cities(request):
    res = CityResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="cities.xls"'
    return response

def export_airports(request):
    res = AirportResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="airports.xls"'
    return response

def export_airlines(request):
    res = AirlineResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="airlines.xls"'
    return response

def export_flights(request):
    res = FlightResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="flights.xls"'
    return response

def export_routes(request):
    res = RouteResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="routes.xls"'
    return response

def export_airplanes(request):
    res = AirplaneResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="airplanes.xls"'
    return response

def export_seats(request):
    res = SeatResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="seats.xls"'
    return response

def export_tickets(request):
    res = TicketResource()
    dataset = res.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tickets.xls"'
    return response





def main_page(request):
    res = Ticket.objects.values('flight__route__airportTo__city__country__name').annotate(total=Count('id'))
    data = [ [row['flight__route__airportTo__city__country__name'], row['total']] for row in res ]
    
    res2 = Ticket.objects.values('flight__airplane__airline__name').annotate(total=Count('id'))
    data2 = [ [row['flight__airplane__airline__name'], row['total']] for row in res2 ]
    
    return render(request, 'airtickets/main_page.html', context={'values1': data, 'values2': data2})



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


def seats_list(request):
    seats = Seat.objects.all()
    return render(request, 'airtickets/seats_list.html', context={'seats': seats})

class SeatDetail(ObjectDetailMixin, View):
    model = Seat
    template = 'airtickets/seat_detail.html'

class SeatCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Seat
    model_form = SeatForm
    raise_exception = True

class SeatUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Seat
    model_form = SeatForm
    raise_exception = True

class SeatDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Seat
    redirect_url = 'seats_list_url'
    raise_exception = True



def tickets_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'airtickets/tickets_list.html', context={'tickets': tickets})

class TicketDetail(ObjectDetailMixin, View):
    model = Ticket
    template = 'airtickets/ticket_detail.html'

class TicketCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Ticket
    model_form = TicketForm
    raise_exception = True

class TicketUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Ticket
    model_form = TicketForm
    raise_exception = True

class TicketDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Ticket
    redirect_url = 'tickets_list_url'
    raise_exception = True







def users_list(request):
    users = User.objects.all()
    return render(request, 'airtickets/users_list.html', context={'users': users})

class RegisterUserView(CreateView):
    model = User
    template_name = 'airtickets/register_form.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('airlines_list_url')
    success_msg = 'User was created successful'

class DetailUserView(DetailView):

    model = User
    template_name = 'airtickets/user_detail.html'

    def get(self, request, id):
        user = get_object_or_404(self.model, id=id)
        return render(request, self.template_name, context={'user': user, 'admin_object': user, 'detail': True})



def signup(request):
    if request.user.is_authenticated:
        return redirect(main_page)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(main_page)
    else:
        form = UserCreationForm()
    return render(request, 'airtickets/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(main_page)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(main_page)
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(main_page)
                else:
                    return render(request, 'airtickets/login.html', context={'form': form, 'mm': 'Disabled account'})
            else:
                return render(request, 'airtickets/login.html', context={'form': form, 'mm': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'airtickets/login.html', {'form': form})