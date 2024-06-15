from django.db import models
from accounts.models import User

class Benefactor(models.Model):
    EXPERIENCE_CHOICES = (
        (0, 'مبتدی'),
        (1, 'متوسط'),
        (2, 'متخصص')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES,
                                          default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)




class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return Task.objects.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return Task.objects.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return Task.objects.filter(Q(state__exact="P") |
                                    Q(charity__user=user) |
                                    Q(assigned_benefactor__user=user))







class Task(models.Model):
    GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male")
    )

    STATE_CHOICES = (
        ("P", "Pending"),
        ("W", "Waiting"),
        ("A", "Assigned"),
        ("D", "Done")
    )
    assigned_benefactor = models.ForeignKey(Benefactor,
                                            models.SET_NULL,
                                            blank=True,
                                            null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    gender_limit = models.CharField(max_length=1,
                                    blank=True,
                                    choices=GENDER_CHOICES)
    state = models.CharField(max_length=1,
                             default="P",
                             choices=STATE_CHOICES)
    title = models.CharField(max_length=60)
    objects = TaskManager()