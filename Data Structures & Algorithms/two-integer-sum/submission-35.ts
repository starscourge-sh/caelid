class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        for (let i = 0; i < nums.length; i++) {
            console.log(i);
            let cur: number = nums[i];
            let other: number = target - cur;
            console.log('nums: ', nums)
            console.log('target: ', target)
            console.log('cur: ', cur)
            console.log('other: ', other)
            let indexOfOther: number = nums.lastIndexOf(other);
            console.log('other index: ', indexOfOther)

            // not a true pair, is same number
            if (indexOfOther == i) continue;
            // complementary number not in list
            if(indexOfOther == -1) continue

            return [i, indexOfOther];
        }
        return [-1, -1];
    }
}
