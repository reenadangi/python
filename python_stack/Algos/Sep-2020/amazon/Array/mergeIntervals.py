def merge(intervals):
#         
        if len(intervals)<=1:
            return intervals
        answers=[]
        intervals.sort()
        print(intervals)
        answers.append(intervals[0])
        i=1
        while i<len(intervals):
            p_value=answers[len(answers)-1]
            c_value=intervals[i]
            if(c_value[0]>=p_value[0] and c_value[0]<=p_value[1]):
                lst=[]
                lst.append(p_value[0])
                lst.append(max(c_value[1],p_value[1]))
                answers[len(answers)-1]=lst
            else:
                answers.append(intervals[i])
            i+=1
        return answers

