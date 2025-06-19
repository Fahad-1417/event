from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),  # ← الآن / يعرض home.html
    path('profile/', views.account_home, name='account_home'),
]
