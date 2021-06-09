import string
def rotate(l, n):
    return l[-n:] + l[:-n]

def _rack(r):
    s = {'rack':r,'letters':[],'counts':[]}
    for i in s['rack']:
        if i not in s['letters']:
            s['letters'].append(i)
            s['counts'].append(s['rack'].count(i))
    return s
    
def scrabble_prob(split_rack,useWilds):
    bag = {
    'letters':list(string.ascii_uppercase + "?"), 
    'counts':[9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1,2]
    }
    prob,_prob=1,1
    wildstr = []
    wilds = []
    if useWilds == True:
        rack_x = sorted(split_rack['rack'])
        for k in range(0,len(split_rack['rack'])):
           rack_x.sort()                
           rack_x = rotate(rack_x,k)                            
           y = rack_x.pop(len(rack_x)-1)
           rack_x.append("?")
           rack_y = ''.join(rack_x)
           if sorted(rack_y) not in wildstr: 
               wilds.append(_rack(rack_y))
           wildstr.append(sorted(rack_y))
           for h in range(0,len(split_rack['rack'])-1):
               z = rack_x.pop(0)
               rack_x.append("?")
               rack_y = ''.join(rack_x)
               if sorted(rack_y)  not in wildstr: 
                   wilds.append(_rack(rack_y))
               wildstr.append(sorted(rack_y))
               rack_x.pop()
               rack_x.append(z)
           rack_x.pop(rack_x.index("?"))
           rack_x.append(y)
    for i in split_rack['letters']:
        rack_count = split_rack['counts'][split_rack['letters'].index(i)]
        tile = bag['letters'].index(i)
        bag_count = bag['counts'][tile]
        for j in range(0,rack_count):
         prob *= (bag_count / sum(bag['counts']))
         bag['counts'][tile] -= 1
    print(''.join(sorted(split_rack['rack'])), "{:.10f}".format(prob*100),"%")
    for K in wilds:
            _prob = 1
            bag['counts'] = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1,2]
            for k in K['letters']:
                rack_count = K['counts'][K['letters'].index(k)]
                tile = bag['letters'].index(k)
                bag_count = bag['counts'][tile]
                for i in range(0,rack_count):
                    _prob *= (bag_count / sum(bag['counts']))
                    #print(_prob, bag_count, "/", sum(bag['counts']))
                    bag['counts'][tile] -= 1
            print(''.join(sorted(K['rack'])), "{:.10f}".format(_prob*100),"%")
            prob += _prob       
    if useWilds: print("{:.10f}".format(prob*100),"%")
        
        
print('Enter rack: ')
input_rack = input()
print('Use blanks? Y/N')
blanks = input()
if blanks in ["y","Y"]: 
    useWilds = True 
else: 
        useWilds = False
scrabble_prob(_rack(input_rack), useWilds
)
