from django.db import models
from django.utils.text import slugify
from authentication.models import Participant
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
class POST(models.Model):
    author = models.ForeignKey(Participant,  on_delete=models.CASCADE, related_name="posts_authored")
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    mentions = models.ManyToManyField( Participant, related_name="mentioned_in_posts", blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1

            while POST.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Profile(models.Model):
    user = models.OneToOneField(Participant, on_delete=models.CASCADE )
    bio = models.TextField()
    image = models.ImageField(upload_to="profiles/")
