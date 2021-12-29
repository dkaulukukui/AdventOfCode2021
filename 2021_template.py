import pprint


def process_input(Day, filename):
  #Day = 12
  #filename = "test_input.txt"

  file_object  = open("/home/dkaulukukui/Documents/AdventOfCode2021/Day_"+str(Day)+ "/" +filename, "r")

  print("AOC_2021_Day "+ str(Day))

  raw_list = []

    #read each line into raw list for processing
  for line in file_object:
      raw_list.append(line.strip('\n'))

  #print (raw_list)

  return raw_list

def split(word):
    return [char for char in word]

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def main():

  raw_input = process_input(13, "test_input.txt")

  print(raw_input)

  input_list = []

  #process list further
  for i in range(len(raw_input)):
    input_list.append(raw_input[i].split('-'))  ##strip newline


  #answer
  print("Part 1:")
  print("NULL")

  print("Part 2:")
  print("NULL")

  
if __name__== "__main__":
  main()

