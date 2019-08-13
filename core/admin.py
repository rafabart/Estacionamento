from django.contrib import admin
from .models import (
    Marca,
    Pessoa,
    Veiculo,
    Parametros,
    MovRotativo,
    Mensalista
)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'checkin', 'checkout',
                    'valor_hora', 'horas_total', 'pago', 'total')

    def veiculo(self, obj):
        return obj.veiculo


admin.site.register(Marca)
admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovRotativo, MovRotativoAdmin)
