from django.contrib import admin

from news.models import Contact, New, Advertise


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    pass