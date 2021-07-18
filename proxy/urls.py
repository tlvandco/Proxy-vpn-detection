from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('results/',views.base,name = 'base'),
    path('output/',views.output,name='output')
]