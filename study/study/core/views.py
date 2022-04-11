from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Test1View(TemplateView):

    template_name = "test1.html"

    def get(self, request):

        return render(request, "test1.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "home.html")


test1_view = Test1View.as_view()


class CalcView(TemplateView):

    template_name = "calc.html"

    def get(self, request):

        return render(request, "calc.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "calc.html")


calc_view = CalcView.as_view()


class FrontendRenderView(TemplateView):

    template_name = "front.html"

    def get(self, request):

        return render(request, "front.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "front.html")


frontendRender_view = FrontendRenderView.as_view()
