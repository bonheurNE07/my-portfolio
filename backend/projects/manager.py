from django.db import models

class ProjectQuerySet(models.QuerySet):
    def featured(self):
        """
        Filter the queryset to objects marked as featured.
        
        Returns:
            QuerySet: Objects from the queryset where `is_featured` is True.
        """
        return self.filter(is_featured=True)

class ProjectManager(models.Manager):
    def get_queryset(self):
        """
        Produce a ProjectQuerySet instance bound to this manager's model and database alias.
        
        Returns:
            ProjectQuerySet: A queryset instance configured with this manager's model and using the manager's database alias.
        """
        return ProjectQuerySet(self.model, using=self._db)

    def featured(self):
        """
        Retrieve a queryset of projects marked as featured.
        
        Returns:
            QuerySet: A queryset of the manager's model instances where `is_featured` is `True`.
        """
        return self.get_queryset().featured()