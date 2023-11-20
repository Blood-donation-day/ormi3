from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
import requests

# Create your tests here.
        #  글쓰기, 글수정
class Test(TestCase):
    def setUp(self):
        '''
        유저 생성
        '''
        
        self.client = Client()
        self.user_test = User.objects.create_user(
            username='test1',
            password='test1',
        )
    
    def test_post_list(self):
        
        print('--- /notice 페이지 접속확인 -----')
        response = self.client.get('/notice/')

        
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print('--- /notice 페이지 접속성공 -----')
        else:
            print('--- /notice 페이지 에러 -----')

           
    def test_post_detail(self):
        
        print('--- /notice 상세글 페이지 확인 -----')
        
        post_001 = Post.objects.create(
            title = '샘플 제목1',
            content = '샘플 작성글',
            author = self.user_test,
        )
        post_002 = Post.objects.create(
            title = '샘플 제목1',
            content = '샘플 작성글',
            author = self.user_test,
        )
        
        response = self.client.get('/notice/1/')
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print('--- /notice 상세글 페이지 성공 -----')
        else:
            print('--- /notice 상세글 페이지 에러 -----')
    
    def test_post_create(self):
        '''
        request.user가 있는 경우에 글을 작성할 수 있습니다.
        익명 사용자의 경우 status_code 403을 출력합니다.
        '''
        
        