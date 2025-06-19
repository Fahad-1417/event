from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_list),  # هذا يعرض الفعاليات عند الضغط على /events/
]
