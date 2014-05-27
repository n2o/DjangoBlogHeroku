from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from blogengine.models import Post

class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()


class FlatPageViewTest(BaseAcceptanceTest):
    def test_create_flat_page(self):
        # Create flat page
        page = FlatPage()
        page.url = '/about/'
        page.title = 'About me'
        page.content = 'All about me'
        page.save()

        # Add the site
        page.sites.add(Site.objects.all()[0])
        page.save()

        # Check new page saved
        all_pages = FlatPage.objects.all()
        self.assertEquals(len(all_pages), 1)
        only_page = all_pages[0]
        self.assertEquals(only_page, page)

        # Check data correct
        self.assertEquals(only_page.url, '/about/')
        self.assertEquals(only_page.title, 'About me')
        self.assertEquals(only_page.content, 'All about me')

        # Get URL
        page_url = only_page.get_absolute_url()

        # Get the page
        response = self.client.get(page_url)
        self.assertEquals(response.status_code, 200)

        # # Check title and content in response
        # self.assertTrue('About me' in response.content)
        # self.assertTrue('All about me' in response.content)


class PostTest(TestCase):
    def test_create_post(self):
        post = Post()
        post.title = "My first post"
        post.text = "This is my first blog post"
        post.pub_date = timezone.now()
        post.save()

        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Check attributes
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEquals(only_post.pub_date.second, post.pub_date.second)


class AdminTest(BaseAcceptanceTest):
    fixtures = ['users.json']

    def test_login(self):
        # Get login page
        response = self.client.get('/admin/')

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Log the user in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

    def test_create_post(self):
        # Log in
        self.client.login(username='bobsmith', password='password')
