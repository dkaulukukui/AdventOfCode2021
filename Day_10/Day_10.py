import pprint

def split(word):
    return [char for char in word]

def char_array_to_int(char_array):
  
  int_array = []

  for elem in char_array:
    int_array.append(int(elem))

  return int_array

def print_error(expected, value):
  print("Expected " + str(expected[0]) + " , but found " + str(value) + " instead.")

def main():
  Day = 10
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


  #convert to int array
  #int_input = char_array_to_int(input_list[0].split(','))
  
  #print(int_input)

  #do stuff

  opening_chars = ['(','{','[','<']
  closing_chars = [')','}',']','>']

  illegal_chars = []

  for i in range(len(input_list)):  # for each line of input

    nesting_level_char = []

    print("Checking line # " + str(i))
     
    for j in range(len(input_list[i])):
      current_char = input_list[i][j]

      print("checking char " + str(current_char) +  " #" + str(j))

      if current_char in opening_chars:  ## opening symbol
        print("Opening chunk with " + str(current_char))

        nesting_level_char.append(current_char)

        #print("Currently " + str(len(nesting_level_char)) + " Levels deep")

        
      elif current_char in closing_chars:  ##closing symbol
        closing_symbol = nesting_level_char.pop()
        index = opening_chars.index(closing_symbol[0])
        print(str(closing_symbol) + " at index " + str(index))

        print(nesting_level_char)
        
        if closing_chars[index] == current_char:
          print("closing level " + str(len(nesting_level_char) + 1) + " with " + str(current_char))

        else:
          illegal_chars.append(current_char)
          print("Line " + str(i) + " ERROR")
          print_error(closing_symbol, current_char)
          break


  print("Illegal Chars found: ")
  print(illegal_chars)

  part1_answer = 0

  for i in illegal_chars:
    if i == ')':
      part1_answer += 3
    elif i == ']':
      part1_answer += 57
    elif i == '}':
      part1_answer += 1197
    elif i == '>':
      part1_answer += 25137
    else:
      print("MAJOR ERROR!!!!!!!!!!!!!!!!!")

  #answer
  print("Part 1:")
  print(part1_answer)

  print("Part 2:")
  print("NULL")

  
if __name__== "__main__":
  main()

