from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'slug',
            'short_description',
            'content',
            'is_featured',
            'repo_url',
            'live_url',
            'image',
            'created_at',
        ]