
print("Scallywag the Pirate")
print("")
print("")
name = input("What is your name?")
print("Hello " + name + "!")
print("My name is Scallywag the pirate!")
counter = 0
while counter == 0:
  description = input("How do you feel right now, matey?")
  list_of_words = description.split()
  for each_word in list_of_words:
    if each_word == "sad" and counter == 0:
      print("Back in my day, if an 'ol seadog was sad, we'll drink to the gods!")
      print("Tomorrow will be a better day, we would say.")
      counter = 1
    if each_word == "happy" and counter == 0:
      print("Well," + name + ", look's like it's time for some rum!")
      print("Yes, the good stuff......")
      counter = 1
    if each_word == "tired" and counter == 0:
      print("Working your butt off the whole day? Hardworking, I'se say.")
      print("You should remember to hole up once in a while, lad")
      counter = 1
    if counter = 0:
      print("What? I don't know what you are saying!")
      print("Oh nevermind. Your feelings can stay to yourself.")
      counter = 1      
while counter == 1:
  description = input("You look troubled, is that nasty shark biting your leg again?")
 while counter == 1:
  description = input("You look troubled, is that nasty shark biting your leg again?")
  if description== 'yes':
    print("aww, thats sad!")
    counter= 0
  if description== 'no':
    print("good")
    counter = 0
    
    
