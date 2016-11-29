from rest_framework.permissions import IsAuthenticatedOrReadOnly

from models import Wish
from serialiazers import WishSerializer
from rest_framework import viewsets


class WishViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
