from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/(?P<category_name>\w+)', 'links.views.show_category'),
    url(r'^$', 'links.views.homepage'),
]
