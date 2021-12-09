import pprint

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def calc_fuel_part1(index, locations):
  fuel = 0

  for i in range(len(locations)):
    fuel += abs(locations[i]-index)

  return fuel

def calc_fuel_part2(index, locations):
  fuel = 0

  for i in range(len(locations)):
    for j in range(abs(locations[i]-index)+1):
      fuel += j

  #print(fuel)
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
  
  #print(int_input)

  max = 0

  for i in int_input:
    if i > max:
      max = i

  answer_pt1 = max * len(int_input)

  for i in range(max):
    fuel = calc_fuel_part1(i, int_input)
    if fuel < answer_pt1:
      answer_pt1 = fuel
     
  #answer = calc_fuel(1,int_input)

  answer_pt2 = max * calc_fuel_part2(max,int_input)

  for i in range(max):
    fuel = calc_fuel_part2(i, int_input)
    if fuel < answer_pt2:
      answer_pt2 = fuel

  #answer
  print("Part 1:")
  print(answer_pt1)

  print("Part 2:")
  print(answer_pt2)

  
if __name__== "__main__":
  main()

