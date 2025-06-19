from django.shortcuts import render

def events_list(request):
    events = [
        {'name': 'فعالية رياضية', 'description': 'سباق جري في الهواء الطلق', 'price': 50},
        {'name': 'مؤتمر تقني', 'description': 'أحدث تقنيات الذكاء الاصطناعي', 'price': 150},
        {'name': 'ورشة عمل', 'description': 'تطوير مهارات القيادة', 'price': 75},
        {'name': 'دورة تصوير', 'description': 'أساسيات التصوير الفوتوغرافي', 'price': 120},
        {'name': 'فعالية طهي', 'description': 'مسابقة أفضل طبق شعبي', 'price': 90},
        {'name': 'ندوة ثقافية', 'description': 'قضايا الفكر العربي الحديث', 'price': 45},
        {'name': 'مهرجان فني', 'description': 'معرض لوحات ورسومات حية', 'price': 80},
        {'name': 'فعالية صحية', 'description': 'مشي جماعي وتوعية رياضية', 'price': 60},
        {'name': 'رحلة استكشافية', 'description': 'تجربة مغامرات صحراوية', 'price': 180},
    ]
    return render(request, 'app2_events/events.html', {
        'events': events,
        'page_title': 'الفعاليات المتوفرة',
        'page_message': 'استعرض فعالياتنا الحالية وسجل اهتمامك'
    })
