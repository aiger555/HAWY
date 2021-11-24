from rest_framework import serializers

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('star', 'doctor')

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            doctor = validated_data.get('doctor', None),
            defaults = {'star': validated_data.get('star')}
        )
        return rating
