class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse = True)
        #print(tasks)
        time = []

        for i in range(len(processorTime)):
            time.append(processorTime[i] + max(tasks[i*4: i*4+4]))
            #print(i, time)
        
        return max(time)

        