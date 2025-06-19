from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events_list, name='events'),        # إن لم يكن مضافًا
         # 🔵 هذا هو المطلوب
]
