class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        zero_indices = set()

        for i, temp in enumerate(temperatures):
            if i==0 or temp<=temperatures[i-1]:
                result[max(i-1, 0)] = 0
                zero_indices.add(max(i-1, 0))
            elif temp>temperatures[i-1]:
                to_be_removed = set()
                for ind in zero_indices:
                    if temperatures[ind]<temperatures[i]:
                        result[ind] = i - ind
                        to_be_removed.add(ind)
                zero_indices.difference_update(to_be_removed)
            zero_indices.add(i)
            # print(temp, temperatures[i-1])
            # print(result)
            # print(zero_indices)
        return result
