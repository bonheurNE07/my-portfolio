from django.db import models

class ProjectQuerySet(models.QuerySet):
    def featured(self):
        """
        Return a queryset containing objects marked as featured.
        
        Returns:
            QuerySet: A queryset of objects where `is_featured` is True.
        """
        return self.filter(is_featured=True)

class ProjectManager(models.Manager):
    def get_queryset(self):
        """
        Create a ProjectQuerySet bound to the manager's model and database alias.
        
        Returns:
            ProjectQuerySet: A queryset instance for this manager's model using the manager's database connection.
        """
        return ProjectQuerySet(self.model, using=self._db)

    def featured(self):
        """
        Return a queryset of this manager's model filtered to featured projects.
        
        Returns:
            QuerySet: A queryset containing objects where `is_featured` is True.
        """
        return self.get_queryset().featured()