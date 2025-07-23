from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from shortener.forms import ShortURLForm
from shortener.models import ShortURL
from utils.helpers import generate_short_code, get_short_url


class HomeView(TemplateView):
    """
        Represent the home page.
        
        This class based view is responsible for rendering the home page.
        It also handles the POST request to shorten the URL.
        
        Attributes:
            template_name (str): The name of the template to render.
        
        Methods:
            get_context_data: 
                Add the form to the context data.
                This method is called when the view is instantiated.
            post:
                Handle the POST request to shorten the URL.
                It validates the form, creates the ShortURL object and renders the HTML for the shortened URL.
                If the form is invalid, it renders the HTML for the error messages.
    """
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ShortURLForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ShortURLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            short_code = generate_short_code()
            expires_at = timezone.now() + timedelta(days=7)
            obj = ShortURL.objects.create(
                long_url=long_url, 
                short_code=short_code, 
                expires_at=expires_at,
                user=request.user if request.user.is_authenticated else None
            )
            short_url = get_short_url(request, obj.short_code)

            html = render_to_string("partials/shortened_url.html", {'short_url': short_url, 'obj': obj}, request=request)
            return JsonResponse({
                'success': True, 
                'html': html,
                'message': "URL shortened successfully!",
                'type': "success"
            })
        
        return JsonResponse({
            'success': False, 
            'message': "Invalid URL. Try again.",
            'type': "error"
        })


class URLRedirectView(View):
    """
        Represent the URL redirect view.
        
        This class based view is responsible for redirecting the user to the original long URL.
        
        Attributes:
            template_name (str): The name of the template to render.
        
        Methods:
            get:
                Redirect the user to the original long URL.
    """
    def get(self, request, shortcode):
        obj = get_object_or_404(ShortURL, short_code=shortcode)
        
        if obj.is_expired():
            return HttpResponse("⚠️ This link has expired.", status=410)
        
        obj.click_count += 1
        obj.save(update_fields=["click_count"])
        return redirect(obj.long_url)