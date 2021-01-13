from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Product.views import CategoryDetailView

urlpatterns = [

    path('search/<slug:cat_slug>/', CategoryDetailView.as_view(),name='category_detail'),
]