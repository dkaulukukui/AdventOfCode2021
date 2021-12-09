import pprint

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def calc_fuel(index, locations):
  fuel = 0

  for i in range(len(locations)):
    fuel += abs(locations[i]-index)

  return fuel


def main():
  Day = 7
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

  #convert to int array
  int_input = char_array_to_int(input_list[0].split(','))
  
  print(int_input)

  max = 0

  for i in int_input:
    if i > max:
      max = i

  answer = max * len(int_input)

  for i in range(max):
    fuel = calc_fuel(i, int_input)
    if fuel < answer:
      answer = fuel
     
  #answer = calc_fuel(1,int_input)

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

