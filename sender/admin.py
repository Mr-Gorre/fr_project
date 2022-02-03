from django.contrib import admin
from sender.models import Deliver, Client, Message
# Register your models here.


admin.site.register(Deliver)
admin.site.register(Client)
admin.site.register(Message)