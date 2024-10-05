from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from main.views import index, cuerpo, pag3, pag4, pag5, pag6, cuerpo, muneco_ligamentoso, muneco_articular, muneco_neurologico, muneco_vascular, muneco_muscular, muneco_tendinoso, intensidad, duracion, duracion6, confirmacion, signup, login_page, logout_page, patologias, buscar_patologia, download_pdf, generate_pdf, request_notifications, whatsapp_webhook

urlpatterns = [
    path('', index, name='index'),
    # path('signup/', signup, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('pag3/', pag3, name='pag3'),
    path('pag4/', pag4, name='pag4'),
    path('pag5/', pag5, name='pag5'),
    path('pag6/', pag6, name='pag6'),
    path('cuerpo/', cuerpo, name='cuerpo'),
    path('muneco_ligamentoso/', muneco_ligamentoso, name='muneco_ligamentoso'),
    path('muneco_articular/', muneco_articular, name='muneco_articular'),
    path('muneco_neurologico/', muneco_neurologico, name='muneco_neurologico'),
    path('muneco_vascular/', muneco_vascular, name='muneco_vascular'),
    path('muneco_muscular/', muneco_muscular, name='muneco_muscular'),
    path('muneco_tendinoso/', muneco_tendinoso, name='muneco_tendinoso'),
    path('patologias/', patologias, name='patologias'),
    path('intensidad/', intensidad, name='intensidad'),
    path('duracion/', duracion, name='duracion'),
    path('duracion6/', duracion6, name='duracion6'),
    path('confirmacion/', confirmacion, name='confirmacion'),
    path('download_pdf/<int:consulta_id>/', download_pdf, name='download_pdf'),
    path('request_notifications/<int:consulta_id>/', request_notifications, name='request_notifications'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
    path('buscar_patologia/', buscar_patologia, name='buscar_patologia'),
    path('whatsapp_webhook/', whatsapp_webhook, name='whatsapp_webhook'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

