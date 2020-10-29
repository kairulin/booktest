from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:pid>/<str:del_pass>',views.index),
    path('list/', views.listing),
    # path('post/', views.posting),
]

