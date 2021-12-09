import pprint

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def plot_line(coord_1, coord_2, map): 
  #given two sets of coordinates increment the counts of the provided map and return it
  
  x1 = coord_1[0]+1
  x2 = coord_2[0]+1
  y1 = coord_1[1]+1
  y2 = coord_2[1]+1

  # ax + by + c = 0
  # 

  if x2 != x1:
    slope = int((y2-y1)/(x2-x1))
  else:
    slope = 0

  y_offset = (y1-1) - (x1-1)*slope 

  #print(coord_1)
  #print(coord_2)
  #print("slope = " + str(slope))

  if (x1<=x2):
    x_start = x1-1
    x_end = x2-1
  else:
    x_start = x2-1
    x_end = x1-1

  if (y1<=y2):
    y_start = y1-1
    y_end = y2-1
  else: 
    y_start = y2-1
    y_end = y1-1

  if x1 == x2:  #if verticle line
    for y in range(y_start,y_end+1):
      map[y][x_start] += 1   
  elif y1 == y2: # horizontal line
    for x in range(x_start,x_end+1):
      map[y_start][x] += 1 
  else:  #45 degree
    for x in range(x_start,x_end+1):



        y = x*slope + y_offset
        #print("plotting diagonal")
        #print("x =" + str(x) + ", y =" + str(y))
        
        map[y][x] += 1

  #pprint.pprint(map)    

  return map


def main():
  Day = 5
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

#parse input into usable format
  #separate x1,y1 and x2,y2 values and convert to ints
  parsed_input = []

  for i in range(len(input_list)):
    temp_elem = input_list[i].split()
    temp_elem.remove('->')

    coord_1 = temp_elem[0].split(',')
    coord_2 = temp_elem[1].split(',')

    coord_1 = char_array_to_int(coord_1)
    coord_2 = char_array_to_int(coord_2)

    parsed_input.append([coord_1, coord_2])

    #print(parsed_input)
    
#input is now a 3D list of integers, [[[x1,y1],[x2,y2]],[[x3,y3],[x4,y4]], ...

  #setup map
  max_x = 10000
  max_y = 10000
  
  map = [[0 for col in range(max_x)] for row in range(max_y)]

  #do stuff 

  for i in range(len(parsed_input)):
    map = plot_line(parsed_input[i][0],parsed_input[i][1],map)

  #pprint.pprint(map)


  #determine max for the map
  max = 0 

  for x in range(max_x):
    for y in range(max_y):
      if map[y][x] > max:
        max = map[y][x]

  #count number of max values

  count = 0
  for x in range(max_x):
    for y in range(max_y):
      if map[y][x] >= 2:
        count += 1

  answer = count

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

