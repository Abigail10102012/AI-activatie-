import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Step 1: Define the average rate (λ)
lambda_rate = 4  # average number of events per interval

# Step 2: Create a range of values
x = np.arange(0, 15)

# Step 3: Calculate Poisson probabilities
poisson_probs = poisson.pmf(x, mu=lambda_rate)

# Step 4: Plot the distribution
plt.bar(x, poisson_probs, color='skyblue')
plt.title(f'Poisson Distribution (λ = {lambda_rate})')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.grid(True)
plt.show()
