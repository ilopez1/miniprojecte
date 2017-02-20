from django.conf.urls import url, include
from usuaris import views

app_name = 'usuaris'

urlpatterns = [
    # ex: /practicaMonoPoli/...
    #url(r'^create/', views.Afegir_Modificar_Jugador, name='Afegir_Jugador'),
    #url(r'^modify/(?P<jugador_id>\d+)/$', views.Afegir_Modificar_Jugador, name='Modificar_Jugador'),
    #url(r'^eliminar/(?P<jugador_id>[0-9]+)/$',views.Eliminar_Jugador, name="Eliminar_Jugador"),
    #url(r'^llista/$', views.llista_jugadors, name='llista_jugadors'),
    url(r'^login/$', views.login, name="login", ),
    url(r'^logout/$', views.logout, name="logout", ),
    url(r'^registre/$', views.registrar, name="registre"),
    url(r'^$', views.index, name="index"),
]
