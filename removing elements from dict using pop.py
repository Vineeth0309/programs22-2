Record = {'id' : 101, 'name' : 'Vineeth Kumar', 'age' : 24}
print("Record...")
print(Record)
ele = Record.pop('id')
print('Deleted value is:', ele)
ele = Record.pop('age')
print('Deleted value is:', ele)
print("Record after deleting the elements...")
print(Record)
