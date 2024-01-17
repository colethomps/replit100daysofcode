import os

f = open("100MostStreamedSongs.csv", "r")
lines = f.readlines()
f.close()

for i in range(len(lines)):
  lines[i] = lines[i].split(",")
  
  print(lines[i][0], lines[i][1], lines[i][2], lines[i][3],lines[i][4])
  
  folderPath = str(lines[i][3]) + "/"
  
  if os.path.exists(folderPath):
    pass
  else:
    os.mkdir(folderPath)

  fileName = folderPath + str(lines[i][1]) + ".txt"
  
  if os.path.exists(fileName):
    pass
  else:
    f = open(fileName, "w")
    f.write(str(lines[i][2])+ "\n"+str(lines[i][4]))
    f.close()

