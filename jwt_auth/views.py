from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from jwt_auth.models import CrmUser
from jwt_auth.serializers import UserSerializer, RegisterSerializer

class UserDetailAPI(APIView):
  permission_classes = (IsAuthenticated, )
  def get(self,request,*args,**kwargs):
    user = CrmUser.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class APILogoutView(APIView):
  permission_classes = (IsAuthenticated,)

  def post(self, request, *args, **kwargs):
    if self.request.data.get('all'):
      token: OutstandingToken
      for token in OutstandingToken.objects.filter(user=request.user):
        _, _ = BlacklistedToken.objects.get_or_create(token=token)
      return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
    refresh_token = self.request.data.get('refresh_token')
    token = RefreshToken(token=refresh_token)
    token.blacklist()
    return Response({"status": "OK, goodbye"})