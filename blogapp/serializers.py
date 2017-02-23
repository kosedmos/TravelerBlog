from rest_framework import serializers
from .models import Article


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author_id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField()
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author_id = validated_data.get('author_id', instance.content)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
#         return instance


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'author_id', 'created', "updated")
