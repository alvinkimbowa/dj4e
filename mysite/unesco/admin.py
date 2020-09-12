from django.contrib import admin
from unesco.models import Site, Iso, Category, State, Region

# Register your models here.
admin.site.register(Site)
admin.site.register(Iso)
admin.site.register(State)
admin.site.register(Region)