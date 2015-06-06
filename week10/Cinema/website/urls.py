from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings
import register.views
import login.views

urlpatterns = patterns('website.views',
                       url(r'^$', 'index'),
                       url(r'^about/$', 'about'),
                       url(r'^register/$', register.views.register,
                           name='register'),
                       url(r'^login/$', login.views.user_login, name='login'),


                       ) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
