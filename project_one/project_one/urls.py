from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from Med import views #import views from Med app
from django.views.generic import  TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('contact/',include('project_one.urls')),

    path('', views.home, name=""), #Url routing
    path('home/', views.home, name="home"),
    path('contact/',TemplateView.as_view(template_name="contact.html"),name='contact'), 
    path('about/', views.about, name="about"), 
    path('login/', views.login_view, name="login"), 
    path('logout/', views.logout_view, name="logout"), 
    # path('dashboard/', views.dashboard, name="dashboard"), 
    path('department/', views.department, name="department"), 
    path('hospital/', views.hospital, name="hospital"), 
    path('make_appointment/', views.make_appointment, name="appoint"), 
    path('dashboard/', views.appointment_list, name="dashboard"), 
    # path('hospital/', views.ImgeHandlers, name="imgehandlers"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
