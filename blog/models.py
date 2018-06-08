from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    created_date = models.DateField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=False)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        flag = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,flag)
            flag += 1
            return unique_slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
