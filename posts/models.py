from django.db import models

# Create your models here.
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Entry(models.Model):
    #Title, Body, Created, Modified, Slug
    title = models.CharField(max_length = 100)
    body = models.TextField(blank = True)
    slug = models.SlugField(max_length = 200, unique = True)
    published = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.slug
    
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]








