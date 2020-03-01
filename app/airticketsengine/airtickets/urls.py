from django.urls import path

from .views import *


urlpatterns = [

    path('airlines/', airlines_list, name='airlines_list_url'),
    path('airline/create/', AirlineCreate.as_view(), name='airline_create_url'),
    path('airline/<str:slug>/', AirlineDetail.as_view(), name='airline_detail_url'),
    path('airline/<str:slug>/update/', AirlineUpdate.as_view(), name='airline_update_url'),
    path('airline/<str:slug>/delete/', AirlineDelete.as_view(), name='airline_delete_url'),

    path('airports/', airports_list, name='airports_list_url'),
    path('airport/create/', AirportCreate.as_view(), name='airport_create_url'),
    path('airport/<str:slug>/', AirportDetail.as_view(), name='airport_detail_url'),
    path('airport/<str:slug>/update/', AirportUpdate.as_view(), name='airport_update_url'),
    path('airport/<str:slug>/delete/', AirportDelete.as_view(), name='airport_delete_url'),

    path('flights/', flights_list, name='flights_list_url'),
    path('flight/create/', FlightCreate.as_view(), name='flight_create_url'),
    path('flight/<str:slug>/', FlightDetail.as_view(), name='flight_detail_url'),
    path('flight/<str:slug>/update/', FlightUpdate.as_view(), name='flight_update_url'),
    path('flight/<str:slug>/delete/', FlightDelete.as_view(), name='flight_delete_url'),

    path('routes/', routes_list, name='routes_list_url'),
    path('route/create/', RouteCreate.as_view(), name='route_create_url'),
    path('route/<str:slug>/', RouteDetail.as_view(), name='route_detail_url'),
    path('route/<str:slug>/update/', RouteUpdate.as_view(), name='route_update_url'),
    path('route/<str:slug>/delete/', RouteDelete.as_view(), name='route_delete_url'),

    path('airplanes/', airplanes_list, name='airplanes_list_url'),
    path('airplane/create/', AirplaneCreate.as_view(), name='airplane_create_url'),
    path('airplane/<str:slug>/', AirplaneDetail.as_view(), name='airplane_detail_url'),
    path('airplane/<str:slug>/update/', AirplaneUpdate.as_view(), name='airplane_update_url'),
    path('airplane/<str:slug>/delete/', AirplaneDelete.as_view(), name='airplane_delete_url'),

    path('countries/', countries_list, name='countries_list_url'),
    path('country/create/', CountryCreate.as_view(), name='country_create_url'),
    path('country/<str:slug>/', CountryDetail.as_view(), name='country_detail_url'),
    path('country/<str:slug>/update/', CountryUpdate.as_view(), name='country_update_url'),
    path('country/<str:slug>/delete/', CountryDelete.as_view(), name='country_delete_url'),

    path('cities/', cities_list, name='cities_list_url'),
    path('city/create/', CityCreate.as_view(), name='city_create_url'),
    path('city/<str:slug>/', CityDetail.as_view(), name='city_detail_url'),
    path('city/<str:slug>/update/', CityUpdate.as_view(), name='city_update_url'),
    path('city/<str:slug>/delete/', CityDelete.as_view(), name='city_delete_url')

]