from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    author = models.OneToOneField(User, related_name="custom_user", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        sum_rating = self.post_set.aggregate(post_rate=Sum('post_rating'))
        result_sum_rating = 0
        try:
            result_sum_rating += sum_rating.get('post_rate')
        except TypeError:
            result_sum_rating = 0

        sum_comment_rating = self.author.comment_user.aggregate(comment_rate=Sum('comment_rating'))
        result_sum_comment_rating = 0
        result_sum_comment_rating += sum_comment_rating.get('comment_rate')

        self.rating = result_sum_rating * 3 + result_sum_comment_rating
        self.save()

class Category(models.Model):
    CategoryName = models.CharField(max_length=255, unique=True)

class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'N'
    ARTICLE = 'A'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )

    post_type = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default=ARTICLE)
    creation_date = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()
    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.content[:124]+'...'

class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete=models.CASCADE)
    cat_category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE)
    comment = models.TextField()
    comment_creation_date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()
    def dislike(self):
        self.comment_rating -= 1
        self.save()