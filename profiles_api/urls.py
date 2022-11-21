from django.urls import path

from profiles_api import views


urlpatterns=[
 path('',views.HelloWorldApiView.as_view()),
 path('hello-world-api',views.HelloWorldApiView.as_view()),
 path('hello-world-api/',views.HelloWorldApiView.as_view())
]
