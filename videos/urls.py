from django.conf.urls import url , include
from videos import views
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


app_name = 'videos'


urlpatterns = patterns('',

    url( r'upload/', views.upload, name = 'jfu_upload' ),
    url( r'^delete/(?P<pk>\d+)$', views.upload_delete, name = 'jfu_delete' ),
    url(r'^llistavideos/$', views.llista_videos, name="llista_videos"),
)

