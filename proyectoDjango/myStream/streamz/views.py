from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm,guardarVideoForm,guardarComentario
from crispy_forms.helper import FormHelper
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.http import HttpRequest
import cv2
import threading
import os
import datetime
import django
from django.conf import settings
from django.contrib.auth.models import User
from streamz.models import comentarios
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from .models import Video

def principal(request):
    imagenes = Video.objects.all().values()
    context = {
        'imagenes':imagenes
    }
    return render(request,'main.html',context)

@login_required
def live_video(request):
    cap = cv2.VideoCapture(0)

    def gen():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    return StreamingHttpResponse(gen(), content_type='multipart/x-mixed-replace; boundary=frame')


class camara(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed,self.frame) = self.video.read()
        threading.Thread(target=self.update,args=()).start()
            
    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed,self.frame) = self.video.read()

def gen(camara):
    while True:
        frame = camara.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')
        
def obtenerVideo(request):
    if request.user.is_authenticated:
        return redirect('/stream')
    else:
        return redirect('/login')

def streamz(request):
    template = loader.get_template('stream.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('/')
    else:
        form = UserRegisterForm()

    helper = form.helper    
    context = {
        'form':form,
        'helper':helper  
    }
    return render(request,'registro.html',context)

def usuario(request):
    context = {'myUser':request.user}
    return render(request,'usuario.html',context)

def vista_comentarios(request,id):
    comments = comentarios.objects.filter(id_video=id)
    imagen = Video.objects.get(id=id)
    helper = None
    form = guardarComentario()    
    if request.method == 'POST':
        form = guardarComentario(request.POST)
        if form.is_valid():
            video = Video.objects.get(id=id)            
            com = comentarios(username=request.user,comentario=form.cleaned_data.get('comentario'),id_video=video)
            com.save()
            return redirect('/comentarios/{}'.format(id))
        else:
            helper = form.helper
    context = {
        'comments':comments,
        'imagen':imagen,
        'helper':helper,
        'form':form
    }
    return render(request,'comentarios.html',context)

def borrar_imagen(url):
    try:
        path = os.path.join(settings.MEDIA_ROOT,url)
        print(path)
        os.remove(path)
        return True
    except Exception as e:
        return False

@login_required
def guardarVideo(request):
    cam = camara()
    frame = cam.get_frame()
    nombreImagen = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.jpg'
    rutaImagen = os.path.join(settings.MEDIA_ROOT,"videos",nombreImagen)
    with open(rutaImagen,'wb') as f:
       f.write(frame)
    if request.method == 'POST':
        form = guardarVideoForm(request.POST, request.FILES)
        if form.is_valid():
            total = Video.objects.count()
            if total == 10:
                primero = Video.objects.order_by('fecha_publicacion').first()
                borrar_imagen(primero.imagen)
                primero.delete()            
            video = Video(usuario=request.user,imagen="videos/{}".format(nombreImagen))
            video.save()
            return redirect('exito')
    else:
        form = guardarVideoForm()
    return render(request, 'guardar_video.html', {'form': form})        

def exito(request):
    return render(request, 'exito.html')
