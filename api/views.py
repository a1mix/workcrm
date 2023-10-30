from rest_framework import views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.models import House
from api.serializers import HouseSerializer

class HouseAPIView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        print(user)
        if user.groups.filter(name='Manager').exists():
            houses = House.objects.all()
            serializer = HouseSerializer(houses, many=True)
            return Response(serializer.data)
        return Response(status=403)

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)