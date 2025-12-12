from rest_framework import serializers
from .models import *

class DailyPositiveCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPositiveCard
        fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email', 'bio', 'profile_image', 'created_at']
        read_only_fields = ['email', 'created_at']


class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ['id', 'title', 'content', 'created_at']


class EmotionPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionPrompt
        fields = "__all__"
