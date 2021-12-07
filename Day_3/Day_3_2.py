def binaryStr_to_int(binary_list):
   num = 0
   for x in range(len(binary_list)):
     magnitude = pow(2,(len(binary_list)-(x+1)))
     num = num + magnitude*binary_list[x]
   return num  

def common_bit_count(input_list):
  #identify most common bits in list
  bit_count = [0]*len(input_list[0])

  for i in range(len(input_list)):
    for x in range(len(input_list[i])):
      if input_list[i][x] == '1':
        bit_count[x] = bit_count[x]+1

  #print(bit_count)
  return bit_count

def O2_generator(input_list):
  for i in range(len(input_list[0])): #filter the input list for each bit provided

    bit_count = common_bit_count(input_list)

    #print("checking bit #" + str(i))
    #print(bit_count)
    #print(input_list)

    if bit_count[i] > len(input_list)/2:  # 1 is the most common bit"
      #print("common bit is 1")
      for elem in list(input_list):
        if elem[i] == '0':
          input_list.remove(elem)  #remove all elements that dont start with 1
    elif bit_count[i] < len(input_list)/2:  # 0 is the most common bit
      #print("common bit is 0")
      for elem in list(input_list):
        if elem[i] == '1':
          input_list.remove(elem)  #remove all elements that dont start with 0 
    else:  #equal value or 0s and 1s, keep values with 1
      for elem in list(input_list):
        if elem[i] == '0':
          input_list.remove(elem)  #remove all elements that dont start with 1 

    #print(input_list)

    if len(input_list) == 1:
      print("O2 generator number is ")
      int_answer = [int(i) for i in list(input_list[0])]
      print(int_answer)
      return int_answer      

def CO2_scrubber(input_list):
  for i in range(len(input_list[0])): #filter the input list for each bit provided

    bit_count = common_bit_count(input_list)

    #print("checking bit #" + str(i))
    #print(bit_count)
    #print(input_list)

    if bit_count[i] > len(input_list)/2:  # 1 is the most common bit"
      for elem in list(input_list):
        if elem[i] == '1':
          input_list.remove(elem)  #remove all elements that dont start with 0
    elif bit_count[i] < len(input_list)/2:  # 0 is the most common bit
      for elem in list(input_list):
        if elem[i] == '0':
          input_list.remove(elem)  #remove all elements that dont start with 1 
    else:  #equal value or 0s and 1s, keep values with 1
      for elem in list(input_list):
        if elem[i] == '1':
          input_list.remove(elem)  #remove all elements that dont start with 0 

    #print(input_list)

    if len(input_list) == 1:
      print("CO2 scrubber number is ")
      int_answer = [int(i) for i in list(input_list[0])]
      print(int_answer)
      return int_answer 



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
  #print(input_list)

  #do stuff



  O2_gen_int = binaryStr_to_int(O2_generator(list(input_list)))
  print(O2_gen_int)

  CO2_scrubber_int = binaryStr_to_int(CO2_scrubber(list(input_list)))
  print(CO2_scrubber_int)

  answer = O2_gen_int*CO2_scrubber_int

  #answer
  print(answer)
  
if __name__== "__main__":
  main()

