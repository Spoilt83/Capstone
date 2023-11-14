from django.urls import path
from . import views

urlpatterns = [
    # path('ratings', views.ratings),
    path('', views.index, name='index')
]