from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, View, TemplateView

from .models import Broadcast, Playlist


class IndexPage(View):
    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        else:
            context = {
                'visitor': request.user,
                'news': Broadcast.objects.filter(genre='News').last(),
                'comedies': Broadcast.objects.filter(genre='Comedy').last(),
                'sports': Broadcast.objects.filter(genre='Sports').last(),
                'playlist': Playlist.objects.filter(user=request.user).order_by('-created_at')[:2],
            }
            return render(request, 'broadcast/home.html', context)


class PlaylistView(TemplateView):
    model = Playlist
    template_name = 'broadcast/playlist.html'

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['obj'] = self.model.objects.filter(user=self.request.user).order_by('-created_at')
        return context

    def get_queryset(self):
        return self.model.objects.all()


class AddToFavorite(View):
    def post(self, request, **kwargs):
        query = Broadcast.objects.get(id=request.POST.get('id'))
        Playlist.objects.create(user=request.user, broadcast=query)
        return JsonResponse({}, status=200)


class BroadcastView(TemplateView):
    model = Broadcast
    template_name = 'broadcast/broadcast.html'

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['obj'] = self.model.objects.all().order_by('-created_at')
        return context

    def get_queryset(self):
        return self.model.objects.all()
