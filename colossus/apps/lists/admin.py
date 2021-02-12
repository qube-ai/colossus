from django.contrib import admin
from colossus.apps.lists import models as m

admin.site.register(m.MailingList)
admin.site.register(m.SubscriberImport)
