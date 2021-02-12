from django.contrib import admin
from colossus.apps.core import models as m


admin.site.register(m.Token)
admin.site.register(m.Option)
admin.site.register(m.Country)
admin.site.register(m.City)
