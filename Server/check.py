def set_array(begin, begin4, map):
	len1 = len(map)
	len2 = len(map[0])
	for x in xrange(begin[0]+1,len1):
		if map[x][begin[1]] != 0:
			begin4[1][1] = x-1
			break
	for x in xrange(0, begin[0]):
		if map[begin[0]-x-1][begin[1]] != 0:
			begin4[1][0] = begin[0]-x
			break
	for x in xrange(begin[1]+1,len2):
		if map[begin[0]][x] != 0:
			begin4[0][1] = x-1
			break
	for x in xrange(0, begin[1]):
		if map[begin[0]][begin[1]-x-1] != 0:
			begin4[0][0] = begin[1]-x
			break

def find_way(begin, end, map):
	"""
	:type begin: [int,int]
	:type end: [int,int]
	:type map: List[List[int]]
	:rtype: [bool,[int,int],[int,int]]
	"""
	len1 = len(map)
	len2 = len(map[0])
	begin4 = [[0, len2-1],[0, len1-1]]
	end4 = [[0, len2-1],[0, len1-1]]
	set_array(begin, begin4, map)
	set_array(end, end4, map)
	print begin4
	print end4
	row = [val for val in [a for a in xrange(begin4[0][0],begin4[0][1]+1)] if val in [b for b in xrange(end4[0][0],end4[0][1]+1)]]
	col = [val for val in [a for a in xrange(begin4[1][0],begin4[1][1]+1)] if val in [b for b in xrange(end4[1][0],end4[1][1]+1)]]
	print row
	print col
	flag = False
	not_return = False
	for x in row:
		not_return = False
		for y in xrange(begin[0]+1,end[0]):
			if map[y][x] != 0:
				not_return = True
				break;
		if not not_return:
			if begin[0]==end[0]:
				return [True,None,None]
			return [True, [begin[0], x], [end[0], x]]
	for x in col:
		not_return = False
		for y in xrange(begin[1]+1,end[1]):
			if map[x][y] != 0:
				not_return = True
				break;
		if not not_return:
			if begin[1]==end[1]:
				return [True,None,None]
			return [True, [x, begin[1]], [x, end[1]]]
	return [False, None, None]

def check_points(begin,end,map):
	if begin == end:
		return [False,None,None]
	if map[begin[0]][begin[1]]!=map[end[0]][end[1]]:
		return [False,None,None]
	return find_way(begin, end, map)