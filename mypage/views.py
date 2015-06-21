from django.views.generic import View
from django.shortcuts import render

from mydetails import MyPersonalDetails


class HomePage(MyPersonalDetails, View):
    def get(self, request, *args, **kwargs):

        context = {
            'about' : self.about
        }

        return render(request, 'index.html', context)

home_page = HomePage.as_view()
