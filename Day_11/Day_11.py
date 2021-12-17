import pprint
import logging,sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def split(word):
    return [int(char) for char in word]

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def main():
  Day = 11
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
    input_list.append(split(raw_list[i].strip('\n')))  ##strip newline

  print(input_list)

  num_step = 100
  num_flashes = 0

  for i in range(num_step): #iterate the # of steps indicated

    logging.debug("step " + str(i+1))

     #increment energy levels

    flashed = [] #keep track of what octopi flashed each step
    pos_to_update = []
     
    for y in range(len(input_list)):  #increment entire field
        for x in range(len(input_list[y])): 
            pos_to_update.append([y,x])

    #logging.debug(pos_to_update)

    while len(pos_to_update) != 0: 
        pos = pos_to_update.pop()
        pos_x = pos[1]
        pos_y = pos[0]

        #logging.debug("checking " + str(pos))

        input_list[pos_y][pos_x] += 1 #increment field

        if pos not in flashed and input_list[pos_y][pos_x] >= 10:
            flashed.append(pos)

            # add all adjacent positions to pos to update queue
            if pos_x > 0:  # left
                pos_to_update.append([pos_y,pos_x-1])
            if pos_x < len(input_list[pos_y])-1:  #right
                pos_to_update.append([pos_y,pos_x+1])
            if pos_y > 0:  # up
                pos_to_update.append([pos_y-1,pos_x])
            if pos_y < len(input_list)-1:  #down
                pos_to_update.append([pos_y+1,pos_x])            
            if pos_x > 0 and pos_y > 0:  # left/up
                pos_to_update.append([pos_y-1,pos_x-1])                
            if pos_x > 0 and pos_y < len(input_list)-1:  # left/down
                pos_to_update.append([pos_y+1,pos_x-1]) 
            if pos_x < len(input_list[pos_y])-1 and pos_y > 0:  #right/up
                pos_to_update.append([pos_y-1,pos_x+1])            
            if pos_x < len(input_list[pos_y])-1 and pos_y < len(input_list)-1:  #right/down
                pos_to_update.append([pos_y+1,pos_x+1])    

    #logging.debug("flashed ")
    #logging.debug(flashed)
    for pos in flashed: #set all flashed to 0
        input_list[pos[0]][pos[1]]= 0 
    
    logging.debug(input_list)

    num_flashes += len(flashed)
    #print(flashed)

  #answer
  print("Part 1:")
  print(num_flashes)

  print("Part 2:")
  print("NULL")

  
if __name__== "__main__":
  main()

