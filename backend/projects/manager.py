from django.db import models

class ProjectQuerySet(models.QuerySet):
    def featured(self):
        return self.filter(is_featured=True)

class ProjectManager(models.Manager):
    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().featured()