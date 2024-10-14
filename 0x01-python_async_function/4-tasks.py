#!/usr/bin/env python3
import asyncio
import time
from task_wait_n import task_wait_n  # Import task_wait_n

def measure_time(n: int, max_delay: int) -> float:
  
    start_time = time.time()  # Record the start time
    asyncio.run(task_wait_n(n, max_delay))  # Run the task_wait_n function
    total_time = time.time() - start_time  # Calculate the total execution time
    return total_time / n  # Return the average time per task

# Test the measure_time function
if __name__ == "__main__":
    n = 5  # Number of tasks
    max_delay = 10  # Maximum delay for each task
    average_time = measure_time(n, max_delay)  # Measure the time
    print(f"Average time per task: {average_time:.2f} seconds")
