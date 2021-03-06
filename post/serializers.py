import json
from rest_framework import serializers
from post.models import Post
from comment.serializers import CommentSerializer


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(
        view_name='post-detail',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('url', 'title', 'thumbnail', 'author', 'timestamp')


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    tag = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(many=True, read_only=True)
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'author',
                  'content', 'tag', 'category', 'timestamp', 'comment')

    def get_author(self, obj):
        user = {}
        user['author'] = str(obj.author)
        user['profice_picture'] = obj.author.get_profile_picture
        return user

    def get_comment(self, obj):
        comments = {}
        for index, comment in enumerate(obj.get_comments):
            comments[str(index)] = CommentSerializer(comment).data

        return comments
