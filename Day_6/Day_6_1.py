import pprint

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def next_day(fish_age):
  #for i in range(len(state)):
  #  state[i] = state[i] - 1
  #  if state[i] == -1:
  #    state[i] = 6
  #    state.append(8)

  old_fish_age = list(fish_age)

  fish_age[8] = old_fish_age[0] 
  fish_age[7] = old_fish_age[8]
  fish_age[6] = old_fish_age[7] + old_fish_age[0]
  fish_age[5] = old_fish_age[6]
  fish_age[4] = old_fish_age[5]
  fish_age[3] = old_fish_age[4]
  fish_age[2] = old_fish_age[3]
  fish_age[1] = old_fish_age[2]
  fish_age[0] = old_fish_age[1]
 
  print(fish_age)

  return fish_age

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

  #convert to int array
  int_input = char_array_to_int(input_list[0].split(','))
  
  #print(int_input)

  print("Initial State:" + str(int_input))

  #convert input into number of lantern fish for each age 1-6
  fish_age =[0,0,0,0,0,0,0,0,0]  #initialize all quantities of fish to 0

  for i in range(len(int_input)):
    for x in range(8):
      if int_input[i] == x:
        fish_age[x] += 1

  print("Initial fish age quantities")
  print (fish_age)

  num_days = 256

  for i in range(num_days):
    fish_age = next_day(fish_age)
    #print("After "+str(i+1)+" days:" + str(int_input))


  answer = sum(fish_age)

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

