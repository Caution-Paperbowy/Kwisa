import csv
# workbook = openpyxl.load_workbook('places.xlsx')


places = [['qualikeeper inv', 6054, 'Sibweni', 'Northmead', 'lsk', 'Roadspark sch'], ['AAH', 6054, 'Sibweni', 'Northmead', 'lsk', 'Roadspark sch'], ['car hire', 6054, 'Sibweni', 'Northmead', 'lsk', 'Roadspark sch']]
with open('places.csv', 'w', newline ='') as file:
     writer = csv.writer(file)
     writer.writerows(places)

FILENAME = 'places.csv'


def display_menu():
    print()
    print('WELCOME TO KWISA, TO SEARCH A PLACE,PRESS THE SEARCH BUTTON, FOR ADDING A PLACE, PRESS THE ADD BUTTON')
    print()
    print('COMMAND MENU')
    print('==============')
    print()
    print("list - LIST ALL PLACES")
    print('add - ADD A PLACE')
    print('search - SEARCH A PLACE')
    print('exit - EXIT PROGRAM')
    print()



def write_places(places):
     with open(FILENAME, 'w', newline ='') as file:# w means in write mode
         writer = csv.writer(file)
         writer.writerows(places)


def read_places():#we start with this since its first thing to be executed after main runs
     places = []   #we convert contents in text file to string
     with open(FILENAME) as file:
         reader = csv.reader(file)
         for row in reader:
             places.append(row)
     return places


def list_places(places):
     for i in range(len(places)):#loop from zero to the end of the list len function is checking the length of our emplyees list
         place = places[i]#which ever employee we're currently on while looping through our list
         print(str(i+1) + '.' + place[0] + ':' + place[1] + '/' + place[2] + ' RD' + ',' + place[3] + ',' + place[4] + ',Near ' + place[5] )#we wont start at zero, we will tart at one.print everything we were on while going through. i can be any element in our list, then also append actual name of employee
     print()



def add_place(places):
    name = input('Name: ')#collects name of place you want to add
    print()
    addr = input('Address: ')##colects extention
    print()
    rd = input('Road: ')
    print()
    area = input('Area: ')
    print()
    city = input('City: ')
    print()
    nrstldmk = input('Nearest landmark: ')
    print()
    place = []#create temporary list
    place.append(name)#append name to that list. actual name of the employee
    place.append(addr)#append extention to that list
    place.append(rd)
    place.append(area)
    place.append(city)
    place.append(nrstldmk)
    places.append(place)#take temporary list we created and append it to main list
    write_places(places)#call the wriite employees function and pass in the list parameter that we are appending
    #workbook.save('example.xlsx')
    print(name,'' +  'was added.\n')


def delete_place(places):
    index = int(input('Number: '))
    place = places.pop(index - 1)#delting
    write_places(places)#pass in the modified list
    print(place[0] + 'was deleted.\n')



def main():
     display_menu()
     places = read_places()#we store ead employees in the variable employees so that its easy to pass it in the conditional statements
     while True:
         command = input('command: ')
         print()
         if command == 'list':
             list_places(places)
         elif command == 'add':
             add_place(places)
         elif command == 'del':
             delete_place(places)
         elif command == 'exit':
             print("the program has been terminated...")
             break
         else:
             print("Not a valid command. Please try a different command")



if __name__== '__main__':  #checks to make sure our main is the main module
    main()