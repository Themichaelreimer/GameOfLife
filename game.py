
def build_adjacents(x,y):
	result = []
	for i in range(-1,2):
		for j in range(-1,2):
			result.append( (x+i,y+j) )
	return result

def is_alive(cell):
	return cell in alive_cells

def count_neighbors(cell):
	neighs = build_adjacents(cell[0],cell[1])
	count = 0

	for n in neighs:
		if is_alive(n):
			count += 1
	return count

def alive_case(cell):
	count =  count_neighbors(cell)
	count == 3 or count == 4:
		return True
	return False

def empty_case(cell):
	count = count_neighbors(cell)
	if count == 3:
		return True
	return False

#FACTS 
alive_cells = set()

for x in range(37):
	alive_cells.add((x,1))

while True:
	new_list = set()

	#LOGIC

	cells_to_consider = set()

	#Build set of cells to consider
	for cell in alive_cells:
		for new_cell in build_adjacents(cell[0],cell[1]):
			cells_to_consider.add(new_cell)


	for cell in cells_to_consider:
		if is_alive(cell):
			if alive_case(cell):
				new_list.add(cell)
		else:
			if empty_case(cell):
				new_list.add(cell)


	#/LOGIC

	alive_cells = new_list.copy()

	# DRAWING
	
	print("---------------------------------")
	for y in range(-30,30):
		for x in range(-30,30):
			if is_alive((x,y)):
				print("X",end="")
			else:
				print("_",end="")
		print("\n",)
	print("----------------------------------")

	line = input("Press any key to continue...")




