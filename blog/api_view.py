from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerializer(all_posts, many=True).data
    return Response({'data':data})



@api_view(['GET'])
def post_detail_api(request , id):
    post = get_object_or_404(Post , id=id)
    data = PostSerializer(post).data
    return Response({'data':data})
