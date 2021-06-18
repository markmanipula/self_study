list_expenses = []

file1 = open("day_1_data.txt", "r")
lines = file1.readlines()
#put items in list
for line in lines:
      list_expenses.append(int(line))

product = 0

#this solution is SLOW AF
for i in list_expenses:
      for j in list_expenses:
            for k in list_expenses:
                  if i + j + k == 2020:
                        product = i * j * k

print(product)