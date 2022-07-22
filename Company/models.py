from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class CompanyInformation(models.Model):
    logo = CloudinaryField()
    page_header_image = CloudinaryField()
    company_name = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=50, null=True, blank=True)
    CAC_number = models.CharField(max_length=15)
    email = models.EmailField()
    telephone = models.CharField(max_length=11)
    telephone_2 = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    about_page_image = CloudinaryField(null=True, blank=True)
    about = RichTextField()
    contact_page_image = CloudinaryField()
    terms_and_conditions = RichTextField()
    privacy_policy = RichTextField()

    class Meta:
        verbose_name_plural = "Company Information"

    def __str__(self):
        return f"{self.company_name}-{self.CAC_number}"


class OurClient(models.Model):
    name = models.CharField(max_length=100)
    logo = CloudinaryField()

    def __str__(self):
        return f"{self.name}"


class CertificationsAndAward(models.Model):
    name = models.CharField(max_length=100)
    logo = CloudinaryField()

    def __str__(self):
        return f"{self.name}"


class Testimonial(models.Model):
    photo = CloudinaryField(null=True, blank=True)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=25)
    testimony = RichTextField()

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/Images/profile.svg"

    def __str__(self):
        return f"{self.name}-{self.designation}"


class EmailSubscription(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"


class CoreValue(models.Model):
    font_awesome_class = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    message = RichTextField()

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    pic = CloudinaryField('image')
    slug = models.SlugField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=50)
    snippet = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class ThankYouMessage(models.Model):
    pic = CloudinaryField('image')
    title = models.CharField(max_length=50)
    snippet = RichTextField()

    def __str__(self):
        return f"{self.title}"


class JobCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Job Categories"

    def __str__(self):
        return f"{self.name}"


class OurProject(models.Model):
    STATUS = [
        ('Completed', 'Completed'),
        ('In Development', 'In Development')
    ]

    date = models.DateField()
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    description = RichTextField()
    # location = models.CharField(max_length=100, blank=True, null=True, default='Asaba')
    category = models.ForeignKey(JobCategory, on_delete=models.CharField)
    status = models.CharField(max_length=20, choices=STATUS, blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.status}"


class ProjectImage(models.Model):
    project_name = models.ForeignKey(OurProject, on_delete=models.CharField)
    image = CloudinaryField()

    def __str__(self):
        return f"{'Image for '}-{self.project_name}"


class ContactUs(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    category = models.ForeignKey(JobCategory, on_delete=models.CharField)
    phone_number = models.CharField(max_length=11)
    message = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name}-{self.phone_number}"


class RequestForQuotation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50)
    category = models.ForeignKey(JobCategory, on_delete=models.CharField)
    phone_number = models.CharField(max_length=11)
    brief_description = RichTextField()
    attach_file = CloudinaryField(blank=True, null=True)  # take note

    def __str__(self):
        return f"{self.name}-{self.phone_number}-{self.location}"


class Stat(models.Model):
    font_awesome_class = models.CharField(max_length=30)
    stat_figure = models.IntegerField()
    stat_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.stat_title}-{self.stat_figure}"


class SocialMediaHandle(models.Model):
    font_awesome_class = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.name}"
