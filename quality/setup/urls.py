from django.urls import path
from .views import *

urlpatterns = [
    path('reg/',RegView.as_view(),name='reg'),
    path('predict/',predict_air_quality,name='h'),
]