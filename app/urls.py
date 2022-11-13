from django.urls import path
from .views import home, pacientes, doctores, citas, pagos

urlpatterns = [
    path('', home, name='home'),
    path('pacientes/', pacientes, name='pacientes'),
    path('doctores/', doctores, name='doctores'),
    path('citas/', citas, name='citas'),
    path('pagos/', pagos, name='pagos'),
]