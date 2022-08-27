from django.urls import path
from . import views

urlpatterns = [
    path('product', views.SearchProduct),
    path('productdata', views.ProductData),
    path('isliked', views.isLiked),
    path('like', views.LikeFunction),
    path('substitute', views.Substitute),

    path('molicule', views.SearchMolicule),
    path('generic', views.Generic),

    path('doctormolicule', views.DoctorMolicules),
    path('doctoritems', views.DoctorItems),
    path('doctorprofile', views.doctorProfile),

]