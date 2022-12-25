from django.shortcuts import render
from .models import Character
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})

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