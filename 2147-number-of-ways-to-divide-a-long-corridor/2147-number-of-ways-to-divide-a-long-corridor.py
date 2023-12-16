class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seatCount, plantCount = 0, 0
        plants = []
        result = 1
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                if seatCount < 2:
                    seatCount += 1
                elif seatCount == 2:
                    plants.append(plantCount)
                    result *= plantCount+1
                    seatCount, plantCount = 1, 0
            elif corridor[i] == 'P' and seatCount == 2:
                plantCount += 1
            #print(seatCount, plantCount)
        if seatCount != 2 or seatCount== 0:
            return 0
        else:
            #return the modulo 109 + 7 of multiplication of all elements in plants where after incrementing each element by 1
            # result = 1
            # for i in range(len(plants)):
            #     result *= (plants[i] + 1)
            # return result % (10**9 + 7)
            return result % (10**9 + 7)
        return 0