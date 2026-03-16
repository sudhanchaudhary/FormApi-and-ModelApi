from django.urls import path
from .views import IndexView,CreateDataView,UpdateDataView,DeleteDataView
urlpatterns = [
    path('',IndexView.as_view(),name='g_index'),
    path('create/',CreateDataView.as_view(),name='g_create'),
    path('update/<pk>',UpdateDataView.as_view(),name='g_update'),
    path('delete/<pk>',DeleteDataView.as_view(),name='g_delete')
]
