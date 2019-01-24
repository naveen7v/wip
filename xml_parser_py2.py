import xml.etree.cElementTree as ET
import glob

fp=glob.glob('/home/nav/Python/xml/*')

for i in fp:
    tree = ET.parse(i)
    root = tree.getroot()
    
    for att in root.iter():
        
            if len(att.attrib)==0:
                print(att.tag+' '+att.text)
            else:
                print(att.tag+' '+str(att.attrib))
    print('----------------------------------------------------------------------------------')
    
    
#clean solution

from xml.etree import ElementTree
tree = ElementTree.parse('input.xml')
root = tree.getroot()

for att in root:
    first = att.find('attval').text
    for subatt in att.find('children'):
        second = subatt.find('attval').text
        print('{},{}'.format(first, second))
