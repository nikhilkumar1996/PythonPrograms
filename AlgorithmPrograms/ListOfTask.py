"""
Program 11 : Input Format - The first line contains the number of tasks.Each of the next
lines contains two integers,D and M .
Output Format - Output T lines. The ith line contains the value of the maximum
amount by which a task's completion time overshoots its deadline, when the first
tasks on your list are scheduled optimally.
"""


def complete_task(dead_line, time_completion, tasks):
    """
    Returns the difference between completion time and deadline in descending order.
    :param dead_line: Deadline integer values given in list provided by the user.
    :param time_completion: Completion Time integer values given in list provided by the user.
    :param tasks: Number of tasks for which deadline and completion time is provided by the user.
    :return: difference between completion time and deadline in descending order.
    """
    time_diff = []
    for task_count in range(tasks):
        time_diff.append(int(time_completion[task]) - int(dead_line[task]))
    time_diff.sort(reverse=True)  # List in Descending Order
    return time_diff


if __name__ == "__main__":
    no_of_tasks = int(input("Enter the number of tasks to complete: "))
    deadline = []
    completion_time = []
    for task in range(no_of_tasks):
        input_line = input("Enter deadline and completion time for the task {}: ".format(task+1))
        deadline.append(input_line.split(" ")[0])
        completion_time.append(input_line.split(" ")[1])
    time_difference = complete_task(deadline, completion_time, no_of_tasks)
    for diff in time_difference:
        print(diff)