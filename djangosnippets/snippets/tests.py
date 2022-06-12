from turtle import title
from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit, snippet_detail
from django.contrib.auth import get_user_model #get_user_modelをインポート
from django.test import TestCase, Client, RequestFactory #RequestFactoryをインポート
from snippets.models import Snippet


UserModel = get_user_model()

# class TopPageViewTest(TestCase):
#     """View関数のテスト
#     """
#     def test_top_returns_200(self):
#         request = HttpRequest()  # HttpRequest オブジェクトの作成
#         response = top(request)
#         self.assertEqual(response.status_code, 200)

#     def test_top_returns_expected_content(self):
#         request=HttpRequest()  # HttpRequestオブジェクトの作成
#         response = top(request)
#         self.assertEqual(response.content, b"HelloWorld")

class TopPageTemplateTest(TestCase):
    """テンプレートのテスト
    """
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Djangoスニペット", status_code=200)
    
    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "snippets/top.html")


class TopPageTest(TestCase):
    """ルーティングのテスト
    """
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    # def test_top_returns_expected_content(self):
    #     response = self.client.get("/")
    #     self.assertEqual(response.content, b"HelloWorld")


class TopPageRenderSnippetsTest(TestCase):
    """データベース読み出し表示のテスト
    """
    def setUp(self):
        self.user=UserModel.objects.create(
            username = "test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet = Snippet.objects.create(
            title="title1",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )
    
    def test_should_return_snippet_title(self):
        request=RequestFactory().get("/")
        request.user=self.user
        response=top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request=RequestFactory().get("/")
        request.user=self.user
        response=top(request)
        self.assertContains(response, self.user.username)


class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user",
            email = "test@example.com",
            password = "secret",
        )
        self.client.force_login(self.user)  # ユーザーログイン

    def test_render_creation_form(self):
        response = self.client.get("/snippets/new/")
        self.assertContains(response, "スニペットの登録", status_code=200)

    def test_create_snippet(self):
        data = {'title': 'タイトル', 'code': 'コード', 'description': '解説'}
        self.client.post("/snippets/new/", data)
        snippet = Snippet.objects.get(title='タイトル')
        self.assertEqual('コード', snippet.code)
        self.assertEqual('解説', snippet.description)

    def test_should_resolve_snippet_new(self):
        found = resolve("/snippets/new/")
        self.assertEqual(snippet_new, found.func)


class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user=UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
            )
        self.snippet=Snippet.objects.create(
            title="タイトル",
            code="コード",
            description="解説",
            created_by=self.user,
            )

    def test_should_use_expected_template(self):
        response=self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response, "snippets/snippet_detail.html")
        
    def test_top_page_returns_200_and_expected_heading(self):
        response=self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(response,self.snippet.title, status_code=200)

    def test_should_resolve_snippet_detail(self):
        found = resolve("/snippets/1/")
        self.assertEqual(snippet_detail, found.func)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, found.func)
