import numpy as np
import matplotlib.pyplot as plt

# Parameters
sample_size = 30       # Number of values in each sample
num_samples = 1000     # Number of samples to generate

# Generate sample means
sample_means = []
for _ in range(num_samples):
    sample = np.random.uniform(0, 1, sample_size)
    sample_means.append(np.mean(sample))

# Plot histogram of sample means
plt.hist(sample_means, bins=30, density=True, color='skyblue', edgecolor='black')
plt.title('Central Limit Theorem Demonstration')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
