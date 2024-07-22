from news.models import User
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

from news.models import Author
Author.objects.create(author=user1)
Author.objects.create(author=user2)

from news.models import Category
Category.objects.create(CategoryName='gaming')
Category.objects.create(CategoryName='music')
Category.objects.create(CategoryName='technology')
Category.objects.create(CategoryName='art')

from news.models import Post
author = Author.objects.get(id=1)
Post.objects.create(post_author=author, post_type='A', title='Kanye West', content='Text about all Kanye West albums')
Post.objects.create(post_author=author, post_type='A', title='Clash Royal', content='negative comments about Clash Royal')
Post.objects.create(post_author=author, post_type='N', title='New Crypto App', content='News about Crypto App')
Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=1).post_category.add(Category.objects.get(id=4))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=1))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=3))
Post.objects.get(id=3).post_category.add(Category.objects.get(id=3))

from news.models import Comment
Comment.objects.create(comment_author=Author.objects.get(id=1).author, comment_post=Post.objects.get(id=1), comment='Trash music')
Comment.objects.create(comment_author=Author.objects.get(id=2).author, comment_post=Post.objects.get(id=1), comment='SUPER ULTRA SWAG')
Comment.objects.create(comment_author=Author.objects.get(id=1).author, comment_post=Post.objects.get(id=2), comment='dont post on this board ever')
Comment.objects.create(comment_author=Author.objects.get(id=2).author, comment_post=Post.objects.get(id=3), comment='MONEY MONEY MONEY')

Comment.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=3).like()
Post.objects.get(id=2).dislike()

u1 = Author.objects.get(id=1)
u1.update_rating()
u2 = Author.objects.get(id=2)
u2.update_rating()

winner = Author.objects.order_by('rating')
for i in winner:
    i.rating
    i.author.username

post = Post.objects.order_by('-post_rating')
for i in post[:1]:
    i.creation_date
    i.post_author.author
    i.post_rating
    i.title
    i.preview()

Post.objects.all().order_by('-post_rating')[0].comment_set.values(
    'comment_creation_date',
    'comment_author',
    'comment_rating',
    'comment',
)
