#!/usr/bin/env python3
import asyncio
from task_wait_random import task_wait_random  # Import task_wait_random

async def run_multiple_tasks(n: int, max_delay: int) -> list:
    
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Create a list of tasks
    results = await asyncio.gather(*tasks)  # Await all tasks to complete
    return results  # Return the list of results

# Test the run_multiple_tasks function
async def main():
    n = 5  # Number of tasks
    max_delay = 10  # Maximum delay for each task
    results = await run_multiple_tasks(n, max_delay)  # Run the tasks
    print(f"Results from {n} tasks: {results}")

# Running the test
if __name__ == "__main__":
    asyncio.run(main())
