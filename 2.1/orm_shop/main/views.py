from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Car, Sale, Client


def cars_list_view(request):
    # get a list of cars
    cars = Car.objects.all()
    template_name = './main/list.html'
    return render(request, template_name, {'cars': cars})  # Passing the list of cars to the context


def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)  # Obtaining a vehicle by ID, or if it doesn't exist, throw a 404 error
    template_name = './main/details.html'
    return render(request, template_name, {'car': car})  # Putting the car in context


def sales_by_car(request, car_id):
    # Получите авто и его продажи
    car = get_object_or_404(Car, id=car_id)  # Obtaining a vehicle by ID, or if it doesn't exist, throw a 404 error
    sales = Sale.objects.filter(car=car)  # Get all sales for this vehicle
    template_name = './main/sales.html'
    return render(request, template_name, {'car': car, 'sales': sales})  # Putting autos and sales into context
