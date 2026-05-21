from django.views.generic import TemplateView

class UnderConstructionView(TemplateView):
    template_name = 'core/under_construction.html'

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Soluciones Inteligentes, Compromiso Innegociable'
        return context
