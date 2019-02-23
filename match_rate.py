
a = open('/path/to/file.txt','r')

# order in the list is the order of removal

ignore = ['Ltd.', 'Ltd', 'Mr.', 'Mr', 'Miss.', 'Miss', 'Ms.', 'Ms', 'Mrs.', 'Mrs',
          '.', '_', '-', ',', '@', '#', '$', '%',
          '^', '&' ,'*', '(', ')','+','"', "\\", 'A/C' ,'/', 'co', 'Corp', 
          'ASSU', ';', "'"]


look = open('/path/to/look_up.csv','r')
look_dict = {}
for j in look:
    val = j[:-1].split(',')
    if not val[0] == '':
        look_dict[val[0]]=val[1]
    



def transform(name):
    name_space = name
    
    for cha in ignore:
        if cha in name_space:
            name_space = name_space.replace(cha, ' ')
    
    name_space = name_space.split(' ')
    new_name = []
    for i in name_space:
        if not len(i) == 0:
            new_name.append(i)
            
    return new_name


b = open('/path/to/output.txt','w')

a = a.readlines()[1:]

b.write('first_name|second_name|some|curreny|curr_code|match_rate\n')

for line in a:
    cells = line[:-1].split('|')
    first = transform(cells[0])
    second = transform(cells[1])
    
    match = 0
    for ele in first:
        if ele in second:
            match += 1
    if len(first)>len(second):
        total=len(first)
    else:
        total=len(second)
    match_rate=(match/total)*100
    
    cells.append(look_dict.get(cells[-1],'NA'))
    cells.append(str(match_rate)+'\n')
    
    b.write('|'.join(cells))

b.close()
