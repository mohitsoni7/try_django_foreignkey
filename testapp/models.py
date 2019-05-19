from django.db import models


class NFCTag(models.Model):
    name = models.CharField(max_length=100)
    tag_no = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True, related_name='tag_creator')
    whose_tag = models.OneToOneField('Employee', on_delete=models.CASCADE, null=True, blank=True, related_name='whose_tag')


    def __str__(self):
        return(self.name + ': ' + self.tag_no)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True, related_name='emp_creator')

    def __str__(self):
        return(self.name)
