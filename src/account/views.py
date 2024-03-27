from rest_framework import generics
from rest_framework.response import Response

from .serializers import RegisterSerializer, UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    """
    Register view
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Register new user
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'message': 'Account created',
        })
