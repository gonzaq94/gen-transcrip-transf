import math
from collections import Counter

def calculate_entropy(string):
    # Count the frequency of characters in the string
    counter = Counter(string)
    length = len(string)
    
    # Ensure the string is not empty to avoid division by zero
    if length == 0:
        return 0
    
    # Calculate entropy and handle very low probabilities (avoiding log(0))
    epsilon = 1e-10  # A small value to prevent log(0)
    entropy = 0
    for count in counter.values():
        probability = count / length
        # Avoid log(0) by adding epsilon
        if probability > 0:
            entropy -= probability * math.log(probability + epsilon, 2)
    
    return entropy


random_string ="""

So, today we're talking about climate change. It's a big deal. Temperatures are rising, polar bears are losing their homes, and we're seeing more extreme weather events. It's caused by human activities like burning fossil fuels and deforestation. The greenhouse effect is a key part of this. Gases like CO2 trap heat in the atmosphere, making the planet warmer.

We need to do something about it. Renewable energy sources like solar and wind are a great start. Governments need to step up with policies that encourage these changes. It's not just about saving the planet; it's about saving ourselves. Climate change affects everything from agriculture to health.

There are challenges, of course. Transitioning to renewable energy isn't easy or cheap. But it's worth it. We need to invest in new technologies and education. Public awareness is crucial. People need to understand the importance of taking action.
"""
random_string = "xzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwertyxzsdqfwerty"
random_string = "cccccccccccccccccccccccccccccccccccccccccccccccc"

print(calculate_entropy(random_string))  # Higher value indicates more randomness