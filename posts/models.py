from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    published_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        original_slug = self.slug
        queryset = Post.objects.filter(slug=self.slug)

        if self.pk:
            queryset = queryset.exclude(pk=self.pk)

        counter = 2
        while queryset.exists():
            self.slug = f"{original_slug}-{counter}"
            queryset = Post.objects.filter(slug=self.slug)
            counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
