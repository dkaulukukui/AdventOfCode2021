def main():
  print("AOC_2021_Day_1_1")
  file_object  = open("/home/dkaulukukui/Documents/AdventOfCode2021/Day_1_1/input.txt", "r")

  raw_list = []
  input_list = []
  increases = 0

  #read each line into raw list for processing
  for line in file_object:
      raw_list.append(line)

  #process list into list of integers
  for i in range(len(raw_list)):
    input_list.append(int(raw_list[i].strip('\n')))  ##strip newline and convert to int

  #do stuff
  for i in range(1,len(input_list)):
    x = input_list[i]
    
    y = input_list[i-1]

    if (x > y):
      increases += 1



  print(increases)
  
if __name__== "__main__":
  main()

