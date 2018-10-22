def convert(value):
  if value=="A" or value== "B" or value=="C":
    return str(2)
  
  if value=="D" or value=="E" or value=="F":
    return str(3)

  if value=="G" or value=="H" or value=="I":
    return str(4)

  if value=="J" or value=="K" or value=="L":
    return str(5)

  if value=="M" or value=="N" or value=="O":
    return str(6)

  if value=="P" or value=="Q" or value=="R" or value=="S":
    return str(7)
  
  if value=="T" or value=="U" or value=="V" or value=="W":
    return str(8)

  if value=="X" or value=="Y" or value=="Z":
    return str(9)




while True:
  y=[]
  fake_number=input("Enter any alpha-numeric phone number (should have 11 characters(excluding the dashes) eg. 1-800-ABCDEFG, 2-ABCDEGFGHIJ\n")
  fake_number=fake_number.split("-")
  for i in fake_number:
    for j in i:
      if ord(j) in range(65, 91) or ord(j) in range(97, 123):
        j=j.upper()
        j=convert(j)
        y.append(str(j))

      else:
        y.append(str(j))

  print(y[0]+"-"+y[1]+y[2]+y[3]+"-"+y[4]+y[5]+y[6]+"-"+y[7]+y[8]+y[9]+y[10])


