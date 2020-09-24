def minMeetingRooms(intervals):
    if len(intervals)<=1:
            return 1
    intervals.sort()
    roomTime=[]
    print(intervals)
    roomTime.append(intervals[0])
    i=1
    rooms=1
    while i<len(intervals):
        startTime=intervals[i][0]
        endTime=intervals[i][1]
        if intervals[i-1][1]>startTime:
            rooms+=1
        i+=1
    return rooms

print(minMeetingRooms([[2,10],[0,1],[15,20]]))
