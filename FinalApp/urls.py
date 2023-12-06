from django.urls import path
from . import views
from django.urls import include

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('booking/', views.BookingViewSet.as_view()),
    path('booking/<int:pk>', views.SingleBookingViewSet.as_view()),
    
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
   
    path('message/', views.msg),
    
    path('api-token-auth/', obtain_auth_token),
  
    ]