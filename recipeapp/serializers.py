from rest_framework import serializers
from .models import recipe,review
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['id','recipe_name','recipe_ingredients','instructions','cuisine','meal_type']
        model=recipe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
    def create(self,validated_data):  #after validation
        user=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        user.save()
        return user

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=review
        fields=['id','recipe_name','user','rating','comment']