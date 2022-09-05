class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        rt = [-1] * n
        cnt = [0] * n
        meetings.sort()
        i,j = 0,0
        if n == 1:
            return 0
        while (i < len(meetings)):
            # if(i == 0):
            #     for t in range(min(n,len(meetings))):
            #         rt[t] = meetings[i][1]
            #         cnt[t] += 1
            #         i += 1
            #     continue
            # print(rt)
            minVal = min(rt)
            # print("minVal",minVal)
            minIdx = 0
            if(minVal > meetings[i][0]):
                for t in range(len(rt)):
                    if(minVal == rt[t]):
                        minIdx = t
                        break
            else:
                for t in range(len(rt)):
                    if(rt[t] <= meetings[i][0]):
                        minIdx = t
                        break
                
                
            rt[minIdx] = (max(0,(rt[minIdx] - meetings[i][0])) + meetings[i][1])
            cnt[minIdx] += 1
            i += 1
            # # j += 1
            # if(j == n-1):
            #     j = 0
        
        maxVal = max(cnt)
        maxIdx = 0
        for t in range(0,len(cnt)):
            if (maxVal == cnt[t]):
                maxIdx = t 
                break
                
        # print(cnt)
        return maxIdx
            
        
        