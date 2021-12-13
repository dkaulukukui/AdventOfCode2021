import pprint

def split(word):
    return [char for char in word]

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def update_signal_possibilities(signal_possibilites, input):
  segments_to_remove = ['a','b','c','d','e','f','g']

  for i in input:  #filter complete list to everything but what was provided
    segments_to_remove.remove(i)
  
  for i in segments_to_remove:  #remove filtered list from signal possibilities
    if i in signal_possibilites:
      signal_possibilites.remove(i)

  return signal_possibilites

def does_string_contain_chars(input_string, input_chars):
  counter = 0

  #print("checking if " + input_string +" contains" + str(input_chars))
  
  for i in range(len(input_chars)):
    if input_string.find(input_chars[i]) != -1:
      #print("char " + input_chars[i]+ " found")
      counter += 1
    
  #print("counter = " + str(counter))
  
  if counter == len(input_chars):
    #print("true")
    return True
  else:
    #print("false")
    return False


def main():
  Day = 8
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
    input_list.append(raw_list[i].strip('\n').split(' | '))  ##strip newline

  #print(input_list)

  signal_patterns = []
  output_values = []

  for i in range(len(input_list)):
    signal_patterns.append(input_list[i][0].split())
    output_values.append(input_list[i][1].split())

  print(signal_patterns)
  print(output_values)

  # Seven Segment number segment counts:
  # # of segments  : display : potential segments
  # 2 : 1      : 1,2
  # 3 : 7      : 1,2,4
  # 4 : 4      : 1,2,5,6
  # 5 : 2,3,5  : ALL
  # 6 : 0,6,9  : ALL
  # 7 : 8      : ALL

  # segment order
  #  4444
  # 5    1
  # 5    1
  #  6666
  # 7    2
  # 7    2
  #  3333




  #print(segment_signal_possibilities)

  num_signal_patterns = len(signal_patterns)

  output_ints = []

  ##process the input and determine signal wire possibilities
  for i in range(num_signal_patterns):   ## for every signal pattern s

    print("**********************next inputs******************")

    signal_mappings = ['0','0','0','0','0','0','0','0','0','0']

    #run through twice to determine identifiers
    for x in range(2):
      for j in range(len(signal_patterns[i])):  ##look at each signal pattern
        length = len(signal_patterns[i][j])   ##determine the length
        
        if length == 2:  #digit is a 1
            signal_mappings[1] = split(signal_patterns[i][j])
        elif length == 4:  #digit is a 4

          signal_mappings[4] = split(signal_patterns[i][j])

          print(does_string_contain_chars(signal_patterns[i][j],signal_mappings[4]))

          #determine the diff between 1 and 4, to be used for other logics
          if len(signal_mappings[1]) == 2:  # signals for 1 have been defined
            four_diff = list(signal_mappings[4])
            four_diff.remove(signal_mappings[1][0])
            four_diff.remove(signal_mappings[1][1])
    
    #print("One = ")
    #print(signal_mappings[1])
    #print("Four Diff =")
    #print(four_diff)

    

    #deduce which signal wire goes to which segment
    for j in range(len(signal_patterns[i])):  ##look at each signal pattern
      length = len(signal_patterns[i][j])   ##determine the length

      if length == 2:  #digit is a 1
        print("digit = 1")

        #signal_mappings[1] = split(signal_patterns[i][j])
        
      elif length == 3:  #digit is a 7

        print("digit = 7")
        
        signal_mappings[7] = split(signal_patterns[i][j])

      elif length == 4:  #digit is a 4

        print("digit = 4")

        #signal_mappings[4] = split(signal_patterns[i][j])

        #determine the diff between 1 and 4, to be used for other logics
        #if len(signal_mappings[1]) == 2:  # signals for 1 have been defined
        #  four_diff = list(signal_mappings[4])
        #  four_diff.remove(signal_mappings[1][0])
        #  four_diff.remove(signal_mappings[1][1])
    
      elif length == 5:  #2,3,5

        if does_string_contain_chars(signal_patterns[i][j],signal_mappings[1]):
          # signals contains the segments from 1 so is a 3
          signal_mappings[3] = split(signal_patterns[i][j])

          print("digit = 3")
        elif does_string_contain_chars(signal_patterns[i][j],four_diff):
          #signal contains four_diff so is a 5
          signal_mappings[5] = split(signal_patterns[i][j])

          print("digit = 5")
        else: #else its a 2
          print("digit = 2")
          signal_mappings[2] = split(signal_patterns[i][j])

      elif length == 6:  #0,6,9
        if does_string_contain_chars(signal_patterns[i][j],signal_mappings[1]):
          # signals contains 1 so is a 0 or 9
          if does_string_contain_chars(signal_patterns[i][j],four_diff):
            #contains 1 and four diff so is a 9
            print("digit = 9")
            signal_mappings[9] = split(signal_patterns[i][j])

          else:
            #contains 1 but not fourdiff so is 0
            print("digit = 0")
            signal_mappings[0] = split(signal_patterns[i][j])
        else:
          #doesnt contain 1 so is a 6
          print("digit = 6")
          signal_mappings[6] = split(signal_patterns[i][j])            

      elif length == 7:
        signal_mappings[8] = split(signal_patterns[i][j])
    
    print(signal_mappings)
    print("processing outputs")
    
    output_digits = []

    for j in range(len(output_values[i])):  
    #for every output value
      print("output["+str(i)+"]["+str(j)+"] = ")

      length = len(output_values[i][j])   ##determine the length

      if length == 2:  #digit is a 1
        print("output digit = 1")
        output_digits.append(1)
        
      elif length == 3:  #digit is a 7

        print("output digit = 7")
        output_digits.append(7)
        

      elif length == 4:  #digit is a 4

        print("output digit = 4")
        output_digits.append(4)
    
      elif length == 5:  #2,3,5

        if does_string_contain_chars(output_values[i][j],signal_mappings[1]):

          print("output digit = 3")
          output_digits.append(3)
        elif does_string_contain_chars(output_values[i][j],four_diff):

          print("output digit = 5")
          output_digits.append(5)
        else: #else its a 2
          print("output digit = 2")
          output_digits.append(2)

      elif length == 6:  #0,6,9
        if does_string_contain_chars(output_values[i][j],signal_mappings[1]):
          # signals contains 1 so is a 0 or 9
          if does_string_contain_chars(output_values[i][j],four_diff):
            #contains 1 and four diff so is a 9
            print("output digit = 9")
            output_digits.append(9)

          else:
            #contains 1 but not fourdiff so is 0
            print("output digit = 0")
            output_digits.append(0)
        else:
          #doesnt contain 1 so is a 6
          print("output digit = 6") 
          output_digits.append(6)       

      elif length == 7:
        print("output digit = 8")
        output_digits.append(8)
        
    print("Output digits =" + str(output_digits))

    int_output = 1000*output_digits[0]+100*output_digits[1]+10*output_digits[2]+output_digits[3]
    
    print("Output ints = " + str(int_output))

    output_ints.append(int_output)

  print(output_ints)  

    
            

    


### part 1 ####
  counter = 0

  for i in range(len(output_values)):
    for j in range(len(output_values[i])):
      length = len(output_values[i][j])
      if length == 2 or length == 3 or length == 4 or length ==7:
        counter += 1

  #answer
  print("Part 1:")
  print(counter)

  print("Part 2:")
  print(sum(output_ints))

  
if __name__== "__main__":
  main()

