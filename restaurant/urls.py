from django.contrib import admin
from rest_framework import routers
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('', views.index, name='menu'),
    path('', views.index, name='about'),
    path('', views.index, name='book'),
    path('', views.index, name='bookings'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]

urlpatterns += router.urls