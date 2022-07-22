from django.contrib import admin
from .models import *


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "email", "category", "phone_number")
    list_filter = ('date',)


class EmailSubAdmin(admin.ModelAdmin):
    list_display = ("date", "email")
    list_filter = ('date',)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "testimony")
    list_filter = ('name',)


class RequestForQuotationAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "email", "category", "phone_number")
    list_filter = ('date',)


admin.site.register(CompanyInformation)
admin.site.register(OurClient)
admin.site.register(CertificationsAndAward)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(EmailSubscription, EmailSubAdmin)
admin.site.register(CoreValue)
admin.site.register(Service)
admin.site.register(ThankYouMessage)
admin.site.register(JobCategory)
admin.site.register(OurProject)
admin.site.register(ProjectImage)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(RequestForQuotation, RequestForQuotationAdmin)
admin.site.register(Stat)
admin.site.register(SocialMediaHandle)
