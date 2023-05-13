from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [    
    path('',views.principal,name='principal'),
    path('registro/',views.registro,name='registro'),    
    path('login/',LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name = 'logout.html'),name='logout'),
    path('live_video/',views.live_video,name='live_video'),
    path('usuario/',views.usuario,name='usuario'),
    path('comentarios/<int:id>',views.vista_comentarios,name='comentarios'),
    path('iniciar_transmision/', views.iniciar_transmision, name='iniciar_transmision'),
    path('guardar/',views.guardarVideo,name='guardarVideo'),
    path('exito/',views.exito,name='exito'),
    path('stream/',views.streamz,name='stream')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)