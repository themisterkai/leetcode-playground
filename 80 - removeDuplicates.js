const nums = [0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3];

var removeDuplicates = function (nums) {
  let currentNum;
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    if (currentNum !== nums[i]) {
      currentNum = nums[i];
      count = 1;
    } else {
      count++;
    }
    if (count > 2) {
      nums.splice(i, 1);
      i--;
    }
  }
};

removeDuplicates(nums);
console.log(nums);
