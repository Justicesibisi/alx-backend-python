#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    
    delay = random.uniform(0, max_delay)  # Generate random float between 0 and max_delay
    await asyncio.sleep(delay)  # Asynchronously wait for the delay
    return delay  # Return the delay after waiting