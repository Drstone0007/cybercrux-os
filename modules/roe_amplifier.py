# modules/roe_amplifier.py
import random

class ROEAmplifier:
    def __init__(self):
        self.compliance = "GREEN"
        self.max_aggression = 85

    def status(self):
        return f"ROE Amplifier: {self.compliance} | Max Aggression Level: {self.max_aggression}%"

    def check(self, action):
        if random.random() > 0.88:
            self.compliance = "YELLOW"
            return f"ROE Warning: {action} may violate proportionality rules."
        return "ROE Check Passed."
