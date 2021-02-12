from django.contrib import admin
from colossus.apps.accounts import models as m

admin.site.register(m.User)
