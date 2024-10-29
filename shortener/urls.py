from django.urls import path

from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save, name='save'),
    path('<url_id>/', views.deflect, name = 'deflect'),
]