from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.base import View
from .models import JMenu



class MenuView(View):
    def get(self, request, item_slug):
        return render(request, 'tmptagmenu/index.html',
                      {'cat_selected': item_slug})

