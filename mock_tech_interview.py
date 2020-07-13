# Print out each element of the following array on a separate line:
things = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# define the list
# iterate through the list
# print each element
# each element needs to be printed in new line

# for loop iterates through the list and get value represented by i
for i in things:
  # format the elements value to return with new line
  print(f"{i}\n")

############## STRETCH  
# Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:

# For the above input, the expected output is:
# Bob
# Slack
# reddit
# 89
# 101
# alacritty
# (brackets)
# 5
# 375
# 0
# {slice, owned}
# 22
# ```
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# the list has nested lists
# the expected output is all elements regardless of what list they are input
# define the list
# iterate through the list
# ignore nested lists to printed
# only consider index values to be print
# first loop will get to third index and see list -
#  should then loop through that list
# check to see if the index type is list if index type is list then start new for loop
# print each element ValueError

stretch_list = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# for i in stretch_list:
#   if type(i) is list:
#     for v in i:
#       if type(v) is list:
#         for e in v:
#           print(f"{e}\n")
#       else:
#         print(f"{v}\n")
#   else:
#     print(f"{i}\n")

# check each index type is list or not if index type is list start new loop
# create a function that loops and calls itself if the index type is a list
print("**********STRETCH*********")
def loop(value):
  for i in value:
    if type(i) is list:
      loop(i)
    else:
      print(f"\n{i}")

loop(stretch_list)