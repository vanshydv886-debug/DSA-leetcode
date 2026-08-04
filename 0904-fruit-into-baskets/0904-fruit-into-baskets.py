class Solution(object):
    def totalFruit(self, fruits):
        max_length = 0
        my_dict = {}
        left = 0
        right = 0
        n = len(fruits)

        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1

            while len(my_dict) > 2:
                my_dict[fruits[left]] -= 1

                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]

                left += 1

            if len(my_dict) <= 2:
                max_length = max(max_length, right - left + 1)

            right += 1

        return max_length