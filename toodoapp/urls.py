from django.urls import path
from . import views
urlpatterns = [
    path('',views.add,name='add'),
    path('detail',views.detail,name="detail"),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvadd/',views.TaskListView.as_view(),name="cbvadd"),
    path("cbvdetail/<int:pk>/",views.TaskDetailView.as_view(),name="cbvdetail"),
    path("cbvupdate/<int:pk>/",views.TaskKUpdateView.as_view(),name="cbvupdate"),
    path("cbvdelete/<int:pk>/",views.TaskDeleteView.as_view(),name="cbvdelete")
]
