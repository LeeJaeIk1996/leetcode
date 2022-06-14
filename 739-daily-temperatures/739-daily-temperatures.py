class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []

        for tindex, tvalue in enumerate(temperatures):
            while stack and tvalue > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = tindex - last
            stack.append(tindex)

        return answer