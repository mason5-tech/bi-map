from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView),
    path('post/coordinate', post_coordinate, name = "post_coordinate"),
    path('get/ajax/loupan', getLoupan, name = "get_loupan"),
    path('post/shopInfo_daqu', shopInfo_daqu, name = "shopInfo_daqu"),
]