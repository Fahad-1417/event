from django.shortcuts import render
from .models import Event  # تأكد من استيراد النموذج

def events_list(request):
    events = Event.objects.all()
    return render(request, 'app2_events/events.html', {
        'events': events,
        'page_title': 'الفعاليات المتوفرة',
        'page_message': 'استعرض فعالياتنا الحالية وسجل اهتمامك'
    })
