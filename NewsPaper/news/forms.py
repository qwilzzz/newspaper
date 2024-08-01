from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_author','title', 'post_type', 'post_category', 'content']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['post_author'].label = 'Автор:'
        self.fields['title'].label = 'Заголовок:'
        self.fields['post_type'].label = 'Тип публикации:'
        self.fields['post_category'].label = 'Категории:'
        self.fields['content'].label = 'Текст публикации:'