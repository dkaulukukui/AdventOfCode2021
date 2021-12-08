import pprint

def initialize_3D_list(a,b,c):
  threeD_list = [[[0 for col in range(a)] for col in range(b)] for row in range(c)]
  return threeD_list

def separate_bingo_cards(input_list):
  # function takes in input_list with first line removed
  # returns a list of 2D char array bingo cards

  #remove spaces in input list
  for elem in list(input_list):
    if elem == '':
      input_list.remove(elem)

  #separate bingo cards
  bingo_cards=[]

  for i in range(0,len(input_list),5):
    bingo_cards.append(input_list[i:(i+5)])

  num_cards = len(bingo_cards)
  len_cards = len(bingo_cards[0])

  print("Input has a total of " + str(num_cards) + " bingo cards")

  #split bingo cards into 3D arrays
  bingo_cards_3D = initialize_3D_list(len_cards,len_cards,num_cards)
  #bingo_cards_3D = [[[0 for col in range(len_cards)] for col in range(len_cards)] for row in range(num_cards)]

  for i in range(num_cards):
    for j in range(len_cards):
      bingo_cards_3D[i][j] = bingo_cards[i][j].split()

  return bingo_cards_3D




def main():
  Day = 4
  filename = "input.txt"

  file_object  = open("/home/dkaulukukui/Documents/AdventOfCode2021/Day_"+str(Day)+ "/" +filename, "r")

  print("AOC_2021_Day "+ str(Day))

  raw_list = []
  input_list = []


  #read each line into raw list for processing
  for line in file_object:
      raw_list.append(line)

  #process list into list of integers
  for i in range(len(raw_list)):
    input_list.append(raw_list[i].strip('\n'))  ##strip newline
  #print(input_list)

  #separate bingo numbers from bingo cards
  bingo_numbers = input_list[0]
  input_list.remove(bingo_numbers)  #remove from list
  bingo_numbers = bingo_numbers.split(',')

  print(bingo_numbers)

  bingo_cards = separate_bingo_cards(input_list)

  num_cards = len(bingo_cards)
  len_cards = len(bingo_cards[0])

  #pprint.pprint(bingo_cards)

  #do stuff

  winning_card = "NULL"
  winning_coord = []

  #call numbers one by one
  for i in range(len(bingo_numbers)):
    #print("i = " + str(i))
    called_numbers = bingo_numbers[0:i+1]

    #every time a number is called check each card for completed rows or columns
  
    #check each card
    for i in range(num_cards):  
    
      #check each rows
      for x in range(len_cards): #check each row
        match = 0  #initialize match counter
        for y in range(len_cards): #check each column in each row
          #setup counter, increment counter for every match, if counter=len then row is complete
          for elem in called_numbers:
            if elem == bingo_cards[i][x][y]:
              match += 1
        if match == len_cards:
          if(winning_card == "NULL"):
             winning_card = i+1
             winning_coord = [x+1,0]
          #print("BINGO!!! for card " + str(i+1) + " row " + str(x+1))
          break
        if (winning_card != "NULL"):   #exit for loop if winner found
          break


      #check each column
      for y in range(len_cards): #check each column
        match = 0  #initialize match counter
        for x in range(len_cards): #check each row in each column
          #setup counter, increment counter for every match, if counter=len then row is complete
          for elem in called_numbers:
            if elem == bingo_cards[i][x][y]:
              match += 1
        if match == len_cards:
          if(winning_card == "NULL"):
             winning_card = i+1
             winning_coord = [0,y+1]
          #print("BINGO!!! for card " + str(i+1) + " row " + str(x+1))
          break
        if (winning_card != "NULL"):   #exit for loop if winner found
          break


      if (winning_card != "NULL"):   #stop checking cards if winner found
          break
    if (winning_card != "NULL"):   #stop calling number if winner found
          break


    
    
    #if card has completed row or column return it and calculate answer
    
  print("BINGO!!! for card " + str(winning_card) + " coord " + str(winning_coord))

  print(called_numbers)
  pprint.pprint(bingo_cards[winning_card-1])

  #answer is the sum of all unmarked numbers on the winning board multiplied by the last number called

  last_called = int(list(called_numbers).pop())
  print("Last called number = " + str(last_called))

  sum_of_winner = 0

  for x in range(len_cards):
    for y in range(len_cards):

      sum_of_winner = sum_of_winner + int(bingo_cards[winning_card-1][x][y])
      
      for elem in called_numbers:  # check called numbers
        if elem == bingo_cards[winning_card-1][x][y]:  #if number was called then subtract it
          sum_of_winner = sum_of_winner - int(bingo_cards[winning_card-1][x][y])


  print("Sum of winning card= " + str(sum_of_winner))     
      

  answer = sum_of_winner*last_called

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

