from django.shortcuts import render, redirect
from .models import Patologia, Consulta, Documento, Numeros_Farmacia
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, PatologiaSearchForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from twilio.rest import Client
from datetime import datetime, timedelta
import io
import qrcode
import logging
import json

logger = logging.getLogger('django')




def signup(request):
    form = CreateUserForm()
    context = {'form':form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada con exito para ' + user)
            return redirect('login')

    return render(request, 'main/signup.html', context)

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'El Usuario o la Contraseña son Incorrectos')

    context = {}
    return render(request, 'main/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html')

@login_required(login_url='login')
def pag3(request):
    return render(request, 'main/pag3.html')

@login_required(login_url='login')
def pag4(request):
    return render(request, 'main/pag4.html')

@login_required(login_url='login')
def pag5(request):
    if request.method == 'POST':
        dolor = request.POST.get('dolor')
        request.session['dolor'] = dolor
        if dolor == 'Dolor_ligamentoso':
            return redirect('muneco_ligamentoso')
        elif dolor == 'Dolor_articular':
            return redirect('muneco_articular')
        elif dolor == 'Dolor_neurologico':
            return redirect('muneco_neurologico')
        else:
            return redirect('cuerpo')
    return render(request, 'main/pag5.html')

@login_required(login_url='login')
def pag6(request):
    if request.method == 'POST':
        dolor = request.POST.get('dolor')
        request.session['dolor'] = dolor
        if dolor == 'Dolor_muscular':
            return redirect('muneco_muscular')
        else:
            return redirect('muneco_tendinoso')
    return render(request, 'main/pag6.html')

@login_required(login_url='login')
def cuerpo(request):
    if request.method == 'POST':
        cuerpo_dolor = request.POST.get('cuerpo_dolor')
        request.session['cuerpo_dolor'] = cuerpo_dolor
        request.session['dolor'] = 'Todos'
        return redirect('patologias')
    return render(request, 'main/cuerpo.html')

@login_required(login_url='login')
def muneco_ligamentoso(request):
    if request.method == 'POST':
        cuerpo_dolor = request.POST.get('cuerpo_dolor')
        request.session['cuerpo_dolor'] = cuerpo_dolor
        return redirect('patologias')
    return render(request, 'main/muneco_ligamentoso.html')

@login_required(login_url='login')
def muneco_articular(request):
    if request.method == 'POST':
        cuerpo_dolor = request.POST.get('cuerpo_dolor')
        request.session['cuerpo_dolor'] = cuerpo_dolor
        return redirect('patologias')
    return render(request, 'main/muneco_articular.html')

@login_required(login_url='login')
def muneco_neurologico(request):
    if request.method == 'POST':
        cuerpo_dolor = request.POST.get('cuerpo_dolor')
        request.session['cuerpo_dolor'] = cuerpo_dolor
        return redirect('patologias')
    return render(request, 'main/muneco_neurologico.html')

@login_required(login_url='login')
def muneco_vascular(request):
    if request.method == 'POST':
        cuerpo_dolor = request.POST.get('cuerpo_dolor')
        request.session['cuerpo_dolor'] = cuerpo_dolor
        return redirect('patologias')
    return render(request, 'main/muneco_vascular.html')

@login_required(login_url='login')
def muneco_muscular(request):
    if request.method == 'POST':
        cuerpo_dolor = request.POST.get('cuerpo_dolor')
        request.session['cuerpo_dolor'] = cuerpo_dolor
        return redirect('patologias')
    return render(request, 'main/muneco_muscular.html')

@login_required(login_url='login')
def muneco_tendinoso(request):
    if request.method == 'POST':
        cuerpo_dolor = request.POST.get('cuerpo_dolor')
        request.session['cuerpo_dolor'] = cuerpo_dolor
        return redirect('patologias')
    return render(request, 'main/muneco_tendinoso.html')

@login_required(login_url='login')
def patologias(request):
    cuerpo_dolor = request.session.get('cuerpo_dolor')
    dolor = request.session.get('dolor')

    if dolor == 'Todos':
        patologias = Patologia.objects.filter(cuerpo=cuerpo_dolor)
    else:
        patologias = Patologia.objects.filter(cuerpo=cuerpo_dolor, dolor=dolor)

    if request.method == 'POST':
        patologia = request.POST.get('patologia')
        request.session['patologia'] = patologia
        return redirect('intensidad')
    return render(request, 'main/patologias.html', {'patologias': patologias, 'dolor':dolor})

@login_required(login_url='login')
def intensidad(request):
    if request.method == 'POST':
        intensidad_dolor = request.POST.get('intensidad_dolor')
        request.session['intensidad_dolor'] = intensidad_dolor

        dolor = request.session.get('dolor')
        if dolor in ['Dolor_tendinoso', 'Dolor_articular']:
            return redirect('duracion')
        else:
            return redirect('duracion6')
    return render(request, 'main/intensidad.html')

@login_required(login_url='login')
def duracion(request):
    if request.method == 'POST':
        duracion_dolor = request.POST.get('duracion_dolor')
        request.session['duracion_dolor'] = duracion_dolor
        return redirect('confirmacion')
    return render(request, 'main/duracion.html')

@login_required(login_url='login')
def duracion6(request):
    if request.method == 'POST':
        duracion_dolor = request.POST.get('duracion_dolor')
        request.session['duracion_dolor'] = duracion_dolor
        return redirect('confirmacion')
    return render(request, 'main/duracion6.html')




def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generate_pdf(request):
    context = {'mydata': 'Hello World'}
    return render_to_pdf('pdf_template.html', context)

def download_pdf(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    documentos = Documento.objects.filter(titulo=consulta.patologia, duracion=consulta.duracion)
    
    if documentos.exists():
        documento = documentos.first()
        titulo = documento.titulo
        contenido = documento.documento
        context = {
            'titulo': titulo,
            'contenido': contenido,
            'consulta': consulta
        }

        return render_to_pdf('main/pdf_template.html', context)
    else:
        return HttpResponse("No se encontró el documento para la consulta.", status=404)

@login_required(login_url='login')
def confirmacion(request):
    dolor = request.session.get('dolor')
    cuerpo_dolor = request.session.get('cuerpo_dolor')
    patologia = request.session.get('patologia')
    intensidad_dolor = request.session.get('intensidad_dolor')
    duracion_dolor = request.session.get('duracion_dolor')
    user = request.user

    consulta = Consulta.objects.create(
        user=user,
        dolor=dolor,
        cuerpo=cuerpo_dolor,
        patologia=patologia,
        intensidad=intensidad_dolor,
        duracion=duracion_dolor
    )

    # Generar URL de notificación
    local_ip = '192.168.1.111'  # Reemplaza esto con tu dirección IP local
    pdf_url = f'http://{local_ip}:8000/download_pdf/{consulta.id}/'
    texto = f"Hola, soy el usuario con ID de consulta: {consulta.id}"
    notify_url = f'https://wa.me/+14155238886?text={texto}'



    # Generar QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(notify_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='transparent')

    # Guardar QR code en un buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    qr_code_image = buffer.getvalue()

    documentos = Documento.objects.filter(titulo=patologia, duracion=duracion_dolor)
    if documentos.exists():
        documento = documentos.first()
        titulo = documento.titulo
        contenido = documento.documento
        return render(request, 'main/confirmacion.html', {
            'titulo': titulo,
            'contenido': contenido,
            'cuerpo': cuerpo_dolor,
            'intensidad': intensidad_dolor,
            'duracion': duracion_dolor,
            'qr_code_image': qr_code_image,
            'notify_url': notify_url
        })
    else:
        mensaje = "No se encontraron documentos que coincidan con los criterios de búsqueda."
        return render(request, 'main/confirmacion.html', {
            'mensaje': mensaje,
            'cuerpo': cuerpo_dolor,
            'intensidad': intensidad_dolor,
            'duracion': duracion_dolor,
            'qr_code_image': qr_code_image,
            'notify_url': notify_url
        })

def request_notifications(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    pdf_url = f'http://{request.get_host()}/download_pdf/{consulta_id}/'
    return render(request, 'main/notify.html', {'pdf_url': pdf_url})



def buscar_patologia(request):
    form = PatologiaSearchForm()
    resultados = []
    searched = False

    if 'query' in request.GET:
        form = PatologiaSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Patologia.objects.filter(
                titulo__icontains=query
            ) | Patologia.objects.filter(
                dolor__icontains=query
            ) | Patologia.objects.filter(
                cuerpo__icontains=query
            )
        searched = True

    return render(request, 'main/buscar_patologia.html', {'form': form, 'resultados': resultados, 'searched':searched})







# Tus credenciales de Twilio (Account SID y Auth Token)
account_sid = 'AC8c354ad3f0a5bc87bfb92d9adeb5d4ec'
auth_token = 'a7153a7af154b49ba7753c4f018a9652'
client = Client(account_sid, auth_token)

ngrok_url = '6c7d-88-0-70-19.ngrok-free.app'


@csrf_exempt  # Para que Twilio pueda enviar peticiones POST sin problemas
def whatsapp_webhook(request):

    mensaje = request.POST['Body'].strip()
    nombre_usuario = request.POST['ProfileName']
    numero_usuario = request.POST['From']


    consulta_id = mensaje.split(':')[-1].strip()
    pdf_url = f'http://{ngrok_url}/download_pdf/{consulta_id}/'

    
    message = client.messages.create(
        body=f'Bienvenido a Dolorfarma {nombre_usuario}!! Aquí tiene el PDF de su consulta. Esperamos que le sea de ayuda.',
        from_='whatsapp:+14155238886',
        to=numero_usuario,
        media_url=[pdf_url]
    )
    

    print(nombre_usuario, numero_usuario[-9:], consulta_id)

    from django.shortcuts import get_object_or_404

    consulta = get_object_or_404(Consulta, id=consulta_id)
    
    # Extraer el usuario asociado a la consulta
    usuario = consulta.user

    Numeros_Farmacia.objects.create(
        farmacia=usuario,
        telefono=numero_usuario[-9:],
        notificaciones=False
    )


    return HttpResponse('Mensaje')