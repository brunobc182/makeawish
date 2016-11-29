from rest_framework.serializers import ModelSerializer

from models import Wish


class WishSerializer(ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'

