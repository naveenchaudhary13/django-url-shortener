from django.views.generic import TemplateView
from django.shortcuts import render
from shortener.models import ShortURL


class HistoryView(TemplateView):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "history.html", {"unauth": True})
        user_urls = ShortURL.objects.filter(user=request.user).order_by('-created_at')
        return render(request, "history.html", {"urls": user_urls})
