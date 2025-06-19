from django.shortcuts import render


def home(request):
    events = [
        {'name': 'فعالية تقنية الرياض', 'description': 'عرض أحدث الابتكارات', 'price': 150},
        {'name': 'ملتقى الفعاليات الصيفية', 'description': 'فعاليات شبابية متنوعة', 'price': 90},
        {'name': 'معرض التصميم الإبداعي', 'description': 'أعمال فنية وتصميم داخلي', 'price': 100},
    ]
    return render(request, 'home.html', {
        'page_title': 'الفعاليات المتاحة',
        'page_message': 'استعرض الفعاليات وسجّل في ما يناسبك.',
        'events': events
    })
