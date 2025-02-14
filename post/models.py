from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Yazar", related_name='posts')
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayımlanma Tarihi", auto_now_add=True)
    image = models.FileField(blank=True, null=True, verbose_name="Resim")
    checked = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title
    
       

    def get_comment_count(self):
        count = Comment.objects.filter (post_id = self.id).count()
        return count
    
    def get_son_yorum_tarihi(self):
        son = Comment.objects.filter (post_id = self.id).first().publishing_date
        return son        
    
    def get_absolute_url(self):
        return reverse('postt:detail', kwargs={'slug': self.slug})
    
    def get_create_url(self):
        return reverse('postt:create')
    
    def get_update_url(self):
        return reverse('postt:update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('postt:delete', kwargs={'slug': self.slug})
    
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    
    def save(self, *args, **kwargs):        
        self.slug = self.get_unique_slug()
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-publishing_date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, verbose_name="İsim")
    content = models.TextField(verbose_name="Yorum")
    publishing_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-publishing_date']