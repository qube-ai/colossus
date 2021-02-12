from django.contrib import admin
from colossus.apps.campaigns import models as m

admin.site.register(m.Campaign)
admin.site.register(m.Email)
admin.site.register(m.Link)
