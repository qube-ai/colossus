from django.contrib import admin
from colossus.apps.subscribers import models as m

admin.site.register(m.Tag)
admin.site.register(m.Domain)
admin.site.register(m.Subscriber)
# admin.site.register(m.SubscriberManager)
admin.site.register(m.Activity)
admin.site.register(m.SubscriptionFormTemplate)
