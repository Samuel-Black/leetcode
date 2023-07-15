const {
    MinPriorityQueue
} = require('@datastructures-js/priority-queue');

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var topKFrequent = function(nums, k) {
    
    const frequencyMap = {};

    for (let i = 0; i < nums.length; i++) {
        const num = frequencyMap?.[nums[i]] ? frequencyMap[nums[i]] : 0;
        frequencyMap[nums[i]] = num + 1;
    }

    const minHeap = new MinPriorityQueue();

    Object.keys(frequencyMap).forEach((key, index) => {
        const currentMinKey = minHeap.front()?.element;
        const currentMin = frequencyMap[currentMinKey];
        const currentVal = frequencyMap?.[key];
        if (index < k) {
            minHeap.enqueue(key, currentVal);
        } else if (currentVal > currentMin) {
            minHeap.dequeue();
            minHeap.enqueue(key, currentVal);
        }
    });

    return minHeap.toArray().map(val => {
        return Number(val?.element);
    });
};

console.log(topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0], 6));
