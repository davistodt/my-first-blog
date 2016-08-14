from django.conf.urls import url
from . import views

#add out first url pattern:
urlpatterns = [
    url(r'^$', views.post_list, name='post_list')

]
