const nums = [1, 2, 3, 4, 1, 1];

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // const container = {};

  // for (let i = 0; i < nums.length; i++) {
  //   if (container[nums[i]] == null) {
  //     container[nums[i]] = 1;
  //   } else {
  //     container[nums[i]] = container[nums[i]] + 1;
  //   }
  // }
  // for (let v in container) {
  //   console.log(v);
  //   if (container[v] > 1) {
  //     return true;
  //   }
  // }
  // return false;

  const numSet = new Set();
  for (const i in nums) {
    if (numSet.has(nums[i])) {
      return true;
    }
    numSet.add(nums[i]);
  }
  console.log(numSet);
  return false;
};

console.log(containsDuplicate(nums));
