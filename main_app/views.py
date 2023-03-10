from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character, Item
from .forms import SessionForm
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
    id_list = character.items.all().values_list('id')
    items_character_doesnt_have = Item.objects.exclude(id__in=id_list)
    session_form = SessionForm()
    return render(request, 'characters/detail.html', {
        'character' : character, 'session_form': session_form,
        'items': items_character_doesnt_have
    })


def items_index(request):
    items = Item.objects.all()
    return render(request, 'items/items_index.html', {'items': items})

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/items_detail.html', { 'item': item })

def add_session(request, character_id):
  # create a ModelForm instance using the data in request.POST
  form = SessionForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_session = form.save(commit=False)
    new_session.character_id = character_id
    new_session.save()
  return redirect('detail', character_id=character_id)

def assoc_item(request, character_id, item_id):
    Character.objects.get(id=character_id).items.add(item_id)
    return redirect('detail', character_id=character_id)

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