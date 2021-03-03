import time

#import fileinput
#import sys

#def replaceAll(file,searchExp,replaceExp):
#      if searchExp in line:
#            line = line.replace(searchExp,replaceExp)
#        sys.stdout.write(line)

menu = "1. Показать список дел \n" \
       "2. Добавить задачу \n" \
       "3. Удалить \n" \
       "0. Выход"
def print_menu():
	print(menu)

def print_todo():
    with open('todo.txt', 'r', encoding='utf-8') as todo:
    	print(todo.read()) # как сделать чтобы выводилось сообшение при пустом списке(файл пуст)   	


def add_todo():
	a = input('Введите новую задачу: ')
	with open('todo.txt', 'a', encoding='utf-8') as todo:
		todo.write(a + '\n')

def delete_todo():
	with open('todo.txt', 'w', encoding='utf-8') as todo:
		todo.write('СПИСОК ЗАДАЧ ПУСТ')
		print('Список задач очищен')# как удалить необходимую нам строчку (как произвести переход на необходимую строчку)
									# как выбрать необходимую нам внесенную задачу и произвести ее замену
print('Приветствую с списке задач!')
time.sleep(1)
print('Вы можете выбрать следующее:') 
time.sleep(1)
print(menu)
time.sleep(2) 

while True:
    command = input("Введите команду:  " )
    if command not in ("1","2","3","4","0"):
            print("Введите необходимую Вам команду!")
            time.sleep(1)
            print_menu()
    elif command == "1":
            print_todo()
    elif command == "2":
            add_todo()
    elif command == '3':
           delete_todo()
    elif command =='0':
       	break
