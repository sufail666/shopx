
from django.urls import path, include

from todoapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id1>/',views.update,name='update'),
    path('chome/',views.listview.as_view(),name='chome'),
    path('cdetail/<int:pk>/',views.detailview.as_view(),name='cdetail'),
    path('cupdate/<int:pk>/',views.updateview.as_view(),name='cupdate'),
    path('cdelete/<int:pk>/',views.deleteview.as_view(),name='cdelete'),
]
