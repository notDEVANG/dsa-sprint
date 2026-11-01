from collections import Counter, deque
import heapq

class Soltuion:
    def leastInterval(self, tasks: list[str], n: int) -> int:
            count = Counter(tasks)

            