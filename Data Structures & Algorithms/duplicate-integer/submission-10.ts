class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let numSet: number[] = [...(new Set(nums))]
        return numSet.length !== nums.length
    }
}


