from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ,name = "index"),
    url(r'^add/', views.add_task),
    url(r'^(?:edit-(?P<task_id>\d+)/)?$', views.edit_task,name = 'task_id'),
     url(r'^(?:delete-(?P<task_id>\d+)/)?$', views.delete,name = 'delete'),
    url(r'^not_finshed/', views.not_finshed),
]
