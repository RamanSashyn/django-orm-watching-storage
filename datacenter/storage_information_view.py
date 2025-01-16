from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.get_entered_at_formatted(),
            'duration': visit.format_duration(),
        }
        for visit in active_visits
    ]

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
