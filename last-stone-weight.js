const {
    MaxPriorityQueue
} = require('@datastructures-js/priority-queue');

/**
 * @param {number[]} stones
 * @return {number}
 */
 var lastStoneWeight = function(stones) {
    // create the max heap
    const maxHeap = new MaxPriorityQueue();

    // construct heap time complexity (n log n)
    stones.forEach(stone => {
        maxHeap.enqueue(stone, stone);
    });

    // while maxHeap.size() > 1
    while (maxHeap?.size() > 1) {
        // get the top element, then remove the top element
        // time complexity (log n)
        const x = maxHeap.front()?.element;
        maxHeap.dequeue();
        // get the top element again and then remove it again
        // time complexity (log n)
        const y = maxHeap.front()?.element;
        maxHeap.dequeue();
        const res = x - y;
        if (res > 0) {
            maxHeap.enqueue(res, res);
        }
    }
    // overall time complexity is (n log n) + ((log n) * 2)?
    return maxHeap.front()?.element ? maxHeap.front().element : 0;
};

console.log(lastStoneWeight([2,2]));
