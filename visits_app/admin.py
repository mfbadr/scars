from django.contrib import admin

from visits_app.models import Visit

class VisitAdmin(admin.ModelAdmin):
  readonly_fields = ('time', 'id' )

admin.site.register(Visit, VisitAdmin)
# Register your models here.
