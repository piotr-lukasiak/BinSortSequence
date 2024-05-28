def AisleSorting(SortStyle, Aisle1, Aisle2):
    SortedAisle = []
    if 'AisleZig' in SortStyle: 
        while len(Aisle1)+len(Aisle2) > 0:
            if len(Aisle1) > 0:            
                SortedAisle.append(str(Aisle1[0])+"."+SortStyle)
                del Aisle1[0]
            if len(Aisle2) > 0:     
                SortedAisle.append(str(Aisle2[0])+"."+SortStyle)
                del Aisle2[0]
            continue
    if 'AisleReverseZig' in SortStyle: 
        while len(Aisle1)+len(Aisle2) > 0:
            if len(Aisle2) > 0:   
                SortedAisle.append(str(Aisle2[-1])+"."+SortStyle)
                del Aisle2[-1]
            if len(Aisle1) > 0: 
                SortedAisle.append(str(Aisle1[-1])+"."+SortStyle)
                del Aisle1[-1]
            continue

    if 'AisleUPick' in SortStyle:
        while len(Aisle1)+len(Aisle2) > 0:
            for x in range(2,int(SortStyle[-1])+1):
                if len(Aisle1) > 0:
                    SortedAisle.append(str(Aisle1[0]+"."+SortStyle))
                    del Aisle1[0]
            for x in range(2,int(SortStyle[-1])+1):
                if len(Aisle2) > 0:
                    SortedAisle.append(str(Aisle2[0]+"."+SortStyle))
                    del Aisle2[0]
    if 'AisleReverseUpick' in SortStyle:
        while len(Aisle1)+len(Aisle2) > 0:
            for x in range(2,int(SortStyle[-1])+1):
                SortedAisle.append(str(Aisle1[-1])+"."+SortStyle)
                del Aisle1[-1]
            for x in range(2,int(SortStyle[-1])+1):
                SortedAisle.append(str(Aisle2[-1])+"."+SortStyle)
                del Aisle2[-1]


    return [str(x).split(".") for x in SortedAisle]


def LaneSorting(SortStyle, Lane):
    SortedLane = []
    
    if 'Lane' in SortStyle:
        SortedLane = [str(x)+"."+SortStyle for x in Lane]

    if 'LaneReverse' in SortStyle:
        SortedLane = [str(x)+"."+SortStyle for x in Lane[::-1]]
        
    return [str(x).split(".") for x in SortedLane]