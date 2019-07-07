# Apriori Algoritm
# INPUTS
# No. of items
# Items
# OUTPUTS
# frequency
min_support_value=2

def remove_key(dict):
    for key in fi_matrix.keys():
        if fi_matrix[key]<min_support_value:
           dict.pop(key, None)
    print dict


pro=int(input("Number of inputs "))

tran_matrix=[]

for i in range(pro):
    inp=raw_input().split(",")
    tran_matrix.append(inp)


# find frequency

fi_matrix={}

for k in range(pro):
    for m in range(len(tran_matrix[k])):
        if tran_matrix[k][m] in fi_matrix:
            fi_matrix[tran_matrix[k][m]]+=1
        else:
            fi_matrix[tran_matrix[k][m]]=1

print "Before"
print fi_matrix
print "After"
remove_key(fi_matrix)

L1= list(fi_matrix)
print L1*L1











'''

li='1,2,3'
lis=li.split(',')

process = [[0] for i in range(pro)]
for i in xrange(len(fromto)):

    if fromto[i][0]==fromto[i][1]:
        last=process[fromto[i][0]][-1]
        process[fromto[i][0]].append(last+1)

    else:
        lastOfFrom=process[fromto[i][0]][-1]
        lastOfTo=process[fromto[i][1]][-1]

        if lastOfFrom>=lastOfTo:
            process[fromto[i][0]].append(lastOfFrom + 1)
            process[fromto[i][1]].append(lastOfFrom + 2)
        else:
            process[fromto[i][1]].append(lastOfTo + 2)
            process[fromto[i][0]].append(lastOfTo + 1)

print "Time stamps for the processes are: "+str(process)
'''
