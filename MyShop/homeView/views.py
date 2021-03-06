from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.db.models import Sum
from Order.models import OrderItem
from Product.models import Category, Product, Brand
from homeView.models import SlideShow


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = SlideShow.objects.all()
        context['categories'] = Category.objects.all()
        context['productsWomen'] = Product.objects.filter(category__name__contains='ladies')
        context['productsMen'] = Product.objects.filter(category__name__contains='men')
        context['brands'] = Brand.objects.all()
        total_items = OrderItem.objects.aggregate(Sum("count"))
        context['total_items'] = total_items
        return context
