### Setup

`python3 -m pip install Flask==2.1.3 aiohttp==3.8.1`

Tested with python version 3.10.4

### Fireworks webserver (time delay example)

```python
from time import sleep
from flask import Flask

app = Flask(__name__)


@app.route("/<fw>/<bang_time>")
def launch(fw, bang_time):
    sleep(float(bang_time))
    return f"""

        .
      .' |
    .'   |
    /`-._'
   /   /
  /   /
 /   /
(`-./
 )

{fw} launched!
"""


if __name__ == "__main__":
    app.run(port=1776)
```

### Threading Example

```python
#!/usr/bin/python3
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests


fireworks = [
    ("Roman Candle", 1),
    ("Report", 2),
    ("Peony", 3),
    ("Palm Tree", 4),
    ("Pistil", 5),
]


def launch_firework(firework_name, launch_time):
    print(f"launching a {firework_name}!")
    return requests.get(f"http://127.0.0.1:1776/{firework_name}/{launch_time}")


start = time.time()

processes = []

# we want to be careful with the number of workers
# if you are making thousands of requests, does your target have limiting engaged?
# beware you don't overload internal or external services; 5 to 10 is fine for most scripts
print("Starting the fireworks show!")
with ThreadPoolExecutor(max_workers=5) as executor:
    for fw in fireworks:
        # add a new task to the threadpool and store in processes list
        processes.append(executor.submit(launch_firework, *fw))  
    for task in as_completed(processes):
        # yields the items in processes as they complete (it finished or was canceled)
        print(task.result().text)

# display the total run time
print(f'Time taken: {time.time() - start}')
```

### Async Example

```python
#!/usr/bin/python3
import asyncio
import time
import aiohttp


fireworks = [
    ("Roman Candle", 1),
    ("Report", 3),
    ("Peony", 4),
    ("Palm Tree", 3),
    ("Pistil", 5),
]


async def launch_firework(session, firework_name, launch_time):
    print(f"launching a {firework_name}!")
    async with session.get(f"http://127.0.0.1:1776/{firework_name}/{launch_time}") as resp:
        print(await resp.text())


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(launch_firework(session, *fwork)) for fwork in fireworks]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f'Time taken: {time.time() - start}')
```
