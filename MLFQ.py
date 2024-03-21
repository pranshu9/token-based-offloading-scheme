#include <iostream>
#include <deque>

using namespace std;

// Task class
class Task {
public:
    int vehicleId;
    int tokenCount;

    // Constructor
    Task(int id, int count) : vehicleId(id), tokenCount(count) {}
};

// MultiLevelFeedbackQueue class
class MultiLevelFeedbackQueue {
private:
    deque<Task> queueWithTokens;      // Queue 1: Tasks with tokens
    deque<Task> queueWithoutTokens;   // Queue 2: Tasks without tokens

public:
    // Method to add a task to the appropriate queue
    void addTask(Task task) {
        if (task.tokenCount > 0) {
            queueWithTokens.push_back(task);
        } else {
            queueWithoutTokens.push_back(task);
        }
    }

    // Method to process tasks from both queues
    void processTasks() {
        while (!queueWithTokens.empty() || !queueWithoutTokens.empty()) {
            if (!queueWithTokens.empty()) {
                processTask(queueWithTokens.front());
                queueWithTokens.pop_front();
            }

            if (!queueWithoutTokens.empty()) {
                processTask(queueWithoutTokens.front());
                queueWithoutTokens.pop_front();
            }
        }
    }

    // Method to process a single task
    void processTask(Task task) {
        cout << "Processing Task for Vehicle " << task.vehicleId << " with " << task.tokenCount << " tokens." << endl;
        // Add additional processing logic as needed
    }
};

int main() {
    // Using the MultiLevelFeedbackQueue
    MultiLevelFeedbackQueue mlfq;

    // Adding tasks to the MLFQ
    Task task1(1, 2);  // Vehicle 1 with 2 tokens
    Task task2(2, 0);  // Vehicle 2 with 0 tokens
    Task task3(3, 1);  // Vehicle 3 with 1 token

    mlfq.addTask(task1);
    mlfq.addTask(task2);
    mlfq.addTask(task3);

    // Processing tasks in the MLFQ
    mlfq.processTasks();

    return 0;
}
