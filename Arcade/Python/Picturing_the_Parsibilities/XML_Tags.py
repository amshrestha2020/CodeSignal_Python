import xml.etree.ElementTree as ET

def solution(xml):
    root = ET.fromstring(xml)
    dictionary = dict()
    answer =  rec(root,0,[], dictionary)
    print(dictionary)
    return ["{}({})".format(x,", ".join(dictionary[x])) for x in answer]
def rec(root, deep, arr, dictionary):
    tag = root.tag
    prefix = "--" * deep
    attribs = sorted(root.attrib)
    
    line = prefix + tag 
    if line not in dictionary:
        dictionary[line] = attribs
        arr.append(line)
    else:
        x = dictionary[line]
        dictionary[line] = sorted(list(set(attribs+x)))
    for x in root:
        rec(x, deep+1, arr, dictionary)
    return arr