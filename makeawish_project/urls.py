from django.conf.urls import include, url
from django.contrib import admin
from makeawish_project import routers

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(routers.router.urls)),
]
