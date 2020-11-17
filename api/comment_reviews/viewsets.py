from rest_framework.viewsets import ModelViewSet
from .models import Comment, Review
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewsets(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()


class CommentViewsets(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
