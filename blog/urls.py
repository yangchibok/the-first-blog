from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='post_detail'),
        url(r'^post/(?P<pk>[0-9]+)/comments/new/$', views.comment_new, name='comment_new'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/(?P<post_pk>[0-9]+)/comments/(?P<pk>[0-9]+)/edit/$', views.comment_edit, name='comment_edit'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

