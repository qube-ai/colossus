from django.contrib import admin
from colossus.apps.notifications import models as m

admin.site.register(m.Notification)
