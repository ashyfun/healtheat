from rest_framework import generics, status
from rest_framework.response import Response

from healtheat.apps.menu.models import DailyMenuModel
from healtheat.apps.menu.serializers import DailyMenuSerializer


class DailyMenuGenericAPIView(generics.GenericAPIView):
    serializer_class = DailyMenuSerializer
    queryset = DailyMenuModel.objects.all()


class DailyMenuList(DailyMenuGenericAPIView):

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({'items': serializer.data})

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        response = Response(status=status.HTTP_201_CREATED)
        if serializer.is_valid():
            serializer.save()
        else:
            response.data = {'errors': serializer.errors}
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response


class DailyMenuDetail(DailyMenuGenericAPIView):
    lookup_field = 'day'

    def get(self, request, day):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def patch(self, request, day):
        serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
        response = Response()
        if serializer.is_valid():
            serializer.save()
        else:
            response.data = {'errors': serializer.errors}
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response

    def delete(self, request, day):
        daily_menu = self.get_object()
        daily_menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
