from django.urls import path
from . import views

# these will be additional URL sub-addresses for later reference.  They can be changed!
urlpatterns = [
    path('', views.cars_list),
    path('<int:pk>', views.car_detail),
]