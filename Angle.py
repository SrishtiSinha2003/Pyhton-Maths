import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the angle between two vectors
def calculate_angle(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    
    # Calculate the angle in radians and then convert it to degrees
    angle_radians = np.arccos(dot_product / (magnitude1 * magnitude2))
    angle_degrees = np.degrees(angle_radians)
    
    return angle_degrees

# Define points for the lines (P1, P2, P3)
P1 = np.array([0, 0])
P2 = np.array([4, 3])  # Line 1 from P1 to P2
P3 = np.array([4, 0])  # Line 2 from P1 to P3

# Create vectors from the points
vector1 = P2 - P1
vector2 = P3 - P1

# Calculate the angle between the two vectors
angle = calculate_angle(vector1, vector2)

# Plotting the lines
plt.plot([P1[0], P2[0]], [P1[1], P2[1]], label='Line 1')
plt.plot([P1[0], P3[0]], [P1[1], P3[1]], label='Line 2')

# Mark the points
plt.scatter([P1[0], P2[0], P3[0]], [P1[1], P2[1], P3[1]], color='red')
plt.text(P1[0], P1[1], 'P1', fontsize=12)
plt.text(P2[0], P2[1], 'P2', fontsize=12)
plt.text(P3[0], P3[1], 'P3', fontsize=12)

# Display the angle in the plot
plt.title(f'Angle between the lines: {angle:.2f} degrees')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

print(f"The angle between the two lines is {angle:.2f} degrees")
