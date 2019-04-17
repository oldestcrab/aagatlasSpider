data = {
    'GeneSymbol':'GeneSymbol',
    'Disease':'Disease',
    'PubMed_ID':'PubMed_ID',
    'Sentence':'Sentence',
    'update_time':'1'
}
# print(data)
keys = ', '.join(x for x in data.keys())
# print(keys)
values = ', '.join(['%s']*len(data))
# print(values)
sql = 'insert in {table}({keys}) values({values});'.format(table='self.table', keys=keys, values=values)
a = data.values()
print(a)
print(type(tuple(a)))
print(tuple(a)*2)