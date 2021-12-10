import pprint

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def main():
  Day = 8
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
    input_list.append(raw_list[i].strip('\n').split(' | '))  ##strip newline

  #print(input_list)

  signal_patterns = []
  output_values = []

  for i in range(len(input_list)):
    signal_patterns.append(input_list[i][0].split())
    output_values.append(input_list[i][1].split())

  print(signal_patterns)
  print(output_values)

  # Seven Segment number segment counts:
  # # of segments  : numbers
  # 2 : 1
  # 3 : 7
  # 4 : 4
  # 5 : 2,3,5
  # 6 : 0,6,9
  # 7 : 8

  counter = 0

  for i in range(len(output_values)):
    for j in range(len(output_values[i])):
      length = len(output_values[i][j])
      if length == 2 or length == 3 or length == 4 or length ==7:
        counter += 1

  #answer
  print("Part 1:")
  print(counter)

  print("Part 2:")
  print("NULL")

  
if __name__== "__main__":
  main()

