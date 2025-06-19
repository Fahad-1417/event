from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app1_accounts.urls')),  # ← هذا يجعل الصفحة الرئيسية تعمل
    path('admin/', admin.site.urls),
    path('accounts/', include('app1_accounts.urls')),
    path('events/', include('app2_events.urls')),
    path('dashboard/', include('app3_dashboard.urls')),
]
