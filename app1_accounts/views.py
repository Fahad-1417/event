from django.shortcuts import render



def home(request):

    events = [
        {'name': 'دورة التعلم الآلي', 'description': 'مقدمة في الذكاء الاصطناعي', 'price': 120},
        {'name': 'ملتقى ريادة الأعمال', 'description': 'جلسات تحفيزية لرواد الأعمال', 'price': 80},
    ]
    return render(request, 'home.html', {
        'page_title': 'حسابك والفعاليات المقترحة',
        'page_message': 'مرحبًا بك! إليك بعض الفعاليات المقترحة لحسابك.',
        'events': events
    })
