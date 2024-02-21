from collections import deque

class TaskScheduler:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)
        print(f"Task '{task}' added to the scheduler.")

    def execute_tasks(self):
        while self.queue:
            task = self.queue.popleft()
            print(f"Executing task: {task}")

# Example usage:
if __name__ == "__main__":
    scheduler = TaskScheduler()
    
    scheduler.add_task("Task 1")
    scheduler.add_task("Task 2")
    scheduler.add_task("Task 3")

    scheduler.execute_tasks()
