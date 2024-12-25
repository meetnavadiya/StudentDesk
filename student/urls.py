from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('create',views.create_student, name='create'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('update/<int:pk>',views.update_student, name='update'),
    path('details/<int:pk>',views.details, name='details'),
    path('delete/<int:pk>',views.delete_stu, name='delete'),
]