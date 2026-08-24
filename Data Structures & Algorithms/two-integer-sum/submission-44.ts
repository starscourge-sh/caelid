class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        for (let i = 0; i < nums.length; i++) {
            let cur: number = nums[i];
            let indexOfComplement: number = nums.lastIndexOf(target - cur);
            console.log("nums: ", nums)
            console.log("comp: ", target - cur)
            console.log("indexOfComplement: ", indexOfComplement)

            // not a true pair, is same number or
            // complementary number not in list
            if (indexOfComplement == i || indexOfComplement == -1) continue;
            return [i, indexOfComplement];
        }
    }
}
