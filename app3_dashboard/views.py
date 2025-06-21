from django.shortcuts import render


def landing_page(request):
    return render(request, 'home.html')



def home(request):
    events = [
        {'name': 'فعالية المسؤولين', 'description': 'اجتماع خاص بإدارة الأنظمة', 'price': 0},
        {'name': 'تحليل الأداء السنوي', 'description': 'عرض تقارير التسجيل والمشاركات', 'price': 0},
    ]
    return render(request, 'home.html', {
        'page_title': 'لوحة التحكم',
        'page_message': 'مرحبا بالمشرف، هذه أبرز الفعاليات الخاضعة للإدارة.',
        'events': events
    })
