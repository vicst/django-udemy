# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

#from graphos.sources.model import ModelDataSource
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart


def graph(request):
    data = [
        ['An', 'Vanzari', 'Cheltuieli'],
        [2001, 100, 1000],
        [2004, 1000, 300],
        [2005, 145, 302],
        [2009, 164, 1132]
    ]
    data_source = SimpleDataSource(data = data)
    chart = LineChart(data_source)
    context = {'chart': chart}
    return render(request, "graf.html", context)

class RestaurantListView(ListView):
    #template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        print slug
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__icontains = slug) |
                Q(category__iexact = slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        print (self.kwargs)
        context = super(RestaurantListView,self).get_context_data(**kwargs)
        print context
        return context

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.filter(category = "Bun")
    #print queryset

    #comentat pt ca face acelasi lucru ca get_object
    # def get_context_data(self, **kwargs):
    #     print (self.kwargs)
    #     context = super(RestaurantDetailView,self).get_context_data(**kwargs)
    #     print context
    #     return context

    #comentat pt ca filtrez obiectele in functie de slug in restaurentlication_detail.html
    # def get_object(self, **kwargs):
    #     rest_id = self.kwargs.get("rest_id")
    #     obj = get_object_or_404(RestaurantLocation, pk = rest_id)
    #     return obj











