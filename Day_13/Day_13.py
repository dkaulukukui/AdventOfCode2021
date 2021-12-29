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

def initialize_map(grid_size_x, grid_size_y):
  map = []
  
  for y in range(grid_size_y+1):
    line = [] 

    for x in range(grid_size_x+1):
      line.append('.')
    map.append(line)
  return map

def count_map(map):
  count = 0

  for line in map:
    for x in line:
      if x == "#":
        count += 1

  return count

def fold_map(x,y, map):

  new_map = []

  if x != 0: #fold in the x direction

    #print("folding in x new map of size " + str(x) +"x"+str(len(map)))
    new_map = initialize_map(x-1,len(map)-1)
    
    for y2 in range(len(map)):
      for x2 in range(len(map[0])):
        if x2 < x:
          new_map[y2][x2] = map[y2][x2]  #transfer marks in bound
        else: #translate new x values and check for marks
          if map[y2][x2] == '#':
            #x2 == old y value
            #x == folding line
            new_x = abs(x2-2*x)
            new_map[y2][new_x] = '#'

  else: #fold in the y direction

    #print("folding in y new map of size " + str(len(map[0])) +"x"+ str(y))
    new_map = initialize_map(len(map[0])-1,y-1)

    for y2 in range(len(map)):
      for x2 in range(len(map[0])):
        if y2 < y:
          new_map[y2][x2] = map[y2][x2]
        else: #translate new y values and check for marks
          if map[y2][x2] == '#':
            #y2 == old y value
            #y == folding line
            new_y = abs(y2-2*y)

            new_map[new_y][x2] = '#'

  #pprint.pprint(new_map)
  return new_map


def main():

  raw_input = process_input(13, "input.txt")

  #print(raw_input)

  input_list = []

  #process list further
  for i in range(len(raw_input)):
    if raw_input[i] == '':
      end_of_coords = i
  
  folding_instructions = []
  folding_values = []

  for i in range(end_of_coords+1,len(raw_input),):
    folding_instructions.append(raw_input[i])

  for i in folding_instructions:
    temp = i.split()
    temp2 = temp[2].split('=')

    print(temp2)

    if temp2[0] == 'x':
      temp3 = [int(temp2[1]),0]
    else:
      temp3 = [0, int(temp2[1])] 
    
    folding_values.append(temp3)
  
  #print(folding_values)

  coords = []

  for i in range(end_of_coords):
    coords.append(char_array_to_int(raw_input[i].split(',')))

    #input_list.append(raw_input[i].split('-'))  ##strip newline

  print(coords)
  print(folding_instructions)
  print(folding_values)

  #initialize map
  map = []

  #determine grid size
  grid_size_x = 0
  grid_size_y = 0

  for i in range(len(coords)):
    if coords[i][0] > grid_size_x:
      grid_size_x = coords[i][0]
    if coords[i][1] > grid_size_y:
      grid_size_y = coords[i][1]
  
  print("Map is " + str(grid_size_x)+" by "+str(grid_size_y))

  map = initialize_map(grid_size_x, grid_size_y)

  #plot coords onto map
  for line in coords:
    map[line[1]][line[0]] = '#'



  part1_map = fold_map(folding_values[0][0], folding_values[0][1], map)

  part1 = count_map(part1_map)

  for i in folding_values:
    map = fold_map(i[0], i[1], map)



  #answer
  print("Part 1:")
  print(part1)

  print("Part 2:")

  for line in map:
    print(line)

  
if __name__== "__main__":
  main()

