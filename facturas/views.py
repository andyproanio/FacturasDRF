from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import requests

# Create your views here.


class FiltrarInventario(APIView):
    def get(self, request):
        mes = request.query_params['mes']

        c = connection.cursor()
        try:
            c.execute('TRUNCATE facturas_inventario')
            c.execute('ALTER SEQUENCE facturas_inventario_id_seq RESTART')
            c.execute(f'INSERT INTO facturas_inventario SELECT * FROM {mes} ORDER BY id ASC')
        finally:
            c.close()

        response = requests.get('http://localhost:8000/api/Inventario')
        return Response(response.json())

