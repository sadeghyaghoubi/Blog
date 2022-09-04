from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post


class BlogPostTest(TestCase):
#############setUpTestData###############
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Post1',
            text='This is the description of post1',
            status=Post.STATUS_CHOICE[0][0],
            author=cls.user,
        )
        cls.post1 = Post.objects.create(
            title='Post2',
            text='lorem ipsum post 2 ',
            status=Post.STATUS_CHOICE[1][0],  # draft
            author=cls.user,
        )

#############setUp###############
# def setUp(self):
#     self.user = User.objects.create(username='user1')
#     self.post1 = Post.objects.create(
#         title='Post1',
#         text='This is the description of post1',
#         status=Post.STATUS_CHOICE[0][0],
#         author=self.user,
#     )
#     self.post1 = Post.objects.create(
#         title='Post2',
#         text='lorem ipsum post 2 ',
#         status=Post.STATUS_CHOICE[1][0], #draft
#         author=self.user,
#     )


#barresi inke hatman esme posti ke to admin namayesh mide hatman title bashe (yani age beja title biad bege text namayesh bede in khata mikhore)
def test_post_model_str(self):
    post = self.post1
    self.assertEqual(str(post), post.title) #string post ba title barabar hast ya na ?


##barresi khode URL : agar to url aslie proje esmesh taghir kone in khata mide
def test_post_list_url(self):
    response = self.client.get('/blog/')
    self.assertEqual(response.status_code, 200)


##agar esme url taghir kone inja khata mide
def test_post_list_url_by_name(self):
    response = self.client.get(reverse('posts_list'))
    self.assertEqual(response.status_code, 200)


###barresi khode URL : agar to url aslie proje esmesh taghir kone in khata mide
def test_post_detail_url(self):
    response = self.client.get(f'/blog/{self.post1.id}/')
    self.assertEqual(response.status_code, 200)


##agar esme url taghir kone inja khata mide
def test_post_detail_url_by_name(self):
    response = self.client.get(reverse('post_detail', args=[self.post1.id]))
    self.assertEqual(response.status_code, 200)


##barresi joziate safhe asli mesle title , text
def test_post_details_on_blog_detail_page(self):
    response = self.client.get(reverse('post_detail', args=[self.post1.id]))
    self.assertContains(response, self.post1.title)
    self.assertContains(response, self.post1.text)


##barresi ID ke vojood nadare
def test_status_404_if_post_id_not_exist(self):
    response = self.client.get(reverse('post_detail', args=[999]))
    self.assertEqual(response.status_code, 404)


#draft ha namayesh dade nashe
def test_draft_post_not_show_in_posts_list(self):
    response = self.client.get(reverse('posts_list'))
    self.assertContains(response, self.post1.title)
    self.assertNotContains(response, self.post2.title)

#barresi create post jadid
def post_test_create_view(self):
    response = self.client.post(reverse('post_create'), {
        'title': 'Some Title',
        'text': 'This is some text',
        'status': 'pub',
        'author': self.user.id,
    })
    self.asserEqual(response.status_code, 302) #302 :create beshe ino mide (redirect)
    self.asserEqual(Post.objects.last().title, 'Some Title') #.last yani akharin chizi ke vojood dare
    self.asserEqual(Post.objects.last().text, 'This is some text')


#barresi update post
def post_test_update_view(self):
    response = self.client.post(reverse('post_update', args=[self.post2.id]), {
        'title': 'Post2 Updated',
        'text': 'This is  text Update',
        'status': 'pub',
        'author': self.post2.author.id,
    })
    self.asserEqual(response.status_code, 302) #302 :create beshe ino mide (redirect)
    self.asserEqual(Post.objects.last().title, 'Post2 Updated')
    self.asserEqual(Post.objects.last().text, 'This is  text Update')


def post_test_delete_view(self):
    response = self.client.post(reverse('post_delete', args=[self.post2.id]))
    self.asserEqual(response.status_code, 302) #302 :create beshe ino mide (redirect)


