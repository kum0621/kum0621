from rest_framework import serializers
from .models import Artist, Music 

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','name',)


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id','title',)

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id','title','artist',)
        # is valid에서 제외
        read_only_fields = ('artist', )

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Artist
        fields = ('id','name','music_set','music_count',)
