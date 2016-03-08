from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'task.views.home', name='home'),
]
