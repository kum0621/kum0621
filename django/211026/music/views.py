from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import(
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)

from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer
# Create your views here.

# DRF 사용할때 필수 !!
@api_view(['GET','POST'])
def artist_create(request):
    '''
    GET : 아티스트 목록(JSON형태의 응답) 반환
    POST : 아티스트 생성
    '''

    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        # artists = Artist.objects.order_by('-pk')
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data) # JSON 응답
    elif request.method == 'POST':
        # DB에 내용 추가 !!!
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def artist_detail_update_delete(request, artist_pk):
    '''
    GET : artist_pk번 정보(JSON) 반환
    PUT : artist 정보 수정
    DELETE : 정보 삭제
    '''
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'GET': 
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        artist.delete()
        data = {
            'delete': f'데이터 {artist_pk}번이 삭제되었습니다.'
        }
        return Response(data , status=HTTP_204_NO_CONTENT)

@api_view(['POST'])
def music_create(request, artist_pk):
    '''
    POST : artist_pk번 게시글에 댓글 생성
    '''
    artist = get_object_or_404(Artist,pk=artist_pk)
    if request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(artist=artist)
            return Response(serializer.data, status=HTTP_201_CREATED)

@api_view(['GET'])
def music_list(request):

    if request.method == 'GET':
        musics = Music.objects.order_by('-pk')
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def music_detail_update_delete(request, music_pk):
    '''
    GET : music_pk번 정보(JSON) 반환
    PUT : music 정보 수정
    DELETE : 정보 삭제
    '''
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET': 
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'데이터 {music_pk}번이 삭제되었습니다.'
        }
        return Response(data , status=HTTP_204_NO_CONTENT)