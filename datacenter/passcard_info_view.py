from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    
    this_passcard_visits = []
    visit_details = {}
    for i in passcard_visits:
      duration = get_duration(i)
      is_strange = is_visit_long(i, minutes=60)
      visit_details = {
      "entered_at": i.entered_at,
      "duration": duration,
      'is_strange': is_strange
      }
      this_passcard_visits.append(visit_details)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
