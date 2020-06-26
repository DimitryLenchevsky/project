from django.contrib import admin
from .models import Subscriber
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'email')
    search_fields = ('pk', 'name', 'email')

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)