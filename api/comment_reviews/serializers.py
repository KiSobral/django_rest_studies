from rest_framework.serializers import ModelSerializer
from .models import Comment, Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'commentary', 'review')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'commentary')
