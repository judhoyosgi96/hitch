from rest_framework import serializers

from django.core.validators import FileExtensionValidator

class DatasetSerializer(serializers.Serializer):
    file=serializers.FileField(validators=[FileExtensionValidator(['xlsx'])])

