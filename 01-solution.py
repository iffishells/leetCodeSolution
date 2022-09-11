class Solution:
    def minimumSum(self, num: int) -> int:
        print(f'Given Number : {num}')
        # converting into the list of integer
        num_list = sorted([int(i) for i in list(str(num))])
        # set 1 be possible solution
        # pair1 =
        pair_1 = [(str(num_list[0]) + str(num_list[1])), (str(num_list[2]) + str(num_list[3]))]
        pair_2 = [(str(num_list[0]) + str(num_list[2])), (str(num_list[1]) + str(num_list[3]))]

        return min( sum([int(num) for num in pair_1]), sum([int(num) for num in pair_2]) )



if __name__ == '__main__':
    Number = 2932
    solution_object = Solution()
    print(solution_object.minimumSum(Number))
