fname = "last_range_finally (2)"


	
readFile = open(fname)
lines = readFile.readlines()
readFile.close()

w = open("last_range_finally", "w")
w.writelines([i for i in lines[:-1]])

w.close()