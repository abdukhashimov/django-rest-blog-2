from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'replies')

    def get_user(self, obj):
        output = {}
        output['email'] = str(obj.user)
        output['profile_picture'] = obj.user.get_profile_picture
        return output

    def get_replies(self, obj):
        comments = obj.child_comments
        reply = []
        comment_dict = {}
        for comment in comments:
            comment_dict['user'] = str(comment.user)
            comment_dict['reply'] = {
                'text': comment.comment,
                'created_at': comment.created_at,
                'parent_id': comment.parent_id
            }
            reply.append(comment_dict.copy())
        return reply
