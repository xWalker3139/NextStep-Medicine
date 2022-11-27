from django.contrib import admin
from .models import Doctor, Pacient, Reteta, Adauga_Cabinet, Adauga_Pacienti, Servicii, Recenzii, Programare

admin.site.register(Doctor)
admin.site.register(Pacient)
admin.site.register(Reteta)
admin.site.register(Adauga_Cabinet)
admin.site.register(Adauga_Pacienti)
admin.site.register(Servicii)
admin.site.register(Recenzii)
admin.site.register(Programare)

# Register your models here.
