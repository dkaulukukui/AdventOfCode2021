
def binaryStr_to_int(binary_list):
   num = 0
   for x in range(len(binary_list)):
     magnitude = pow(2,(len(binary_list)-(x+1)))
     num = num + magnitude*binary_list[x]
   return num  

def gamma_to_epsilon(gamma):
  epsilon = [0]*len(gamma)
  for x in range(len(gamma)):
    if gamma[x]== 0:
      epsilon[x] = 1
    else:
      epsilon[x] = 0
  return epsilon

def main():
  Day = 3
  print("AOC_2021_Day "+ str(Day))
  file_object  = open("/home/dkaulukukui/Documents/AdventOfCode2021/Day_"+str(Day)+"/input.txt", "r")

  raw_list = []
  input_list = []


  #read each line into raw list for processing
  for line in file_object:
      raw_list.append(line)

  #process list into list of integers
  for i in range(len(raw_list)):
    input_list.append(raw_list[i].strip('\n'))  ##strip newline
  print(input_list)

  #do stuff

  bit_count = [0]*len(input_list[0])

  for i in range(len(input_list)):
    for x in range(len(input_list[i])):
      if input_list[i][x] == '1':
        bit_count[x] = bit_count[x]+1

  print(bit_count)
  
 
  
  gamma = [0]*len(input_list[0])
  #gamma
  for x in range(len(input_list[0])):
    if bit_count[x] > len(input_list)/2 :
      gamma[x] = 1
    else:
      gamma[x] = 0

  #convert to binary
  print (gamma)
  gamma_int = binaryStr_to_int(gamma)
  print(gamma_int)

  #epsilon =  

  epsilon = gamma_to_epsilon(gamma)
  print(epsilon)
  epsilon_int = binaryStr_to_int(epsilon)
  print(epsilon_int)


  answer = gamma_int*epsilon_int

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

