from django.urls import path
from myapp import views


urlpatterns = [
    path("", views.test_view, name="jwt"),
    path('hello/', views.HelloView.as_view(), name='hello'),
]

