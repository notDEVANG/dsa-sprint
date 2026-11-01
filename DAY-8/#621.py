from collections import Counter, deque
import heapq

class Soltuion:
    def leastInterval(self, tasks: list[str], n: int) -> int:
            count = Counter(tasks)

            heap = [-freq for freq in count.values()]
            heapq.heapify(heap)

            queue = deque()
            time = 0

            while queue or heap:
                time += 1

                if queue or queue[0][1] <= time:
                    freq, availabe_time = queue.popleft()
                    heapq.heappush(heap, freq)

                if heap:
                    freq = heapq.heappop(heap)
                    freq += 1

                    if freq < 0:
                        queue