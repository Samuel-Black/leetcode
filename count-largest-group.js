// 1399. Count Largest Group

/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
  const countMap = {};
  const sumMap = {};
  let highestSumKey = "1";
  for (let i = 1; i <= n; i++) {
    const sum = getSum(i.toString());
    sumMap?.[sum] == null ? sumMap[sum] = 1 : sumMap[sum] = sumMap[sum] + 1;
    countMap?.[sumMap?.[sum]] == null ? countMap[sumMap?.[sum]] = 1 : countMap[sumMap?.[sum]] = countMap?.[sumMap?.[sum]] + 1;
    if (Number(highestSumKey) < sumMap?.[sum]) {
      highestSumKey = String(sumMap[sum]);
    }
  }
  return countMap?.[highestSumKey];
};

var getSum = function(s) {
  let sum = 0;
  for (let i = 0; i < s.length; i ++) {
    sum += Number(s[i]);
  }
  return sum;
};

console.log(countLargestGroup(13));
