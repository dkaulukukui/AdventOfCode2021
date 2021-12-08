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

  card_index = []
  win_order = []
  winning_calls = []
  last_called = []

  #initialize a list of all card indexs
  for i in range(num_cards): 
    card_index.append(i)

  #call numbers one by one
  for i in range(len(bingo_numbers)):
    #print("i = " + str(i))
    called_numbers = bingo_numbers[0:i+1]

    #print("Called Numbers:" )
    #print(called_numbers)

    if len(card_index) == 0:
      break

    #every time a number is called check each card for completed rows or columns
  
    #check each card
    for i in card_index:
      #print("cards remaining:")
      #print(card_index)

      #check each rows
      card_is_winner = 0
      #print("checking card " + str(i+1))

      for x in range(len_cards): #check each row
        match = 0  #initialize match counter
        for y in range(len_cards): #check each column in each row
          #setup counter, increment counter for every match, if counter=len then row is complete
          for elem in called_numbers:
            if elem == bingo_cards[i][x][y]:
              match += 1
          if match == len_cards:  #winner winner  
              card_index.remove(i)  ##delete card from index since it won
              win_order.append(i)   ##add card index to winner list
              winning_calls.append(called_numbers)  ## record numbers called at time of win
              card_is_winner = 1
              #print("BINGO!!! for card " + str(i+1) + " row " + str(x+1))
              break
       
      if card_is_winner == 0:  #card hasnt won for a row
          #check each column
          for y in range(len_cards): #check each column
            match = 0  #initialize match counter
            for x in range(len_cards): #check each row in each column
              #setup counter, increment counter for every match, if counter=len then row is complete
              for elem in called_numbers:
                if elem == bingo_cards[i][x][y]:
                  match += 1
              if match == len_cards: #winner winner
                  card_index.remove(i)  ##delete card from index since it won
                  win_order.append(i)   ##add card index to winner list
                  winning_calls.append(called_numbers)  ## record numbers called at time of win
                  card_is_winner = 1
                #  print("BINGO!!! for card " + str(i+1) + " column " + str(y+1))
                  break  
    
  
  last_winner = list(win_order).pop()+1

  print("Last winning card is card " + str(last_winner))

  #print("remaining cards are: " + str(card_index))

  pprint.pprint(bingo_cards[last_winner-1])

  last_call_order = list(winning_calls).pop()

  print("Calls made to last winner =" + str(last_call_order))


  #print(last_call_order)

  last_called = int(list(last_call_order).pop())
  last_called = int(last_call_order[len(last_call_order)-2])  #I am a hack and I should be ashamed

  print("Last number called = " + str(last_called))


  sum_of_winner = 0
  offset_sum_of_winner = 0

  for x in range(len_cards):
    for y in range(len_cards):

      sum_of_winner = sum_of_winner + int(bingo_cards[last_winner-1][x][y])
      
      for elem in last_call_order:  # check called numbers
        if elem == bingo_cards[last_winner-1][x][y]:  #if number was called then subtract it
          #print("elem =" + str(elem) + " value= " + str(bingo_cards[last_winner-1][x][y]))
          offset_sum_of_winner = offset_sum_of_winner + int(bingo_cards[last_winner-1][x][y])
          #print("Subtracting " + str(int(bingo_cards[last_winner-1][x][y])))



  print("Sum of losing card= " + str(sum_of_winner)) 
  print("Offset = " + str(offset_sum_of_winner)) 

  sum_of_winner = sum_of_winner - offset_sum_of_winner  

  print("Sum of losing card - offset = " + str(sum_of_winner))  

  answer = sum_of_winner*last_called

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

