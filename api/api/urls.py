"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from attractions.viewsets import AttractionViewsets
from comment_reviews.viewsets import CommentViewsets, ReviewViewsets
from tourist_spots.viewsets import TouristSpotViewsets

router = routers.DefaultRouter()
router.register(r'attractions', AttractionViewsets)
router.register(r'comments', CommentViewsets)
router.register(r'reviews', ReviewViewsets)
router.register(r'touristspots', TouristSpotViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
