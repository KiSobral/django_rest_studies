from rest_framework.serializers import ModelSerializer
from .models import Comment, Review


class CommentSerializer(ModelSerializer):
    model = Comment
    fields = ('id', 'commentary')


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'commentary', 'review')
