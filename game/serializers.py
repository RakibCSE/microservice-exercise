from rest_framework import serializers

from game.models import Category, Game


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'image', 'category',)
