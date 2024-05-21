from pandas import DataFrame, read_excel
from _laSort import LaneSorting, AisleSorting
#from _visualizer import visualize

columnumber = 0
rownumber = 0
sortedlist = []

table = read_excel('_layout.xlsx')
sortlist = table.columns.values.tolist()

table = table.transpose()

tbl = table.values.tolist()



while sortlist.__len__() > 0:
    SortStyle = sortlist[0]
    if 'Lane' in sortlist[0]:
        sortedlist.extend(LaneSorting(SortStyle, tbl[columnumber].copy()))
        columnumber += 1
        del sortlist[0]
        continue
    if 'Aisle' in sortlist[0]:
        sortedlist.extend(AisleSorting(SortStyle, tbl[columnumber].copy(), tbl[columnumber+1].copy()))
        columnumber += 2
        del sortlist[0]
        del sortlist[0]
        continue

sortedlist = [x for x in sortedlist if "nan" not in x]


#Only somewhat works
#visualize(sortedlist,table)

# Write bins in order - debug
#file = open('sortedbins.csv','w')
#for line in sortedlist:
#    file.writelines(line)
#    file.write("\n")

columns = ["Warehouse Number",	"Storage Bin",	"Activity",	"Sequence Number",	"Activity Area",	
           "Storage Type",	"Storage Section",	"Storage Bin Aisle",	"Sort Sequence",	"Distance to Start of Aisle",	
           "Aisle Length",	"Subsequent Aisle",	"Dist. to Subs. Aisle",	"Consolidation Group",	"Message Row"]

SortSequence = 1
activities = ["PICK","CLSP","INTL","INV","NOLM","PTWY","REPL","STCH"]
dictionary = {}

for activity in activities:
    for bin in sortedlist:
        binNumber = 1

        if bin[2] == 0 and bin[3] == 0:
            #placeholder - needs updating to handle non-standard bins
                datarow = { "Warehouse Number":bin[4],	
                            "Storage Bin":bin[0][0:7] + str(binNumber),
                            "Activity":"",
                            "Sequence Number":SortSequence,
                            "Activity Area":activity,	
                            "Storage Type":bin[0:3],	
                            "Storage Section":"",	
                            "Storage Bin Aisle":"",	
                            "Sort Sequence":SortSequence,	
                            "Distance to Start of Aisle":"",	
                            "Aisle Length":"",	
                            "Subsequent Aisle":"",	
                            "Dist. to Subs. Aisle":"",	
                            "Consolidation Group":"",	
                            "Message Row":""
                            }
                dictionary[SortSequence] = datarow
                SortSequence += 1
                binNumber +=1
        else:
            for pcks in range(1,int(bin[2])+1):
                datarow = { "Warehouse Number":bin[4],	
                            "Storage Bin":bin[0][0:7] + str(binNumber),
                            "Activity":"",
                            "Sequence Number":SortSequence,
                            "Activity Area":activity,	
                            "Storage Type":"0101",	
                            "Storage Section":"",	
                            "Storage Bin Aisle":bin[0][0:2],	
                            "Sort Sequence":SortSequence,	
                            "Distance to Start of Aisle":"",	
                            "Aisle Length":"",	
                            "Subsequent Aisle":"",	
                            "Dist. to Subs. Aisle":"",	
                            "Consolidation Group":"",	
                            "Message Row":""
                            }
                dictionary[SortSequence] = datarow
                SortSequence += 1
                binNumber +=1

            for reserve in range(1,int(bin[3])+1):
                datarow = { "Warehouse Number":bin[4],	
                            "Storage Bin":bin[0][0:7] + str(binNumber),
                            "Activity":"",
                            "Sequence Number":SortSequence,
                            "Activity Area":activity,	
                            "Storage Type":"0102",	
                            "Storage Section":"",	
                            "Storage Bin Aisle":bin[0][0:2],	
                            "Sort Sequence":SortSequence,	
                            "Distance to Start of Aisle":"",	
                            "Aisle Length":"",	
                            "Subsequent Aisle":"",	
                            "Dist. to Subs. Aisle":"",	
                            "Consolidation Group":"",	
                            "Message Row":""
                            }
                dictionary[SortSequence] = datarow
                SortSequence += 1
                binNumber +=1
            
sortedDF = DataFrame.from_dict(dictionary, orient='index')
sortedDF.to_csv("sort_sequence_upload.csv", index=False)
