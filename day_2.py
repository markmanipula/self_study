passwords = []
passing_password_count = 0

# for line in txt_file:
# str= line.rstrip("\n")
# for line in txt_file:

file1 = open("day_2_data.txt", "r")
lines = file1.readlines()

for line in lines:
      #this is my key value pair
      key, value = line.split(": ")
      #print(key, value)
      min_count, max_count = key.split(" ")[0].split("-")
      #print(min_count, max_count)
      input_password = key.split(" ")[1]
      #print(v)

      if int(min_count) <= value.count(input_password) <= int(max_count):
            passwords.append(value)
     
#print(key, value, min_count, max_count, v)
print(len(passwords))

# def print_stars(stars):
#       for i in range(stars, 0, -1):
#             print("")
#             for j in range(i, stars):
#                   print("*", end="")
#       for i in range(0, stars):
#             print("")
#             for j in range(i, stars):
#                   print("*", end="")
