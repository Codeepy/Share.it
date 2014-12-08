from rest_framework import serializers
from share_it.models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('lat_position', 'long_position')