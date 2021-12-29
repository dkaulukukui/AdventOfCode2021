import pprint

from collections import defaultdict
adj = defaultdict(list)

node_dict = defaultdict(list)

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

def paths (current, seen):
  if current == "end":
    return 1
  if current.islower() and current in seen:
    return 0
  seen = seen | {current}
  out = 0

  for thing in adj[current]:
    out += paths(thing,seen)
  return out

def paths2 (cur, seen, dup):
  if cur == 'end':
      return 1
  if cur == "start" and seen:
      return 0
  if cur.islower() and cur in seen:
      if dup is None:
          dup = cur
      else:
          return 0
  seen = seen | {cur}
  out = 0
  for thing in adj[cur]:
      out += paths2(thing, seen, dup)
  return out


def main():

  raw_input = process_input(12, "input.txt")

  input_list = []

  #process list further
  for i in range(len(raw_input)):
    input_list.append(raw_input[i].split('-'))  ##strip newline

  for line in raw_input:
    a, b = line.split("-")
    adj[a].append(b)
    adj[b].append(a)  

  print(adj)

  #convert to int array
  #int_input = char_array_to_int(input_list[0].split(','))
  
  #print(int_input)

  #node_dict = {}
  nodes = []

  for i in input_list:  #for each connection in list
    for j in i:  #process each node 
      if nodes.count(j) == 0:  #if node isnt in list of nodes
        nodes.append(j)        # add to list of nodes

  
  for elem in nodes:  #go through nodes to build neighbor dict
    neighbors = []
 
    for i in input_list:
      start = i[0]
      end = i[1]

      if elem == start and end not in neighbors:
        neighbors.append(end)
      elif elem == end and start not in neighbors:
        neighbors.append(start)

    node_dict [elem] = neighbors

  print(node_dict)

  #print(node_dict.keys())
  print("Input has total of " + str(len(node_dict)) + " nodes.")
  #print(node_dict)

  #####current state is a list of nodes and dict of nodes with neighbors


  ##find all paths

  out = paths("start", set())

  out2 = paths2("start", set(), None)
  
  #print (out)

  #answer
  print("Part 1:")
  print(out)

  print("Part 2:")
  print(out2)

  
if __name__== "__main__":
  main()

