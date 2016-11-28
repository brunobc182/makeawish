from rest_framework.permissions import IsAuthenticated

from makeawish_project.utils import IsAdminOrSelf
from models import Wish
from serialiazers import WishSerializer
from rest_framework import viewsets


class WishViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrSelf,)
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
