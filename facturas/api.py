from .models import Inventario
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from email.message import EmailMessage
from .serializers import *
import smtplib, os


class InventarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Inventario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InventarioSerializer


class SubirComprobantesViewSet(viewsets.ViewSet):
    serializer_class = SubirArchivoSerializer

    def create(self, request):
        archivo = request.FILES.get('archivo')

        email_sender = 'andy_proanio@yahoo.com.ar'
        password = 'whvycsmcyayprjmz'

        subject = "Envío de Comprobantes"

        em = EmailMessage()

        em['From'] = email_sender
        em['To'] = 'andy.proanio@gmail.com'
        em['Subject'] = subject
        em.set_content('Envío los comprobantes del mes')

        with open(str(archivo), 'wb') as f:
            f.write(archivo.read())

        filename = str(archivo)

        with open(filename, 'rb') as attachmentFile:
            content = attachmentFile.read()
            em.add_attachment(content, maintype='application', subtype=filename.split('.')[-1], filename=filename)

        os.remove(filename)

        try:
            smtp = smtplib.SMTP('smtp.mail.yahoo.com', 587)
            smtp.starttls()
            smtp.login(email_sender, password)
            smtp.send_message(em)
            return Response('Comprobante enviado correctamente.')
        except Exception as e:
            return Response(f'Falló el envío del comprobante: {str(e)}')
