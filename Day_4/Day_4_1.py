import pprint

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
  bingo_cards_3D = [[[0 for col in range(len_cards)] for col in range(len_cards)] for row in range(num_cards)]

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

  print(bingo_numbers)

  bingo_cards = separate_bingo_cards(input_list)

  pprint.pprint(bingo_cards)

  #do stuff



  answer = "NULL"

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

