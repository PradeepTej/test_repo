from django.views.generic import TemplateView
from players.models import Player
from clubs.models import Club
from matches.models import Match
from runrate_properties_pkg.runrate_properties import Runrate


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['tops'] = Player.objects.featured().order_by('-runs')[:3]
        context['top_clubs'] = Club.objects.all().order_by('-points')[:3]
        context['matches'] = Match.objects.all().order_by('-timestamp')[:3]
        n = Runrate()
        # n.runrate()
        return context
