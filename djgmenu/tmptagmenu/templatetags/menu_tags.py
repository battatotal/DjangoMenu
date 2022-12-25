from django import template
from tmptagmenu.models import *

register = template.Library()

@register.inclusion_tag('tmptagmenu/dr_menu.html')
def draw_menu(item_slug=None):
    menu = JMenu.objects.all()  #<<<<<!!!!
    cmp = [i.id for i in menu if i.slug == item_slug]  # элемент контекста для отображения всех вкладок поверх выбранной
    countdct = {}  # Определяю количество вложенных строк в шаблоне
    for i in menu:
        if i.descendant:
            # count = 0
            count = []
            for val in menu:
                if val.ancestor == i.id:
                    # count += 1
                    count.append(val)
            countdct[i] = count  # [0]*count  #тут решил создать объект который можно перебрать на шаблоне
    return {"menu_list":menu, "spaces":countdct, "cmp":cmp[0] }