from django.urls import path

from . import views

app_name = 'report'

urlpatterns = [

    path('', views.index, name='index'),
    #path('admin/', admin.site.urls),

    path('', views.report_create, name='report_create'),
    path('', views.report_read, name='report_read'),

]