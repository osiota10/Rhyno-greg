from django.db.models.signals import pre_save, post_save
from django.http import HttpResponse

from .models import Service, OurProject, ContactUs, RequestForQuotation
from .utils import unique_slug_generator
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.core.signals import request_finished


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Service)
pre_save.connect(slug_generator, sender=OurProject)


def contact_form_alert(sender, instance, created, **kwargs):
    if created:
        subject = "Contact Form Notification at Rhyno-greg"
        name = instance.name
        number = instance.phone_number
        message_instance = instance.message
        email = instance.email

        with open(settings.BASE_DIR / "templates/ContactForm/ContactFormEmailMsg.txt") as msg:
            contact_msg = msg.read()
        try:
            message = EmailMultiAlternatives(subject=subject, body=contact_msg,
                                             from_email=settings.EMAIL_HOST_USER, to=[settings.EMAIL_HOST_USER],
                                             headers={'name': name, 'email': email, 'number': number,
                                                      'message': message_instance})
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        html_template = get_template("ContactForm/adminContactNotification.html").render(
            {'name': name, 'email': email, 'number': number, 'message': message_instance})
        message.attach_alternative(html_template, "text/html")
        message.send()


def quotation_form_alert(sender, instance, created, **kwargs):
    if created:
        subject = "Quotation Form Notification at Rhyno-greg"
        name = instance.name
        number = instance.phone_number
        message_instance = instance.brief_description
        email = instance.email
        location = instance.location
        attach_file = instance.attach_file

        with open(settings.BASE_DIR / "templates/QuotationForm/adminQuotationNotification.txt") as msg:
            contact_msg_1 = msg.read()
        try:
            message1 = EmailMultiAlternatives(subject=subject, body=contact_msg_1,
                                              from_email=settings.EMAIL_HOST_USER, to=[settings.EMAIL_HOST_USER],
                                              headers={'name': name, 'email': email, 'number': number,
                                                       'message': message_instance, 'location': location,
                                                       'attach_file': attach_file})
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        html_template = get_template("QuotationForm/adminQuotationNotification.html").render(
            {'name': name, 'email': email, 'number': number, 'message': message_instance, 'location': location,
             'attach_file': attach_file})
        message1.attach_alternative(html_template, "text/html")
        message1.send()


post_save.connect(quotation_form_alert, sender=RequestForQuotation, dispatch_uid='quotation')
post_save.connect(contact_form_alert, sender=ContactUs, dispatch_uid='contact_us')

request_finished.connect(quotation_form_alert, sender=RequestForQuotation, dispatch_uid='quotation')
request_finished.connect(contact_form_alert, sender=ContactUs, dispatch_uid='contact_us')