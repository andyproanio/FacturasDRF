from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import requests, os


# Create your views here.


class FiltrarInventario(APIView):
    def get(self, request):
        mes = request.query_params['mes']
        cedula = request.query_params['cedula']

        c = connection.cursor()
        try:
            c.execute('TRUNCATE facturas_inventario')
            c.execute('ALTER SEQUENCE facturas_inventario_id_seq RESTART')
            c.execute(f"INSERT INTO facturas_inventario SELECT * FROM {mes} WHERE IDENTIFICACION_RECEPTOR LIKE '{cedula}%' ORDER BY id ASC")
        finally:
            c.close()

        hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
        if hostname:
            response = requests.get(f'https://{hostname}/api/Inventario')
        else:
            response = requests.get('http://localhost:8000/api/Inventario')
        return Response(response.json())
