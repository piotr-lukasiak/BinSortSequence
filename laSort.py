def AisleSorting(SortStyle, Aisle1, Aisle2):
    SortedAisle = []
    if 'AisleZig' in SortStyle: 
        while Aisle1.__len__() > 0:
            SortedAisle.append(str(Aisle1[0])+"."+SortStyle)
            SortedAisle.append(str(Aisle2[0])+"."+SortStyle)
            del Aisle1[0]
            del Aisle2[0]
            continue

    if 'AisleReverseZig' in SortStyle: 
        while Aisle1.__len__() > 0:
            SortedAisle.append(str(Aisle2[-1])+"."+SortStyle)
            SortedAisle.append(str(Aisle1[-1])+"."+SortStyle)
            del Aisle1[-1]
            del Aisle2[-1]
            continue
    return [str(x).split(".") for x in SortedAisle]


def LaneSorting(SortStyle, Lane):
    SortedLane = []
    
    if 'Lane' in SortStyle:
        SortedLane = [str(x)+"."+SortStyle for x in Lane]

    if 'LaneReverse' in SortStyle:
        SortedLane = [str(x)+"."+SortStyle for x in Lane[::-1]]
        
    return [str(x).split(".") for x in SortedLane]