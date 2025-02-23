from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

# View to list and create posts (Only authenticated users can create)
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can create posts

    def perform_create(self, serializer):
        # Automatically set the author of the post as the authenticated user
        serializer.save(author=self.request.user)

# View to retrieve, update, and delete posts (Users can only edit their own posts)
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Admin users can see all posts
        if user.is_staff:
            return Post.objects.all()
        # Regular users can only see and edit their own posts
        return Post.objects.filter(author=user)
