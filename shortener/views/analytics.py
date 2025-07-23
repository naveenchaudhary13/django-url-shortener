from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.models import User
from django.utils.timezone import now
from shortener.models import ShortURL


class AnalyticsView(TemplateView):
    template_name = "analytics.html"

    def get(self, request):
        urls = ShortURL.objects.all()
        total_clicks = urls.aggregate(total=Sum('click_count'))['total'] or 0
        total_urls = urls.count()
        unique_users = User.objects.count()

        top_url = urls.order_by('-click_count').first()
        recent_url = urls.order_by('-created_at').first()
        expiring_soon_url = urls.filter(expires_at__isnull=False, expires_at__gte=now()).order_by('expires_at').first()

        return render(request, self.template_name, {
            'total_clicks': total_clicks,
            'total_urls': total_urls,
            'unique_users': unique_users,
            'top_url': top_url,
            'recent_url': recent_url,
            'expiring_soon_url': expiring_soon_url,
        })
