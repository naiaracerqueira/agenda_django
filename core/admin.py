from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') #campos que vao aparecer
    list_filter = ('usuario','data_evento',) #essa virgula tem que ficar no final

admin.site.register(Evento, EventoAdmin)

