import pprint

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def next_day(state):
  for i in range(len(state)):
    state[i] = state[i] - 1
    if state[i] == -1:
      state[i] = 6
      state.append(8)
  return state

def main():
  Day = 6
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
  
  #split_input_list = input_list.split() 
  
  #print(input_list)

  #convert to int array
  int_input = char_array_to_int(input_list[0].split(','))
  
  #print(int_input)

  print("Initial State:" + str(int_input))

  num_days = 80

  for i in range(num_days):
    int_input = next_day(list(int_input))
    print("After "+str(i+1)+" days:" + str(int_input))


  answer = len(int_input)

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

