from rest_framework.serializers import ModelSerializer

from models import Wish


class WishSerializer(ModelSerializer):
    fields = '__all__'

    class Meta:
        model = Wish
