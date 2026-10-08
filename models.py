from django.db import models
from api.models import TimeStampedModel
from organisations.models import Organisation, Facility

class Patient(TimeStampedModel):
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT, related_name='patients')
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT, related_name='patients')
    patient_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['organisation','patient_number'], name='unique_patient_number_per_org')]
    def __str__(self): return f'{self.first_name} {self.last_name}'.strip()
