from django.conf.urls import url
from .views import lavista, SopesView

urlpatterns=[
url(r'^$',lavista),
url(r'^sopes/$', SopesView.as_view()),
]
