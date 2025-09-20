#Question Link: https://leetcode.com/problems/implement-router/description/?envType=daily-question&envId=2025-09-20
"""
3508. Implement Router

Problem Statement: Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:
- source: A unique identifier for the machine that generated the packet.
- destination: A unique identifier for the target machine.
- timestamp: The time at which the packet arrived at the router.

Implement the Router class:
Router(int memoryLimit): Initializes the Router object with a fixed memory limit.
- memoryLimit is the maximum number of packets the router can store at any given time.
- If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.

bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.
- A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
- Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.

int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.
- Remove the packet from storage.
- Return the packet as an array [source, destination, timestamp].
- If there are no packets to forward, return an empty array.

int getCount(int destination, int startTime, int endTime):
- Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].

Note that queries for addPacket will be made in increasing order of timestamp.

Example 1:
Input:
["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
Output:
[null, true, true, false, true, true, [2, 5, 90], true, 1]

Explanation:
Router router = new Router(3); // Initialize Router with memoryLimit of 3.
router.addPacket(1, 4, 90); // Packet is added. Return True.
router.addPacket(2, 5, 90); // Packet is added. Return True.
router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.
router.addPacket(3, 5, 95); // Packet is added. Return True
router.addPacket(4, 5, 105); // Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
router.forwardPacket(); // Return [2, 5, 90] and remove it from router.
router.addPacket(5, 2, 110); // Packet is added. Return True.
router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.

Example 2:
Input:
["Router", "addPacket", "forwardPacket", "forwardPacket"]
[[2], [7, 4, 90], [], []]
Output:
[null, true, [7, 4, 90], []]

Explanation:
Router router = new Router(2); // Initialize Router with memoryLimit of 2.
router.addPacket(7, 4, 90); // Return True.
router.forwardPacket(); // Return [7, 4, 90].
router.forwardPacket(); // There are no packets left, return [].
 
Constraints:
* 2 <= memoryLimit <= 10^5
* 1 <= source, destination <= 2 * 10^5
* 1 <= timestamp <= 10^9
* 1 <= startTime <= endTime <= 10^9
* At most 10^5 calls will be made to addPacket, forwardPacket, and getCount methods altogether.
* queries for addPacket will be made in increasing order of timestamp.
"""

from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # FIFO order
        self.seen = set()  # for duplicates
        self.dest_map = defaultdict(list)  # destination -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        # Duplicate check
        if packet in self.seen:
            return False

        # Remove oldest if full
        if len(self.queue) == self.memoryLimit:
            old_source, old_dest, old_time = self.queue.popleft()
            self.seen.remove((old_source, old_dest, old_time))
            # remove from dest_map (list is sorted, so use bisect to delete quickly)
            idx = bisect_left(self.dest_map[old_dest], old_time)
            if idx < len(self.dest_map[old_dest]) and self.dest_map[old_dest][idx] == old_time:
                self.dest_map[old_dest].pop(idx)

        # Add new packet
        self.queue.append(packet)
        self.seen.add(packet)
        self.dest_map[destination].append(timestamp)  # always increasing order

        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []

        source, destination, timestamp = self.queue.popleft()
        self.seen.remove((source, destination, timestamp))

        # remove from dest_map using bisect
        idx = bisect_left(self.dest_map[destination], timestamp)
        if idx < len(self.dest_map[destination]) and self.dest_map[destination][idx] == timestamp:
            self.dest_map[destination].pop(idx)

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0

        timestamps = self.dest_map[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)

        return right - left
