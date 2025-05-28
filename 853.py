class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for pos, spd in cars:
            time = (target - pos) / float(spd)
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)

obj = Solution()
print(obj.carFleet(10, [6,8], [3,2]))