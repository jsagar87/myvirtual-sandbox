table = dict()


class Solution:

    def fib(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n > 1:
            if not table.get(n):
                compute = self.fib(n - 1) + self.fib(n - 2)
                table[n] = compute
            return table.get(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(0))
    print(sol.fib(1))
    print(sol.fib(2))
    print(sol.fib(3))
