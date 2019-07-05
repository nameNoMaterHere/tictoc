def whosturn(turn):#function help know who s turn x or o
    '''
    checks who'es turn is it. if turn is even return 'o' if odd return 'x'
    :param turn: number of current turn
    :return: 'x' or 'o'
    '''
    if turn % 2 == 0:
       play = "o"
    else:
       play = "x"
    return play
def placeprint(place):
    for i in place:
        print(i)
        #for x in range(len(place[i])):
        #   print(place[i][x])

def inputNumber(msg):
    num = ""
    while (num in ['0','1','2']) == False:
        num = input(msg)
    num = int(num)
    return num

print("welcome to tik tok game")
place=[["_","_","_"],["_","_","_"],["_","_","_"]]
turn= 1 #couter turns
while True:
        a = inputNumber("Input line: ")
        b = inputNumber("Input row: ")

        #if (a in [0, 1, 2]) == False or (b in [0, 1, 2]) == False:#help know the input is right
        #      print("wrong numbers try again")
        #      continue#continue collect numbers until number be btweeb 0-2
        if place[a][b]=="_":#check if the place is ampty
             play = whosturn(turn)
             place[a][b]=play
             turn=turn+1
             placeprint(place)
             
             if (place[0].count('x') or place[1].count('x') or place[2].count('x')) == 3:#win in line in the same inlist
                     print("x winner")
                     again = input("want play again?(1= yes,2= no)")#ask if start game again
                     if again == "1":
                           turn = 1
                           place = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
                           continue
                     else:
                           break
             elif (place[0].count('o') or place[1].count('o') or place[2].count('o')) == 3:#win in line in the same inlist
                    print("o winner")
                    again = input("want play again?(1= yes,2= no)")#ask if start game again
                    if again == "1":
                         turn = 1
                         place = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
                         continue
                    else:
                            break
             if ((place[0][0]==place[1][1]==place[2][2])and (place[0][0]!="_")) or ((place[0][2]==place[1][1]==place[2][0])and (place[0][2]!="_")):
                    if place[0][0]=="x":
                            print("x win")
                    else:
                            print("o win")
                    again = input("want play again?(1= yes,2= no)")#ask if start game again
                    if again == "1":
                            turn = 1
                            place = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
                            continue
                    else:
                        break
             if ((place[0][1]==place[1][1]==place[2][1]and place[1][1]!="_" )\
                            or(place[0][0]==place[1][0]==place[2][0] and place[0][0]!="_")\
                            or(place[0][2]==place[1][2]==place[2][2] and place[2][2]!="_")):
                    if place[0][1]=="x":
                             print("x win")
                    else:
                             print("o win")
                    again = input("want play again?(1= yes,2= no)")
                    if again == "1":
                         turn = 1
                         place = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
                         continue
                    else:
                         break
             if str(place).count("_") == 0:
                 print("draw")
                 again = input("want play again?(1= yes,2= no)")
                 if again == "1":
                    turn = 1
                    place = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
                    continue
                 else:
                     break
        else:
             print("the place full try another place")
             continue
