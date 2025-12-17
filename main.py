# 括号生成 回溯
def generate_parentheses(n: int) -> list[str]:
    result = []

    def backtrack(current: str, left: int, right: int):
        # 终止条件：已用完 n 对括号
        if len(current) == 2 * n:
            result.append(current)
            return

        # 添加左括号（如果还有剩余）
        if left < n:
            backtrack(current + '(', left + 1, right)

        # 添加右括号（只有当右括号数量 < 左括号时才合法）
        if right < left:
            backtrack(current + ')', left, right + 1)

    backtrack('', 0, 0)
    return result


import math
# 组合数学公式 卡特兰数 返回的是数字 有多少种可能
def count_parentheses_combinations(n: int) -> int:
    if n < 0:
        return 0
    # C_n = (2n)! / ((n+1)! * n!)
    return math.comb(2 * n, n) // (n + 1)


# 动态规划写法 返回的是数字 有多少种可能
def count_parentheses_combinations_d(n: int) -> int:
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]


# 计算阶乘 n！
def factorial(n):
    if n < 0:
        raise ValueError("小于0的数没有阶乘")
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


# 回溯的思路











