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

    stones.forEach(stone => {
        maxHeap.enqueue(stone, stone);
    });

    // while maxHeap.size() > 1
    while (maxHeap?.size() > 1) {
        // get the top element, then remove the top element
        const x = maxHeap.front()?.element;
        maxHeap.dequeue();
        // get the top element again and then remove it again
        const y = maxHeap.front()?.element;
        maxHeap.dequeue();
        const res = x - y;
        if (res > 0) {
            maxHeap.enqueue(res, res);
        }
    }
    return maxHeap.front()?.element ? maxHeap.front().element : 0;
};

console.log(lastStoneWeight([2,2]));
