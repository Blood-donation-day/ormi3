from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    '''
    PostSerializer에서 CommentSerializer를 사용하기 때문에 CommentSerializer를 먼저 정의

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    '''
    author_username = serializers.SerializerMethodField()


    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_username', 'post', 'content', 'created_at'] # author id로 표현
        read_only_fields = ('author', 'created_at')


    def get_author_username(self, obj):
        '''
        get_author_username 함수가 serializers.SerializerMethodField()의 반환값이 되어author_username 에 삽입
        Django REST Framework는 해당 필드에 대한 값을 얻기 위해 get_<field_name> 형식의 메서드를 호출
        '''
        return obj.author.username
    
    def create(self, validated_data):
        '''
        CommentSerializer의 create() 메서드를 오버라이딩
        author를 현재 로그인한 유저로 설정
        '''
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)



class PostSerializer(serializers.ModelSerializer):
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='posts/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    '''

    author_username = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()


    class Meta:
        '''
        author_username, comments, like_count, is_liked는 PostSerializer에서 직접 정의한 필드
        '''
        model = Post
        fields = ['id', 'author', 'author_username', 'content', 'image', 'created_at', 'comments', 'like_count', 'is_liked']
        read_only_fields = ('author', 'created_at', 'updated_at')

    
    def get_author_username(self, obj):
        return obj.author.username
    
    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.likes.filter(author=user).exists()
        return False