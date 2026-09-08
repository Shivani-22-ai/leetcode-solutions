class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(idx, path):
            if idx == len(s):
                ans.append(path[:])
                return

            for i in range(idx, len(s)):
                sub = s[idx:i + 1]

                if sub == sub[::-1]:
                    path.append(sub)

                    backtrack(i + 1, path)

                    path.pop()

        backtrack(0, [])
        return ans