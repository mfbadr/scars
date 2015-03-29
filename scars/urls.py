from django.conf.urls import include, url, patterns
from django.contrib import admin

from visits_app import views

urlpatterns = [
    # Examples:
    url(r'^$', 'visits_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
