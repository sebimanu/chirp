from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from message.views import RegisterView, TimelineView, MyProfileView, ProfileView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TimelineView.as_view(), name='index'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
    url(r'^my-profile/$', login_required(MyProfileView.as_view()), name='my-profile'),
    url(r'^profile/(?P<slug>[-\w]+)/$', login_required(ProfileView.as_view()), name='profile'),
]
