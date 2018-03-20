class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        for i in S:
            print(i)
            if i in J:
                counter = counter + 1

        print(counter)
        return counter


def main():

    J = input("Enter the jewels: ")
    S = input("Enter the stones: ")
    Solution().numJewelsInStones(J, S)


if __name__ == '__main__':
    main()