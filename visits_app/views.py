from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse


from visits_app.models import Visit

from user_agents import parse

import sys

def scars(request, pk):


  return render(request, 'visits_app/scars.html', {})

def home(request):

  if request.is_ajax():
    current_scar = request.GET['id']
    last = int(current_scar) + 1
    visits = Visit.objects.filter(id__lte = last).order_by('time')
    visits = visits.values()
    visits_dict = {}
    for x in range(0, last - 1):
      visits_dict[str(x + 1)] = visits[x]

    #print visits_dict
    return JsonResponse(visits_dict)

  ua_string = request.META.get('HTTP_USER_AGENT')
  user_agent = parse(ua_string)

  visit = Visit.objects.create(
      browser = user_agent.browser.family,
      browser_version = user_agent.browser.version_string,
      os = user_agent.os.family,
      os_version = user_agent.os.version_string,
      device = user_agent.device.family,
      is_mobile = user_agent.is_mobile,
      is_tablet = user_agent.is_tablet,
      is_pc = user_agent.is_pc,
      is_bot = user_agent.is_bot,
      summary = str(user_agent),
      )

  pk = str(visit.id)

  return HttpResponseRedirect('/' + pk)

# Create your views here.
