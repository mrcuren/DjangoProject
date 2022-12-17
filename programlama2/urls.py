"""programlama2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from home import views
from user import views as UserViews

urlpatterns = [
    path("", include('home.urls')),
    path("home/", include('home.urls')),
    path("course/", include('course.urls')),
    path("user/", include('user.urls')),
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
    path("referanslar/", views.referanslar, name="referanslar"),
    path("iletisim/", views.iletisim, name="iletisim"),
    path("category/<int:id>/<slug:slug>/", views.category_courses, name='category_courses'),
    path("course/<int:id>/<slug:slug>/", views.course_detail, name='course_detail'),
    path("logout/", UserViews.logout_view, name="logout_view"),
    path("login/", UserViews.login_view, name="login_view"),
    path("signup/", UserViews.signup_form, name="signup"),



]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
