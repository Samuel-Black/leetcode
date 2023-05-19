// 1399. Count Largest Group

/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
  const countArr = [];
  const nLength = n.toString().length;
  for (let i = 1; i < n; i++) {
    let temp = [];
    temp.push(i);
    for (let k = 0; k < nLength; k++) {
    }
  }
};

console.log(countLargestGroup(13));

var countLargestGroup = function(n) {
  const hashmap = new Map();
  let output = {
      value: 0,
      count: 0,
  };
  
  for (let i = 1; i <= n; i++) {
      const sum = getSum(i);
      
      if (!hashmap.has(sum)) {
          hashmap.set(sum, 1)
      } else {
          hashmap.set(sum, hashmap.get(sum) + 1);
      }
  }
  
  hashmap.forEach((value, key) => {
      if (value > output.value) {
          output = {
              value,
              count: 1,
          };
      } else if (value === output.value) {
          output.count++;
      }
  })
  return output.count;
};

const getSum = (number) => {
  number = String(number);
  let output = 0;
  
  for (let i = 0; i < number.length; i++) {
      output += Number(number[i]);
  }
  
  return output;
}