class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(idx, path, total):
            if total == target:
                ans.append(path[:])
                return
            if total > target:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return ans
        