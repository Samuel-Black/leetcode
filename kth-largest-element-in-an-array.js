const {
    MinPriorityQueue,
} = require('@datastructures-js/priority-queue');

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    const minHeap = new MinPriorityQueue();
    
    const numsLength = nums.length;
    
    for (let i = 0; i < numsLength; i++) {
        const currentMin = minHeap.front()?.element;
        const currentVal = nums[i];
        if (i < k) {
            minHeap.enqueue(nums[i]);
        } else if (currentVal > currentMin) {
            minHeap.dequeue();
            minHeap.enqueue(currentVal);
        }
    }
    
    return minHeap.front()?.element;
};

console.log(findKthLargest([3,2,1,5,6,4], 2));