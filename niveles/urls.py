from django.conf.urls import url
from .views import NivelesView

urlpatterns=[
url(r'^levels/$', NivelesView.as_view()),
]
