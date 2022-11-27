"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "my_app"

urlpatterns = [
    url('admin/', admin.site.urls),
    url('acasa/', views.acasa, name="acasa"),
    url('acasa_s/', views.acasa_s, name="acasa_s"),
    url(r'my_app/', include("my_app.urls", namespace='my_app')),
    url(r'inregistrare/$', views.inregistrare, name="inregistrare"),
    url(r'inregistrare_pacient/$', views.inregistrare_pacient, name="inregistrare_pacient"),
    url(r'contul_meu_doctor/$', views.contul_meu_doctor, name="contul_meu_doctor"),
    url(r'cautare_cabinet_medical/$', views.cautare_medical, name="cautare_medical"),
    url(r'cautare_cabinet_stomatologie/$', views.cautare_s, name="cautare_s"),
    url(r'pag_cabinete/(?P<pk>\d+)/$', views.pag_cabinete, name="pag_cabinete"),
    url(r'programare/(?P<pk>\d+)/$', views.programare, name="programare"),
    url(r'^favorite/$', views.favorite, name="favorite"),
    url(r'^favorite_f/(?P<pk>\d+)/$', views.favorite_f, name="favorite_f"),
    ##############DOCTOR##############
    url(r'inregistreaza_cabinet/$', views.inregistreaza_cabinet, name="inregistreaza_cabinet"),
    url(r'setari_doctor/$', views.setari_doctor, name="setari_doctor"),
    url(r'logout_doctor/$', views.logout_doctor, name="logout_doctor"),
    url(r'adauga_pacienti/$', views.adauga_pacienti, name="adauga_pacienti"),
    url(r'pacienti_inregistrati/$', views.pacienti_inregistrati, name="pacienti_inregistrati"),
    url(r'trimite_reteta/$', views.trimite_reteta, name="trimite_reteta"),
    url(r'cabinete_inregistrate/$', views.cabinete_inregistrate, name="cabinete_inregistrate"),
    url(r'servicii/$', views.servicii, name="servicii"),
    url(r'adauga_servicii/(?P<pk>\d+)/$', views.adauga_servicii, name="adauga_servicii"),
    ###############PACIENT#############
    url(r'contul_meu_pacient/$', views.contul_meu_pacient, name="contul_meu_pacient"),
    url(r'deconectare_pacient/$', views.logout_pacient, name="logout_pacient"),
    url(r'setari_pacient/$', views.setari_pacient, name="setari_pacient"),
    url(r'programari_pacient/$', views.programari_pacient, name="programari_pacient")

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
