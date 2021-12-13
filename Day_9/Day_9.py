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

  #convert to int array
  int_input = []
  for i in range(len(input_list)):
      split_list = split(input_list[i])
      int_input.append(split_list)
  
  #convert to ints

  for y in range(len(int_input)):
    for x in range(len(int_input[y])):
      int_input[y][x] = int(int_input[y][x])

  pprint.pprint(int_input)

  #find low points in input map

  low_point_risk = []

  for y in range(len(int_input)):
    for x in range(len(int_input[y])):
      #print("checking y= " + str(y)+" x= " + str(x))

      current_value = int_input[y][x]
      
      #low point if all points adjecent, up, down, left, right are higher in value
      
      if (y-1) < 0: # up = [y-1][x]
        up = 10
      else: 
        up = int_input[y-1][x]  
      if (y+1) >= len(int_input): # down = [y+1][x]
        down = 10
      else:
        down = int_input[y+1][x]
      if (x-1) < 0: # left =  [y][x-1]
        left = 10
      else:
        left = int_input[y][x-1]
      if (x+1 >= len(int_input[y])): # right = [y][x+1]
        right = 10
      else:
        right = int_input[y][x+1]

      #print("up = " + str(up) + " down = " + str(down) + " left = " + str(left) + " right = " + str(right))


      if current_value < up and current_value < down and current_value < left and current_value <right:
        #lowpoint
        print("lowpoint at " + str(x) + "," + str(y))
        low_point_risk.append(current_value+1)

  #answer
  print("Part 1:")
  print(sum(low_point_risk))

  print("Part 2:")
  print("NULL")

  
if __name__== "__main__":
  main()

