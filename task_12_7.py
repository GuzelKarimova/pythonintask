# Задача 12. Вариант 7. 
# Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python гл. 6) 
# Videneev P. A.
# 26.05.2016 
import random 
#крестики-нолики 
X = "X" 
O = "O" 
EMPTY = " " 
TIE = "ничья" 
NUM_SQUARES = 9 
def main(): 
return 0 
def display_instruct(): 
print (""" 
0 | 1 | 2 
—-----— 
3 | 4 | 5 
—-----— 
6 | 7 | 8 
""") 
def ask_yes_no(question): 
response = None 
while response not in ("y", "n"): 
response = input (question).lower() 
return response 

def ask_number(question, low, high): 
response = None 
while response not in range(low, high): 
response = int(input(question)) 
return response 
def pieces(): 
go_first = ask_yes_no("Кто ходит первым?\n") 
if go_first == "y": 
print ("Твой ход!") 
human = X 
computer = O 
else: 
print ("Начинаю") 
human = O 
computer = X 
return computer, human 

def new_board(): 
board = [] 
for square in range(NUM_SQUARES): 
board.append(EMPTY) 
return board 

def display_board(board):