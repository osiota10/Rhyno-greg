from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.views import generic
from .forms import ContactForm, EmailSubscriptionForm, QuotationForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.views.generic.list import ListView


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


class ServicesView(generic.ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'services.html'
    paginate_by = 6


class ServicesDetailView(generic.DetailView):
    model = Service
    context_object_name = 'services'
    template_name = 'services-detail.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class ProjectsView(generic.ListView):
    model = OurProject
    context_object_name = 'Projects'
    template_name = 'projects.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectsView, self).get_context_data(*args, **kwargs)
        projects_list = OurProject.objects.all()
        project_status = OurProject.STATUS

        # unpacking with zip
        _,  res = zip(*project_status)
        print(res)
        context['completed_project'] = projects_list.filter(status='Completed')
        context['in_dev_project'] = projects_list.filter(status='In Development')
        context['project_status'] = res
        return context


class ProjectsDetailView(generic.DetailView):
    model = OurProject
    context_object_name = 'Projects'
    template_name = 'projects-detail.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class TestimonialView(generic.ListView):
    model = Testimonial
    context_object_name = 'testimonials'
    template_name = 'testimonials.html'
    paginate_by = 6


def projects_categories_view(request, cats):
    cat_post = JobCategory.objects.filter(name=cats)
    all_cat_posts = OurProject.objects.filter(category__name__icontains=cats)

    # paginator
    paginator = Paginator(all_cat_posts, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {'cats': cats, 'cat_post': cat_post, 'page_obj': page_obj}
    return render(request, 'project-categories.html', context)


class ProjectStatusView(ListView):
    model = OurProject
    template_name = 'project-status.html'
    context_object_name = 'Projects'
    paginate_by = 6

    def get_queryset(self):
        status = self.kwargs['status']
        qs = OurProject.objects.filter(status__icontains=status)
        print(status)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectStatusView, self).get_context_data(*args, **kwargs)
        context['status'] = self.kwargs['status']

        projects_list = OurProject.objects.all()
        project_status = OurProject.STATUS

        # unpacking with zip
        _, res = zip(*project_status)
        print(res)
        context['project_status'] = res
        return context


def contact(request):
    return render(request, 'contact.html')


def thank_you(request):
    return render(request, 'thank-you.html')


def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def terms_and_conditions(request):
    return render(request, 'terms-and-conditions.html')


def company_info(request):
    info = CompanyInformation.objects.all()
    core_value = CoreValue.objects.all()
    service_list = Service.objects.all()
    testimonial_list = Testimonial.objects.all()
    projects_list = OurProject.objects.all()
    completed_project_list = projects_list.filter(status='Completed')
    in_dev_project_list = projects_list.filter(status='In Development')
    job_categories = JobCategory.objects.all()
    company_data = CompanyInformation.objects.all()
    clients = OurClient.objects.all()
    value_statement = CoreValue.objects.all()
    stat = Stat.objects.all()
    certification = CertificationsAndAward.objects.all()
    socials = SocialMediaHandle.objects.all()

    # All forms handling
    if request.method == 'POST':
        if request.POST.get("form_type") == 'ContactForm':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "Ryhno-greg Quick Contact"
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                with open(settings.BASE_DIR / "templates/ContactForm/ContactFormEmailMsg.txt") as msg:
                    contact_msg = msg.read()
                try:
                    message = EmailMultiAlternatives(subject=subject, body=contact_msg,
                                                     from_email=settings.EMAIL_HOST_USER, to=[email],
                                                     headers={'name': name})
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                form.save()
                html_template = get_template("ContactForm/ContactFormEmailMsg.html").render({'name': name})
                message.attach_alternative(html_template, "text/html")
                message.send()

                messages.success(request, 'Contact Details Captured')

        elif request.POST.get("form_type") == 'SubscriptionForm':
            form = EmailSubscriptionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Email Details Captured')

        elif request.POST.get("form_type") == 'QuotationForm':
            form = QuotationForm(request.POST)
            if form.is_valid():
                subject = "Ryhno-greg- Quotation Request"
                subject2 = "Notification- Quotation Request"
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                with open(settings.BASE_DIR / "templates/ContactForm/ContactFormEmailMsg.txt") as msg:
                    contact_msg = msg.read()
                try:
                    message = EmailMultiAlternatives(subject=subject, body=contact_msg,
                                                     from_email=settings.EMAIL_HOST_USER, to=[email],
                                                     headers={'name': name})
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                form.save()
                html_template = get_template("QuotationForm/QuotationFormEmailMsg.html").render({'name': name})
                message.attach_alternative(html_template, "text/html")
                message.send()
                messages.success(request, 'Quotation Recieved')

    storage = messages.get_messages(request)
    context = {'info': info, 'core_value': core_value, 'service_list': service_list,
               'testimonial_list': testimonial_list, 'projects_list': projects_list,
               'completed_project_list': completed_project_list, 'in_dev_project_list': in_dev_project_list,
               'storage': storage, 'job_categories': job_categories, 'company_data': company_data, 'clients': clients,
               'value_statement': value_statement, 'stat': stat, 'certification': certification, 'socials': socials}
    return context
