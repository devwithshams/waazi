from rest_framework import serializers
from .models import Scholar, Category, Waazi

class WaaziSerializer(serializers.ModelSerializer):
    audio_url = serializers.SerializerMethodField()
    scholar_name = serializers.CharField(source='scholar.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Waazi
        fields = ['id', 'title', 'scholar', 'scholar_name', 'category', 'category_name', 
                  'audio_url', 'duration', 'description', 'views', 'downloads', 'created_at']

    def get_audio_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.audio_file.url) if obj.audio_file else None

class ScholarListSerializer(serializers.ModelSerializer):
    waazi_count = serializers.SerializerMethodField()

    class Meta:
        model = Scholar
        fields = ['id', 'name', 'image', 'country', 'waazi_count']

    def get_waazi_count(self, obj):
        return obj.waazi_set.count()

class ScholarDetailSerializer(serializers.ModelSerializer):
    waazi = WaaziSerializer(many=True, read_only=True)

    class Meta:
        model = Scholar
        fields = ['id', 'name', 'bio', 'image', 'country', 'social_links', 'created_at', 'waazi']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']