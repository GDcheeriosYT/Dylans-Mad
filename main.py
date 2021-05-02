import random
import re

#mode
print("0. on\n1. off")
mode = input("would you like sfw mode on or off? ")
list_end = 113

while True:
  pattern = "\d\d\d"
  #random_variables
  object_1 = random.randint(10, list_end)
  object_2 = random.randint(10, list_end)
  verb = random.randint(0, 5)
  lines = random.randint(0, 2)
  reaction = random.randint(4, 8)

  #turning the dictionaries into a list
  with open("object_dictionary.txt") as f:
    objects = f.read().splitlines()

  with open("verbs.txt") as f:
    verbs = f.read().splitlines()
    
  with open("beatmaps.txt") as f:
    maps = f.read().splitlines()

  with open("reactions.txt") as f:
    reactions = f.read().splitlines()
  
  if mode == "0":
    print("ok")
  else:
    print("ok")
    nsfw_object_if = random.randint(0, 2)
    if nsfw_object_if == 1:
      object_1 = random.randint(0, list_end - 1)
      object_2 = random.randint(0, list_end - 1)
      reaction = random.randint(0, 6)
    else:
      object_1 = random.randint(8, list_end - 1)
      object_2 = random.randint(8, list_end - 1)
      reaction = random.randint(1, 6)

  #choosing a beatmap
  x = 0
  while x < 18:
    print("%s %s" % (x, maps[x]))
    x = x + 1

  print("______________________________________________________")

  map_choose = input("which beatmap shall dylan play?\nenter a number... ")
  try:
    val = int(map_choose)
  except ValueError:
    print("expected a number, I will just pick for you...")
    map_choose = random.randint(0, 18)
  try:
    maps[int(map_choose)]
  except IndexError:
    print("too big!")
    map_choose = random.randint(0, 18)

  print(maps[int(map_choose)])

  #map name
  map_name = re.search("^\D+", maps[int(map_choose)]) 

  #point judger
  points = re.search(pattern, maps[int(map_choose)])

  dylans_goal = random.randint(0, int(points.group()))
  dylans_outcome = random.randint(0, int(points.group()))

  #random output

  ending = random.randint(0, 3)
  if ending == 1:
    ending = "at his"
  elif ending == 2:
    ending = "and it landed on his"
  else:
    ending = "and it hit his"


  if dylans_outcome > dylans_goal:
    print("============================================================================================================")
    print("dylan went %s and got a %spp play out of %spp on %shis intended goal was %spp" % (reactions[reaction], dylans_outcome, points.group(), map_name.group(), dylans_goal))
    print("============================================================================================================")
  elif dylans_outcome < dylans_goal:
    if lines == 1:
      print("============================================================================================================")
      print("dylan wanted a %spp play on %s and got a %spp play out of %spp and %s %s" % (dylans_goal, map_name.group(), dylans_outcome,  points.group(), verbs[verb], objects[object_1]))
      print("============================================================================================================")
    else:
      print("============================================================================================================")
      print("dylan wanted a %spp play on %s and got a %spp play out of %spp and threw his %s %s %s" % (dylans_goal, map_name.group(), dylans_outcome, points.group(),  objects[object_1], ending, objects[object_2]))
      print("============================================================================================================")
  else:
    print("============================================================================================================")
    print("dylan went %s and got a %spp play out of %spp on %s his intended goal was %s" % (reactions[reaction], dylans_outcome, points.group(), map_name.group(), dylans_goal))
    print("============================================================================================================")
  input("press enter to continue...")
  print("============================================================================================================")