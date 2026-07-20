class Solution(object):
    def generateParenthesis(self, n):

        def solve(ind, total, brackets, result):

            if total > len(brackets) // 2:
                return

            if total < 0:
                return

            if ind >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            brackets[ind] = "("
            new_total = total + 1
            solve(ind + 1, new_total, brackets, result)

            brackets[ind] = ")"
            new_total = total - 1
            solve(ind + 1, new_total, brackets, result)

        result = []
        brackets = [""] * (2 * n)

        solve(0, 0, brackets, result)

        return result