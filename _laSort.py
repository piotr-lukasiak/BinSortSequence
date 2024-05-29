def AisleSorting(SortStyle, Aisle1, Aisle2):
    SortedAisle = []
 
 #Zigzag sort
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

#U-Pick sort
    if 'AisleUPick' in SortStyle:
        binsPickedPerLane = int(SortStyle.split(".")[0][-1])
        while len(Aisle1)+len(Aisle2) > 0:
            for x in range(0,binsPickedPerLane)[::-1]:
                if len(Aisle1) > 0:
                    SortedAisle.append(str(Aisle1[0])+"."+SortStyle)
                    del Aisle1[0]
            for x in range(0,binsPickedPerLane)[::-1]:
                if len(Aisle2) > 0:
                    SortedAisle.append(str(Aisle2[x])+"."+SortStyle)
                    del Aisle2[x]
    if 'AisleReverseUpick' in SortStyle:
        while len(Aisle1)+len(Aisle2) > 0:
            for x in range(0,binsPickedPerLane)[::-1]:
                if len(Aisle1) > 0:               
                    SortedAisle.append(str(Aisle1[-1])+"."+SortStyle)
                    del Aisle1[-1]
            for x in range(0,binsPickedPerLane)[::-1]:
                if len(Aisle2) > 0:
                    SortedAisle.append(str(Aisle2[-1])+"."+SortStyle)
                    del Aisle2[-x]

#N-Pick sort
    if 'AisleNPick' in SortStyle:
        binsPickedPerLane = int(SortStyle.split(".")[0][-1])
        while len(Aisle1)+len(Aisle2) > 0:
            for x in range(1,binsPickedPerLane+1):
                if len(Aisle1) > 0:
                    SortedAisle.append(str(Aisle1[0])+"."+SortStyle)
                    del Aisle1[0]
            for x in range(1,binsPickedPerLane+1):
                if len(Aisle2) > 0:
                    SortedAisle.append(str(Aisle2[0])+"."+SortStyle)
                    del Aisle2[0]
    if 'AisleReverseNpick' in SortStyle:
        while len(Aisle1)+len(Aisle2) > 0:
            for x in range(1,int(SortStyle.split(".")[0][-1])+1):
                SortedAisle.append(str(Aisle1[-1])+"."+SortStyle)
                del Aisle1[-1]
            for x in range(1,int(SortStyle.split(".")[0][-1])+1):
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