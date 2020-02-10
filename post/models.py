from django.db import models
from django.contrib.auth import get_user_model
from post.validators.validate_title import validate_title
from post.validators.validate_name import validate_name


class Category(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, validators=[validate_title])
    thumbnail = models.ImageField(
        upload_to='thumbnails', blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.title) > 20:
            return "{}'s post {}...".format(self.author, self.title)
        return "{}'s post {}...".format(self.author, self.title)

    @property
    def get_comments(self):
        return self.comments.filter(parent_id__isnull=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.title = str(self.title).title()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
