from django.shortcuts import render
from django.http import HttpResponse

from visits_app.models import Visit

from user_agents import parse

import sys

def home(request):
  values = request.META.items()
  values.sort()
  html = []
  for k, v in values:
    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))

  ua_string = request.META.get('HTTP_USER_AGENT')
  user_agent = parse(ua_string)

  print 'USER-AGENT'
  print '%s --- %s ' % ('user_agent.browser', user_agent.browser.family)
  print '%s --- %s ' % ('user_agent.os', user_agent.os.family)
  print '%s --- %s ' % ('user_agent.device', user_agent.os.family)
  print '%s --- %s ' % ('str(user_agent)', str(user_agent))
  print '%s --- %s ' % ('user_agent.is_mobile', user_agent.is_mobile)
  print '%s --- %s ' % ('user_agent.is_tablet', user_agent.is_tablet)
  print '%s --- %s ' % ('user_agent.is_touch_capable', user_agent.is_touch_capable)
  print '%s --- %s ' % ('user_agent.is_pc', user_agent.is_pc)
  print '%s --- %s ' % ('user_agent.is_bot', user_agent.is_bot)

  visit = Visit(
      browser = user_agent.browser.family,
      os = user_agent.os.family,
      device = user_agent.device.family,
      is_mobile = user_agent.is_mobile,
      is_tablet = user_agent.is_tablet,
      is_pc = user_agent.is_pc,
      is_bot = user_agent.is_bot,
      )

  visit.save()

  return HttpResponse('<table>%s</table>' % '\n'.join(html))

# Create your views here.
