from django.urls import path
from . import views

urlpatterns = [
    
      path('', views.index,name = 'index'),
      path('thank-you/', views.thankYou, name='thank_you'),

    
]
