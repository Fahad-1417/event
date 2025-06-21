from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('app1_accounts.urls')),  # هذا يجعل الصفحة الرئيسية تعمل ←
    path('admin/', admin.site.urls),
    path('accounts/', include('app1_accounts.urls')),
    path('events/', include('app2_events.urls')),
    path('dashboard/', include('app3_dashboard.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='app1_accounts/login.html'), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
