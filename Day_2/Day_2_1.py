
def process_command(current_pos, command):

  x = command.split()

  #print(x)

  direction = x[0]
  magnitude = int(x[1])
  new_position =[0,0]

  if direction == 'forward':
    new_position[0] = current_pos[0]+magnitude
    new_position[1] = current_pos[1]

  elif direction == 'up':
    new_position[0] = current_pos[0]
    new_position[1] = current_pos[1]-magnitude

  elif direction == 'down':
    new_position[0] = current_pos[0]
    new_position[1] = current_pos[1]+magnitude

  else:
    #print(new_position)
    print("Input Error")

  return new_position


def main():
  print("AOC_2021_Day_2_1")
  file_object  = open("/home/dkaulukukui/Documents/AdventOfCode2021/Day_2/input.txt", "r")

  raw_list = []
  input_list = []


  #read each line into raw list for processing
  for line in file_object:
      raw_list.append(line)

  #process list into list of integers
  for i in range(len(raw_list)):
    input_list.append(raw_list[i].strip('\n'))  ##strip newline
    #print(input_list)

  #do stuff
  current_pos = [0,0]
  
  for i in range(len(input_list)):
    current_pos = process_command(current_pos, input_list[i])
    #print(current_pos)

  print(current_pos)

  answer = current_pos[0]*current_pos[1]

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

