import time
import random

print('Please refer to README.txt before playing.\n')

time.sleep(1)
print('There is darkness, all around you. You have no idea where you are.')
print('A voice calls out to you.\n')
time.sleep(1)

#Character Maker
charComplete = ('no')
while charComplete in ['n', 'NO','no','N','No']:
  charName = input('What is your name?:')
  charAge = input('How old are you?:')
  charRace = input('What is your race?:')
  charGender = input('What is your gender?:')
  charClass = input('What is your class?:')
  print("\nYour are %s, the %s year old %s %s %s.\n" % (charName, charAge, charRace,charGender, charClass))
  
  charComplete = input('Is this information correct?(y/n):')
  time.sleep(1)

  if charComplete in ['y','YES','yes','Y', 'Yes']:
    print('\nGood! Character creation complete!\n')
    break
  elif charComplete in ['n', 'NO','no','N','No']:
    print('\nOh sorry. I am a lot less sharp than I used to be. Could you repeat that all again for me?\n')
  else:
    charComplete = ('no')
    print('\nI am afraid I do not understand your answer. Could you repeat that all again for me?\n')
#Character Maker

time.sleep(1)

print('The darkness fades and you can suddenly see much more clearly. Your vision adjusts to find that you are in a small bed.')
print('A middle aged dwarf looks down on you from a nearby chair. He speaks.\n')

time.sleep(1)

print('Voldrek: Aye, glad to see your still alive. I thought ye might be dead considering I found ye on the side of the road.\n')

charAction = ('INVALID')

while charAction in ['INVALID']:

  print('What do you do?:')
  print('A) Speak')
  print('B) Inspect')
  print('C) Run')
  charAction = input ('Input:')

  if charAction in ['a','A']:
    print('\nWhat do you say?:')
    print('A) Who are you?')
    print('B) Where am I?')
    charSpeak = input ('Input:')
    if charSpeak in ['a','A']:
      charAction = ('INVALID')
      print('\nVoldrek: I am Voldrek Stormhelm, the simple blacksmith here in the town of dirt.\n')
      time.sleep(1)

  elif charAction in ['b','B']:
    print('What do you want to inspect?:')
    print('A) The Bed')
    print('B) The Bookshelf')
    print('C) The Dwarf')
    print('D) The Room')
    charInspect = input ('Input:')
    if charInspect in ['a','A']:
      charAction = ('INVALID')
      print('The bed you lay in is small, but soft. The bead spread is a bright red.')
    elif charInspect in ['b','B']:
      charAction = ('INVALID')
      print('The bookshelf contains many books of various shapes and sizes. Many look old and mysterious.')
    elif charInspect in ['c','C']:
        charAction = ('INVALID')
        print('The old dwarf sits at the foot of the bed. His face is red and stern. His long grey beard drapes across his lap.')
    elif charInspect in ['d','D']:
        charAction = ('INVALID')
        print('The room is full of dusty furnishings and cobwebs. Only you and the dwarf reside in the room.')
    else:
        print('Oh shit. Whatup?')
        print('End of code.')
