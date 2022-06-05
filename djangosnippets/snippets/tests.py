from django.test import TestCase
from django.http import HttpRequest
from snippets.views import top  #これから実装するビュー関数(今はまだ存在しません)


class TopPageViewTest(TestCase):
    """View関数のテスト
    """
    def test_top_returns_200(self):
        request = HttpRequest()  # HttpRequest オブジェクトの作成
        response = top(request)
        self.assertEqual(response.status_code,200)


    def test_top_returns_expected_content(self):
        request=HttpRequest()  # HttpRequestオブジェクトの作成
        response = top(request)
        self.assertEqual(response.content, b"HelloWorld")


class TopPageTest(TestCase):
    """ルーティングのテスト
    """
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"HelloWorld")
