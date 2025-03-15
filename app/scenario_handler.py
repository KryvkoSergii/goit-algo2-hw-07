from enum import Enum
import random

max_number = 100_000

def generate_random_array(n):
    return [random.randint(1, max_number) for _ in range(n)]

class Action(Enum):
    RANGE = 1
    UPDATE = 2

class ScenarioHandler:
    def __init__(self):
        self.scenaries = []

    def generate_random_scenarios(self, length_of_arry, number_of_scenarios):
        for _ in range(number_of_scenarios):
            action = random.choice(list(Action))
            if action == Action.UPDATE:
                L = random.randint(0, length_of_arry - 1)
                R = random.randint(L, length_of_arry - 1)
                self.scenaries.append((action, L, R))
            else:
                index = random.randint(0, length_of_arry - 1)
                value = random.randint(1, max_number)
                self.scenaries.append((action, index, value))
        print(f"length of scenarios: {len(self.scenaries)} generated")

    def get_statistics(self):
        range_count = sum(1 for action, *_ in self.scenaries if action == Action.RANGE)
        update_count = sum(1 for action, *_ in self.scenaries if action == Action.UPDATE)
        return range_count, update_count

    def run_scenarios(self, array, range_sum, update, adhoc=False): 
        increment = max(1, len(array) // 10)       
        for idx, (action, *args) in enumerate(self.scenaries):
            if idx % increment == 0:
                print(f"progress: {idx} / {len(self.scenaries)}")
            if action == Action.UPDATE:
                update(array, *args)
            elif action == Action.RANGE:
                if adhoc:
                    range_sum(*args)
                else:
                    range_sum(array, *args)
            else:
                raise ValueError(f"Unknown action: {action}")