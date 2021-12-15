import pprint


def split(word):
    return [char for char in word]

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def pos_edge_cases(position, heightmap):
  updated_pos = [0,0]

  return updated_pos

def add_pos_to_check(position, heightmap, pos_to_check):
  y = position[1]
  x = position[0]

  #print(heightmap)
  
  # for each direction if not out of bounds then add to pos to check
  #up
  if (y-1) >= 0: 
    pos_to_check.append([x,y-1])
   
  #down
  if (y+1) < len(heightmap): 
    pos_to_check.append([x,y+1])

  #left
  if (x-1) >=0:
    pos_to_check.append([x-1,y])

  #right
  if x+1 < len(heightmap[0]):
    pos_to_check.append([x+1,y])

  return(pos_to_check)



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

  low_points = []
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
        #print("lowpoint at " + str(x) + "," + str(y))
        low_points.append([x,y])
        low_point_risk.append(current_value+1)

  print(low_points)

  #part 2,  For each low point, determine the basin size.  multiply the 3 largest basin sizes

    #pos_to_check = []
  #pos_in_basin = []
  pos_queue = []
  pos_checked = []
  basins = []

  for i in range(len(low_points)):  # for each low point determin basin size

    #print("Checking Basin around lowpoint at " + str(low_points[i])) 

    basin_size = 0
    y = low_points[i][1]
    x = low_points[i][0]
    
    #add initial points to check
    pos_queue = add_pos_to_check(low_points[i], int_input, pos_queue)
    basin_size += 1
    pos_checked.append(low_points[i])
    
    #for a given position, check if it is not part of a basin (9)
  
    while len(pos_queue) > 0:
      position = pos_queue.pop()
      #print ("checking position: " + str(position))
      pos_value = int_input[position[1]][position[0]]

      if position not in pos_checked and pos_value != 9:
        pos_queue = add_pos_to_check(position,int_input,pos_queue)
        basin_size += 1

      pos_checked.append(position) 
    
    #print("Basin size is " + str(basin_size))
    basins.append(basin_size)
           
  basins.sort(reverse=True)


  #answer
  print("Part 1:")
  print(sum(low_point_risk))

  print("Part 2:")
  print(basins[0]*basins[1]*basins[2])

  
if __name__== "__main__":
  main()

  filename = "input.txt"
