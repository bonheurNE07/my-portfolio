from django.db import models
from cloudinary.models import CloudinaryField
from core.mixins import TimeStampedModel
from .manager import ProjectManager

class Project(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    repo_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image = CloudinaryField('image', folder='portfolio')

    objects = ProjectManager()

    def __str__(self):
        """
        Project string representation using its title.
        
        Returns:
            str: The project's title used as its string representation.
        """
        return self.title