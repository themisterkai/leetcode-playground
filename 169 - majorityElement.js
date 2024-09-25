const nums = [3, 3, 4];

var majorityElement = function (nums) {
  let count = 0;
  let element;

  const holder = {};

  for (let i = 0; i < nums.length; i++) {
    if (holder[nums[i]] === undefined) {
      holder[nums[i]] = 1;
    } else {
      holder[nums[i]] = holder[nums[i]] + 1;
    }
    if (holder[nums[i]] > count) {
      console.log(holder[nums[i]]);
      count = holder[nums[i]];
      element = nums[i];
    }
    console.log(count, element, nums[i]);
  }
  return element;
};

console.log(majorityElement(nums));
