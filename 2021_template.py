import pprint

def split(word):
    return [char for char in word]

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array


def main():
  Day = 9
  filename = "test_input.txt"

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

  #convert to int array
  int_input = char_array_to_int(input_list[0].split(','))
  
  print(int_input)



  #answer
  print("Part 1:")
  print("NULL")

  print("Part 2:")
  print("NULL")

  
if __name__== "__main__":
  main()

