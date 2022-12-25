from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character, Item
# Create your views here.


class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'race', 'background', 'level', 'style']
    success_url = '/characters/'

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'race', 'background', 'level', 'style']

class CharacterDelete(DeleteView):
    model = Character
    success_url = '/characters/'

class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'notes']
    success_url = '/items/'

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'notes']

class ItemDelete(DeleteView):
    model = Item
    success_url = '/items/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'characters/detail.html', { 'character': character })


def items_index(request):
    items = Item.objects.all()
    return render(request, 'items/items_index.html', {'items': items})

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/items_detail.html', { 'item': item })


# class Character:
#     def __init__(self, name, race, background, level, style):
#         self.name = name
#         self.race = race
#         self.background = background
#         self.level = level
#         self.style = style

# characters = [
#     Character('Dragur Fallrag', 'Dwarf', 'Fisherman', 7, 'Bard'),
#     Character('Huddol Wintervine', 'Elf', 'Smuggler', 3, 'Rogue'),
#     Character('Kindi Eveningfall', 'Human', 'Sage', 15 , 'Druid'),
#     Character('Trax Idlehands', 'Dragonborn', 'Soldier', 8, 'Fighter')
# ]