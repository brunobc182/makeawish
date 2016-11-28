from rest_framework import routers

from wishes.views import WishViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'wishes', WishViewSet)
