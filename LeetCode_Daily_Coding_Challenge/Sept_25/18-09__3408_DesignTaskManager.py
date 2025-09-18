#Question Link: https://leetcode.com/problems/design-task-manager/description/?envType=daily-question&envId=2025-09-18
"""
3408. Design Task Manager

Problem Statement: There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:
- TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.
- void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.
- void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.
- void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.
- int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

Note that a user may be assigned multiple tasks.

Example 1:
Input:
["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
Output:
[null, null, null, 3, null, null, 5]
Explanation:
TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
taskManager.edit(102, 8); // Updates priority of task 102 to 8.
taskManager.execTop(); // return 3. Executes task 103 for User 3.
taskManager.rmv(101); // Removes task 101 from the system.
taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
taskManager.execTop(); // return 5. Executes task 105 for User 5.
 
Constraints:
* 1 <= tasks.length <= 10^5
* 0 <= userId <= 10^5
* 0 <= taskId <= 10^5
* 0 <= priority <= 10^9
* 0 <= newPriority <= 10^9
* At most 2 * 10^5 calls will be made in total to add, edit, rmv, and execTop methods.
* The input is generated such that taskId will be valid.
"""

import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_to_user = {}
        self.task_to_priority = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            self.task_to_user[taskId] = userId
            self.task_to_priority[taskId] = priority
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_user[taskId] = userId
        self.task_to_priority[taskId] = priority
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_to_priority[taskId] = newPriority
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        # Mark as removed by deleting from dictionaries
        if taskId in self.task_to_user:
            del self.task_to_user[taskId]
        if taskId in self.task_to_priority:
            del self.task_to_priority[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, taskId = heapq.heappop(self.heap)

            # Check if task is still valid
            if taskId not in self.task_to_priority:
                continue  # deleted earlier

            if -priority != self.task_to_priority[taskId]:
                continue  # outdated entry (old priority)

            # Found the correct top task
            userId = self.task_to_user[taskId]
            # Remove it
            del self.task_to_user[taskId]
            del self.task_to_priority[taskId]
            return userId

        return -1  # no tasks available
