const {
    MinPriorityQueue
} = require('@datastructures-js/priority-queue');

/**
 * @param {number} k
 * @param {number[]} nums
 */
 var KthLargest = function(k, nums) {
    this.k = k;
    this.minHeap = new MinPriorityQueue();
    const numsLength = nums.length;
    for (let i = 0; i < numsLength; i++) {
        const currentVal = nums[i];
        if (i < k) {
            this.minHeap.enqueue(currentVal, currentVal);
        } else {
            this.add(currentVal);
        }
    }

};

KthLargest.prototype.k;
KthLargest.prototype.minHeap;

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    
    const currentMin = this.minHeap.front()?.element;
    if (this.minHeap.size() < this.k) {
        this.minHeap.enqueue(val, val);
    } else if (val > currentMin) {
        this.minHeap.dequeue();
        this.minHeap.enqueue(val, val);
    }
    return this.minHeap.front()?.element;
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */

 const kthLargest = new KthLargest(1, []);
 console.log(kthLargest.add(-3));   // return 4
 console.log(kthLargest.add(-2));   // return 5
 console.log(kthLargest.add(-4));  // return 5
 console.log(kthLargest.add(0));   // return 8
 console.log(kthLargest.add(4));   // return 8
