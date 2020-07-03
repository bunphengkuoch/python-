Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello, world!")
print("""This is a simple poem Isn't it nice?""")
print(7)
print(1 + 1)
print("Hello" + "Bob")
print("Hello" * 5)
age = int(input("How old are you?"))
age_in_10 = age + 10
print("In 10 years you will be {}".format(age_in_10))


score = 0
 
answer = input("What does CPU stand for?")
if answer == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")
answer = input("How many bits are in a byte?")
if answer == "8":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")
 
answer = input("Which is bigger: a kilobyte or a megabyte?")
if answer == "megabyte":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")
 
print("You scored {} points!".format(score))
