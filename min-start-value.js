// 1413. Minimum Value to Get Positive Step by Step Sum

/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
  let lowestVal = 1;
  let currentVal = 0;
  nums.forEach(val => {
    currentVal += val;
    if (currentVal < lowestVal) {
      lowestVal = currentVal;
    }
  });

  return lowestVal < 1 ? Math.abs(lowestVal) + 1 : 1;
};

console.log(minStartValue([-3,2,-3,4,2]));
