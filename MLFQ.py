from collections import deque

class Task:
    def __init__(self, vehicle_id, token_count):
        self.vehicle_id = vehicle_id
        self.token_count = token_count

class MultiLevelFeedbackQueue:
    def __init__(self):
        self.queue_with_tokens = deque()    # Queue 1: Tasks with tokens
        self.queue_without_tokens = deque()  # Queue 2: Tasks without tokens

    def add_task(self, task):
        if task.token_count > 0:
            self.queue_with_tokens.append(task)
        else:
            self.queue_without_tokens.append(task)

    def process_tasks(self):
        while self.queue_with_tokens or self.queue_without_tokens:
            if self.queue_with_tokens:
                self.process_task(self.queue_with_tokens.popleft())

            if self.queue_without_tokens:
                self.process_task(self.queue_without_tokens.popleft())

    def process_task(self, task):
        print(f"Processing Task for Vehicle {task.vehicle_id} with {task.token_count} tokens.")
        # Add additional processing logic as needed

# Example: Using the MultiLevelFeedbackQueue
mlfq = MultiLevelFeedbackQueue()

# Adding tasks to the MLFQ
task1 = Task(1, 2)  # Vehicle 1 with 2 tokens
task2 = Task(2, 0)  # Vehicle 2 with 0 tokens
task3 = Task(3, 1)  # Vehicle 3 with 1 token

mlfq.add_task(task1)
mlfq.add_task(task2)
mlfq.add_task(task3)

# Processing tasks in the MLFQ
mlfq.process_tasks()
