from django.db import models

NULL_BLANK = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title',)
    slug = models.SlugField(max_length=100, verbose_name='Slug', **NULL_BLANK,)
    content = models.TextField(verbose_name='Content', **NULL_BLANK,)
    image = models.ImageField(upload_to='blog/', verbose_name='Image Preview', **NULL_BLANK, )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created',)
    date_uploaded = models.DateTimeField(auto_now=True, verbose_name='Date Uploaded',)

    views_count = models.IntegerField(default=0, verbose_name='Views Count',)
    is_published = models.BooleanField(default=True, verbose_name='Is Published',)

    def __str__(self):
        return f"{self.title} {self.content} {self.date_created} {self.date_uploaded} {self.views_count}"

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('title', 'content', 'date_created', 'date_uploaded', 'views_count',)
