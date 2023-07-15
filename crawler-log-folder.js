// 1598. Crawler Log Folder

const operationsMap = {
  "../": -1,
  "./": 0
};
/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
  let numOperations = 0;
  logs.forEach(command => {
    numOperations += operationsMap?.[command] != null ? operationsMap?.[command] : 1;
    if (numOperations < 0) {
      numOperations = 0;
    }
  });
  return numOperations;
};

minOperations(["d1/","d2/","../","d21/","./"]);

console.log(operationsMap["./"]);
