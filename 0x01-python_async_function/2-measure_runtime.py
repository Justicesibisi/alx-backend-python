#!/usr/bin/env python3
import time
import asyncio
from basic_async_syntax import wait_n  # Import wait_n from the previous file

async def measure_time(n: int, max_delay: int) -> float:
   
    start_time = time.time()  # Record the start time
    await wait_n(n, max_delay)  # Run the wait_n function
    end_time = time.time()  # Record the end time
    
    total_time = end_time - start_time  # Calculate the total execution time
    return total_time / n  # Return the average time per call

# Test the measure_time function
async def main():
    avg_time = await measure_time(5, 10)  # Measure the runtime for 5 tasks with max_delay 10
    print(f"Average time per call: {avg_time:.2f} seconds")

# Running the test
if __name__ == "__main__":
    asyncio.run(main())
