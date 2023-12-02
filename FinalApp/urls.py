from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.BookingViewSet.as_view()),
    path('booking/<int:pk>', views.SingleBookingViewSet.as_view()),
    
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]