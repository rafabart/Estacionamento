from django.contrib import admin
from .models import (
    Marca,
    Pessoa,
    Veiculo,
    Parametros,
    MovRotativo,
    Mensalista,
    MovMensalista
)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'checkin', 'checkout',
                    'valor_hora', 'horas_total', 'pago', 'total')


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total', 'teste')

    def teste(self, obj):
        return "Pode retornar qualquer coisa"


admin.site.register(Marca)
admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)
