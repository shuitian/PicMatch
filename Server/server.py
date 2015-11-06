import json
import check
import map1
# string = '{"begin":[1,2], "end":[1,2]}'
def get_data_from_json(string):
	return json.loads(string)

data1 = '{"begin":[1,4], "end":[1,2]}'
jsondata =  get_data_from_json(data1)
begin = jsondata['begin']
end = jsondata['end']
print check.check_points(begin,end,[[0,0,0,0,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]])

