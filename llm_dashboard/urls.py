from django.urls import path
from . import views

urlpatterns = [
    path('', views.llm_dashboard)
]
