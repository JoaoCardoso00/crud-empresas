from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Empresa
from .serializers import EmpresaSerializer

@api_view(['GET'])
def getEmpresas(request):
    empresas = Empresa.objects.all()
    serializer = EmpresaSerializer(empresas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createEmpresa(request):
    serializer = EmpresaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getEmpresa(request, pk):
    try:
        empresa = Empresa.objects.get(pk=pk)
    except Empresa.DoesNotExist:
        return Response({'error': 'Empresa não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmpresaSerializer(empresa)
    return Response(serializer.data)

@api_view(['PUT'])
def updateEmpresa(request, pk):
    try:
        empresa = Empresa.objects.get(pk=pk)
    except Empresa.DoesNotExist:
        return Response({'error': 'Empresa não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmpresaSerializer(empresa, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteEmpresa(request, pk):
    try:
        empresa = Empresa.objects.get(pk=pk)
    except Empresa.DoesNotExist:
        return Response({'error': 'Empresa não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

    empresa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
