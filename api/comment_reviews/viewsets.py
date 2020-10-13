from rest_framework.viewsets import ModelViewSet
from .models import Comment, Review
from .serializers import CommentSerializer, ReviewSerializer


class CommentViewsets(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReviewViewsets(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
