from django.urls import path, include
from rest_framework.routers import DefaultRouter

from images import views

image_router = DefaultRouter(trailing_slash=False)
image_router.register('images', views.ImageView, basename='images')

urlpatterns = [
    path('', include(image_router.urls))
]
