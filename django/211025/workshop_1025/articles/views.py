from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import(
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
# Create your views here.

# DRF 사용할때 필수 !!
@api_view(['GET','POST'])
def article_create(request):
    '''
    GET : 게시물 목록(JSON형태의 응답) 반환
    POST : 게시물 생성
    '''

    if request.method == 'GET':
        # data가 필요! => JSON을 구성하려면 serializer가 필요!
        articles = get_list_or_404(Article)
        articles = Article.objects.order_by('-pk')
        
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data) # JSON 응답
    elif request.method == 'POST':
        # DB에 내용 추가 !!!
        # form = ArticleForm(request.POST)
        # 데이터는 어디서 꺼내지??
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail_update_delete(request, article_pk):
    '''
    GET : article_pk번 게시글 정보(JSON) 반환
    GET : 
    '''
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET': 
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data , status=HTTP_204_NO_CONTENT)

@api_view(['POST'])
def comment_create(request, article_pk):
    '''
    POST : article_pk번 게시글에 댓글 생성
    '''
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=HTTP_201_CREATED)

@api_view(['GET'])
def comment_list(request):

    if request.method == 'GET':
        comments = Comment.objects.order_by('-pk')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
