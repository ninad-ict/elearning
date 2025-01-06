from rest_framework import serializers
from .models import UserLogin,ContentUpload

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id', 'email', 'name', 'role']


    def validate_email(self, value):
        """
        Custom validation to ensure email doesn't contain '@yahoo'.
        """
        if "@yahoo" in value:
            raise serializers.ValidationError("Yahoo email addresses are not allowed.")
        return value


class ContentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentUpload
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at']  # Exclude 'is_deleted'

    def validate_content(self, value):
        """
        Custom validation to ensure content doesn't exceed 1000 characters.
        """
        if len(value) > 1000:
            raise serializers.ValidationError("Content cannot be more than 1000 characters.")
        return value