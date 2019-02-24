import datetime
import logging


def main():
    logging.info("Run date : "+str(datetime.datetime.now()))

    a = open('/path/to/input.txt','r')
    
    ignore = ['Ltd.', 'Ltd', 'Mr.', 'Mr', 'Miss.', 'Miss', 'Ms.', 'Ms', 'Mrs.', 'Mrs',
              '.', '_', '-', ',', '@', '#', '$', '%', '^', '&' ,'*', '(', ')', 
              '+','"', "\\", 'A/C' ,'/', 'co', 'Corp', 'ASSU', ';', "'"]
    
    
    look = open('/path/to/look_up.csv','r')
    look_dict = {}
    for j in look:
        val = j[:-1].split(',')
        if not val[0] == '':
            look_dict[val[0]]=val[1]

    #print(fgh)
    
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
    
    b.write('name_1|name_2|some|curreny|ccy_code|match_rate\n')
    
    for line in a:
        cells = line[:-1].split('|')
        name_1 = transform(cells[0])
        name_2 = transform(cells[1])
        
        
        match = 0
        for ele in name_1:
            if ele in name_2:
                match += 1
        if len(name_1)>len(name_2):
            total=len(name_1)
        else:
            total=len(name_2)
        match_rate=(match/total)*100
        cells.append(look_dict.get(cells[-1],'NA'))
        cells.append(str(match_rate)+'\n')
        
        b.write('|'.join(cells))
    
    b.close()
    logging.info("file written successfully")
    logging.info("----------------------------------------------------------------")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="/path/to/logfile.txt", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    try:
        main()
    except:
        logging.exception("")
        logging.info("----------------------------------------------------------------")
