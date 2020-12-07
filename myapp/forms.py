from django import forms
from .models import blog_post
from .views import blog
class PostForm(forms.ModelForm):
    class Meta:
        model = blog_post
        fields = ('post_title', 'post_text')

        
    def __init__(self,*args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        
        self.fields['post_title'].widget.attrs['class']= 'form-control'
        self.fields['post_text'].widget.attrs['class']='form-control'
