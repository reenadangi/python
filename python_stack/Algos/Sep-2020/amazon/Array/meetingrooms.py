def canAttendMeetings(meetings):
    meetings.sort()
    for i in range(1,len(meetings)):
        if meetings[i][0]<meetings[i-1][1]:
            return False
    return True


print(canAttendMeetings([[1,3],[2,7],[8,10],[15,18]]))

   
     