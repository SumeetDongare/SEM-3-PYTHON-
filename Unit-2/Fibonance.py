#Without Dynamic Programming
class Solution_Without_DP:
    def fib(self,n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
fib1 = Solution_Without_DP()
m = int(input("Enter number:"))
print(f"Fibonacci Number is:{fib1.fib(m)}")

#With Dynamic Progrmming using Memoization Method(Top to Bottom)
#Memoization in Dynamic Programming means storing the results of already-solved subproblems so you don’t calculate them again.

class Solution_Using_Memoization:
    def fib(self,nm):
        memo = {0:0,1:1}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1)+f(x-2)
                return memo[x]

        return f(nm)
fib2 = Solution_Using_Memoization()
m = int(input("Enter number:"))
print(f"Fibonacci Number Using memoizatio Method is:{fib2.fib(m)}")

#With Dynamic Progrmming using Tabulation Method(Bottom to Top)
#Tabulation in Dynamic Programming means solving all the subproblems and storing their results in a table (usually an array) so that you can build up the solution to the original problem.
class Solution_Using_Tabulation:
    def fib(self,n):
        if n <= 0:
            return 0
        if n ==1:
            return 1
        dp = [0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]
fib3 = Solution_Using_Tabulation()
m = int(input("Enter number:"))
print(f"Fibonacci Number Using memoizatio Method is:{fib3.fib(m)}")



