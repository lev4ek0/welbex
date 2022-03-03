from rest_framework import serializers

from .models import Table


class TableSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Table
        fields = ('pk', 'date', 'name', 'amount', 'distance')

    def create(self, validated_data):
        return Table.objects.create_table(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class TableRequestSerializer(serializers.Serializer):
    limit = serializers.IntegerField(default=5)
    offset = serializers.IntegerField(default=0)
    value = serializers.CharField(max_length=100, allow_blank=True, required=False, default='')
    eq = serializers.CharField(max_length=10, allow_blank=True, required=False)
    thead = serializers.CharField(max_length=20, allow_blank=True, required=False)
    sort_by = serializers.CharField(max_length=20, allow_blank=True, required=False)
    sort_type = serializers.CharField(max_length=10, allow_blank=True, required=False, default='')

    def validate(self, attrs):
        limit = attrs.get('limit', 5)
        offset = attrs.get('offset', 0)
        if offset < 0:
            raise serializers.ValidationError('Страница не может быть отрицательной')
        if limit < 1:
            raise serializers.ValidationError('На одной странице не может быть < 1 записи')
        return attrs
