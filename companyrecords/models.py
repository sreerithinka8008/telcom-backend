from django.db import models

# Company
class Company(models.Model):
    class Status(models.TextChoices):
        Active = "Active", "Active"
        Inactive = "Inactive", "Inactive"
        Junk = "Junk", "Junk"
        Hot = "Hot", "Hot"
        New = "New", "New"
    
    class TechnicalDetails(models.TextChoices):
        TestPassed = "Test Passed", "Test Passed"
        TestInitiated = "Test Initiated", "Test Initiated"
        TestFail = "Test Fail", "Test Fail"
        Pending = "Pending", "Pending"
    
    class Priority(models. TextChoices):
        High = "High", "High"
        Medium = "Medium", "Medium"
        Low = "Low", "Low"
    
    class UserType(models.TextChoices):
        Client = "Client", "Client"
        Vendor = "Vendor", "Vendor"

    company_name = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=250)
    company_email = models.EmailField()
    company_website = models.CharField(max_length=250, default=None, null=True, blank=True)
    country = models.CharField(max_length=250)
    company_phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    support_email = models.EmailField()
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.New)
    technical_details = models.CharField(max_length=50, choices=TechnicalDetails.choices, default=TechnicalDetails.TestInitiated)
    priority = models.CharField(max_length=50, choices=Priority.choices,  default=Priority.Medium)
    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.Client)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Companies"


    def __str__(self):
        return self.company_name
    
# Switch I.P.
class SwitchIP(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    ip = models.CharField(max_length=250, unique=True)
    is_deleted = models.BooleanField(default=False)


# Follow Up
class FollowUp(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    message = models.TextField()
    is_deleted = models.BooleanField(default=False)