"""Reference: https://github.com/qiwsir/algorithm/blob/050178ada82ef8d5c7ace2eda7ed408aa61e7b90/longest_increasing_sequence.py#L7"""
from StatRepair import StatRepair
def isBiggerCompare(a, b):
	return a > b

def findLIS(sequence, compare = isBiggerCompare):
	n = len(sequence)
	dp = [0 for i in range(n)]
	track = [-1 for i in range(n)]
	ans = 1
	for i in range(1, n):
		MAX = 0
		for j in range(i):
			if compare(sequence[i], sequence[j]) and MAX < dp[j]:
				MAX = dp[j]
				track[i] = j
		dp[i] = MAX + 1
		if dp[i] > dp[ans]:
			ans = i
	ansList = [sequence[ans]]
	while track[ans] != -1:
		ans = track[ans]
		ansList.insert(0, sequence[ans])
	return ansList

def test_findLIS():
    lisDebugger = StatRepair()

    with lisDebugger.collect_pass():
        s = [3, 1]
        findLIS(s)

    with lisDebugger.collect_pass():
        s = [3, 1, 2]
        findLIS(s)

    with lisDebugger.collect_pass():
        s = [3, 1, 2, 6]
        findLIS(s)

    with lisDebugger.collect_pass():
        s = [3, 1, 2, 6, 0]
        findLIS(s)

    with lisDebugger.collect_pass():
        s = [3, 1, 2, 6, 0, 5]
        findLIS(s)

    with lisDebugger.collect_fail():
        try:
            print(findLIS(-1))
        except:
            pass

    with lisDebugger.collect_fail():
        try:
            findLIS([0])
        except:
            pass

    with lisDebugger.collect_fail():
        try:
            findLIS([])
        except:
            pass

    line, dist = lisDebugger.mostsimilarstmt(lisDebugger.rank()[0])
    assert (line == "def isBiggerCompare(a, b):" and dist == 33) or (line == "ans = track[ans]" and dist == 14)
