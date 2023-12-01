from django.urls import path
from .views import bookingview
from . import views

urlpatterns = [
    path('booking', bookingview.as_view()),
    
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]