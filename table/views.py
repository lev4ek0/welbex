from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TableSerializer, TableRequestSerializer
from .table_service import get_table_and_amount


class TableAPIView(APIView):
    table_serializer_class = TableSerializer
    table_request_serializer_class = TableRequestSerializer

    def get(self, request):
        serializer = self.table_request_serializer_class(data=request.GET)
        serializer.is_valid(raise_exception=True)
        table, amount = get_table_and_amount(serializer.data)
        serializer = self.table_serializer_class(instance=table, many=True)
        table = serializer.data
        return Response({'table': table, 'amount': amount}, status=status.HTTP_200_OK)
