from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.file_list, name='file_list'),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^(?P<file_id>[0-9]+)/edit/upload/$',
        views.edit_and_upload_file, name='edit_and_upload_file'),
    url(r'^(?P<file_name>.+)/get/versions/$',
        views.get_versions, name='get_versions'),
]

app_name = 'file_mngmnt'
