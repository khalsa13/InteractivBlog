from django import forms
from .models import Post
from django.utils.text import slugify
import itertools


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","content","image"]

    def save(self,commit=True):
        instance = super(PostForm, self).save(commit=False)

        instance.slug = orig = slugify(instance.title)

        for x in itertools.count(1):
            if not Post.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)

        instance.save()

        return instance