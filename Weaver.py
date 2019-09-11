#Weaver
#Tegan Broderick, September 2019
#Program visualizes weaving patterns for a four harness loom. The warp threads are represented in white, and the weft threads are represented in black
#Code runs using repl.it, using the Python (with Turtle) interface.
#Open Weaver in repl.it at https://repl.it/@TeganBroderick/Weaver

import random
import turtle
#define turtle and turtle attributes
t = turtle.Turtle()
wn = turtle.Screen()
t.pensize(10)
t.speed(100)
#define turtle starting point, and move turtle there
x = -900
y = 900
startingpoint = (x,y)
t.penup()
t.goto(startingpoint)
t.pendown()

#Arrays storing pattern names, warp calculations, and weft calculations
easy_pattern_names = ["Plain Weave", "Twill (left to right)", "Twill (right to left)", "Extended ZigZag", "Hopsack", "3/1 Hopsack", "Mixed Twill, 3x2/16", "Mixed Twill, 1/3 and 3/1 Twill Merging", "Mini Herringbone", "Point 2/2 Twill"]
easy_warp_array = [[1,2,3,4]]
easy_weft_array = [[[1,3],[2,4]], [[1,2],[2,3],[3,4],[1,4]],[[1,4],[3,4],[2,3],[1,2]], [[3,4],[2,3],[1,2],[1,4],[3,4],[2,3],[1,2],[2,3],[3,4],[1,4],[1,2],[2,3],[3,4],[1,4]],[[1,2],[1,2],[3,4],[3,4]], [[1],[2,3,4],[2,3,4],[2,3,4]], [[1,2,3],[1,2],[1],[2,3,4],[3,4],[4]],[[1],[2],[3],[4],[1,2,3],[2,3,4],[1,3,4],[1,2,4]],[[1,2],[2,3],[1,4],[3,4]], [[1,3],[1,2],[3,4],[2,3],[1,3],[3,4],[2,4],[1,4],[1,3],[1,4],[2,4],[3,4],[1,3],[2,3],[2,4],[1,2]] ]

hard_pattern_names = ["Plain Weave", "Point Draft, Straight Diagonal Sequence", "Birds Eye 1", "Birds Eye 2", "Birds Eye, Extended point over 14"]
hard_warp_array = [[2,3,4,3,2,1]]
hard_weft_array = [[[1,3],[2,4]],[[1,2],[2,3],[3,4],[1,4]], [[1],[2],[3],[4],[3],[2]], [[1,2],[2,3],[3,4],[4,1],[3,4],[2,3]],[[1],[2],[3],[4],[3],[2],[1],[4],[3],[2],[1],[2],[3],[4]],]

def print_pattern(warp, weft, x, y):
  """prints a visual depiction of the pattern chosen by the user, using the warp and weft information in the nested warp and weft arrays"""
  #Draw pattern
  for l in range(0,2):
    for i in range (0, len(weft)):
      for k in range(0,16):
        for j in range(0, len(warp)):
          if warp[j] in weft[i]:
            t.penup()
            t.forward(11)
            t.pendown()
          else:
            t.forward(11)
      #move start position of row
      y -= 11
      t.penup()
      t.goto(x, y)
      t.pendown()
  new_start_position = [x,y]
  return new_start_position

def print_weave_info(selection_array, pattern_names):
  """Function prints pattern information for the user, by listing the different weaves they used in their pattern"""
  print("______________________________________________________________")
  print("Here are the patterns you chose, in order, for your reference: ")
  for i in range(0, len(selection_array)):
    temp_number = selection_array[i] - 1
    print(pattern_names[temp_number])

def run_program(pattern_names, warp_array, weft_array, x, y):
  """Function gets user input for pattern number, calls the print_pattern function with this input, and calls the print_weave_info function once the user is done designing their weaving"""

  selection_array = []
  weft_array_length = len(weft_array)
  repeat = "yes"
  while repeat == "yes" or repeat == "y":
    print("Here are the weaving patterns available: ")
    for i in range(0, len(pattern_names)):
      print((str(i+1)) + ". " + pattern_names[i])

    pattern_number = int(input("Please choose a number. To select a random pattern, choose 0. "))
    while pattern_number > weft_array_length or pattern_number <=-1 :
      print("Invalid input")
      pattern_number = int(input("Please choose a number: "))
    print("Please click on the result screen")

    if pattern_number == 0: #choose random pattern if input is 0
      pattern_number = random.randrange(1, weft_array_length)

    selection_array.append(pattern_number) #append number to reference in print_weave_info function

    #calculate the information to be sent to the print_pattern function, and call function
    temp_warp = warp_array[0]
    temp_weft = weft_array[pattern_number-1]
    new_start_position = print_pattern(temp_warp, temp_weft, x, y)

    #define turtle starting point for next round of pattern drawing
    x = new_start_position[0]
    y = new_start_position[1]

    repeat = input("Would you like to add another pattern? yes/no ")
    repeat = repeat.lower()
    while repeat != "yes" and repeat != "y" and repeat != "no" and repeat != "n":
      print("Invalid input")
      repeat = input("Would you like to add another pattern? yes/no ")
      repeat = repeat.lower()

  #call print_weave_info function once user is done adding patterns
  print_weave_info(selection_array, pattern_names)


#Introduction, level input, and call run_program function
print("This program allows you to explore various weaving patterns for a four harness loom. You will need to switch between this screen (console) and the result screen to see your patterns drawn. Please make sure to click on this screen when you return in order to enter information. ")
print("The warp threads are represented by blank spaces, and the weft threads are represented by black lines.")
print("")

level = input("Please select a difficulty level for your warp: easy/hard")
level = level.lower()
while level != "easy" and level != "hard":
  print("Invalid input")
  level = input("Please select a difficulty level for your warp: easy/hard")
  level = level.lower()

if level == "easy":
  run_program(easy_pattern_names, easy_warp_array, easy_weft_array, x, y)
else:
  run_program(hard_pattern_names, hard_warp_array, hard_weft_array, x, y)


"""
#INDIVIDUAL PATTERN INFO FOR REFERENCE
#Plain weave
plainweave_easy_warp = [1,2,3,4]
plainweave_easy_weft = [[1,3],[2,4]]

#Twill
twill_warp = [1,2,3,4]
twill_weft = [[1,2],[2,3],[3,4],[1,4]]

#Extended zigzag
ezigzag_warp = [1,2,3,4]
ezigzag_weft = [[3,4],[2,3],[1,2],[1,4],[3,4],[2,3],[1,2],[2,3],[3,4],[1,4],[1,2],[2,3],[3,4],[1,4]]

#Hopsack
hopsack_warp = [1,2,3,4]
hopsack_weft = [[1,2],[1,2],[3,4],[3,4]]

#3/1 Hopsack
hopsack2_warp = [1,2,3,4]
hopsack2_weft = [[1],[2,3,4],[2,3,4],[2,3,4]]

#Mixed Twill 3 x 2/16
mixedtwill_warp = [1,2,3,4]
mixedtwill_weft = [[1,2,3],[1,2],[1],[2,3,4],[3,4],[4]]

#Mixed Twill, 1/3 and 3/1 Twill Merging
mixedtwill2_warp = [1,2,3,4]
mixedtwill2_weft = [[1],[2],[3],[4],[1,2,3],[2,3,4],[1,3,4],[1,2,4]]

#Mini Herringbone
miniherringbone_warp = [1,2,3,4]
miniherringbone_weft = [[1,2],[2,3],[1,4],[3,4]]

#Point 2/2 Twill
point22twill_warp = [1,2,3,4]
point22twill_weft = [[1,3],[1,2],[3,4],[2,3],[1,3],[3,4],[2,4],[1,4],[1,3],[1,4],[2,4],[3,4],[1,3],[2,3],[2,4],[1,2]]


#Harder warps___________________________________
#"Point Draft, Straight Diagonal Sequence"
straightdiagonal_warp = [2,3,4,3,2,1]
straightdiagonal_weft = [[1,2],[2,3],[3,4],[1,4]]

#Birds Eye 1
birdseye1_warp = [2,3,4,3,2,1]
birdseye1_weft = [[1],[2],[3],[4],[3],[2]]

#Birds Eye 2
birdseye2_warp = [2,3,4,3,2,1]
birdseye2_weft = [[1,2],[2,3],[3,4],[4,1],[3,4],[2,3]]

#Birds Eye, Extended point over 14
birdseye3_warp = [2,3,4,3,2,1]
birdseye3_weft = [[1],[2],[3],[4],[3],[2],[1],[4],[3],[2],[1],[2],[3],[4]]

#Plain weave hard
plainweave_hard_warp = [2,3,4,3,2,1]
plainweave_hard_weft = [[1,3],[2,4]]
"""
