from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
import time
class Test(TestCase):
    # def setUp(self):
    #     print('-- blog app 테스트 --')

    def test_connect(self):
        print('-- 접속확인 테스트 --')
        self.client = Client()
        
        print('-- /about 페이지 접속확인 --')
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        header = soup.header
        body = soup.body
        footer = soup.footer
        
        self.assertIsNotNone(header)
        self.assertIsNotNone(body)
        self.assertIsNotNone(footer)
        
        
        print('-- /contact 페이지 접속확인 --')
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        header = soup.header
        body = soup.body
        footer = soup.footer
        
        self.assertIsNotNone(header)
        self.assertIsNotNone(body)
        self.assertIsNotNone(footer)
        
        print('-- /blog 페이지 접속확인 --')
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        header = soup.header
        body = soup.body
        footer = soup.footer
        
        self.assertIsNotNone(header)
        self.assertIsNotNone(body)
        self.assertIsNotNone(footer)
        
    def test_postlist(self):
        print('-- 게시물 리스트 확인 --')
        
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        if Post.objects.count() == 0:
            # content >> list형식으로 들어옴
            content = soup.select('.contents-text')
            self.assertIn('게시물이 존재하지 않습니다. 첫번째 게시물에 주인공이 되세요!', content[0].text)
        
        print('-- 게시물 생성 --')
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World. We are the world.',
        )
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content = soup.body.select('h2')
        print('h2태그 갯수: ', len(content))
        self.assertGreater(len(content), 0)
        
    
    
    def test_postdetail(self):
        print('-- 게시물 상세 페이지 확인 --')

        response = self.client.get('/blog/1')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.select('.contents-heading')
        print(title)


# Create your tests here.
