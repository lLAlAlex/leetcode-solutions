class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Notes so i dont forget
        
        # Greedy
        # Minimum 1 candy
        candies = [1] * len(ratings)
        
        # Left-right pass
        for i in range(1, len(ratings)):
            # if curr rating is higher than prev, update curr candy to higher than prev candy
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # print(candies)
        
        # Right-left pass
        for i in range(len(ratings)-2, -1, -1):
            # if curr rating is higher than next, update curr candy to max(curr candy, next candy)
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

obj = Solution()
print(obj.candy([1,0,2]))