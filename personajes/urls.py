from django.conf.urls import url
from .views import PersonajesView

urlpatterns=[
url(r'^mb/$', PersonajesView.as_view()),
]
