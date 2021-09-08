from datacenter.models import Visit
from datacenter.models import get_duration
from django.shortcuts import render


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    visit_details = {}
    for i in active_visits:
      duration = get_duration(i)
      visit_details = {
      "who_entered": i.passcard,
      "entered_at": i.entered_at,
      "duration": duration
      }
      non_closed_visits.append(visit_details)
    
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
