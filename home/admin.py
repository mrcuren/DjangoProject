from django.contrib import admin

from home.models import Setting, ContactFormMessage


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ["status"]


# Register your models here.

admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
