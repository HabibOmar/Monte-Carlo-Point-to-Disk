import random
import math
import time

def estimate_view_factor(theta0, num_samples):
    """
    Estimate the view factor between a point and a circular disk using
    Monte Carlo simulation.

    Parameters:
        theta0 (float): Threshold angle (in radians).
        num_samples (int): Number of random samples to generate.

    Returns:
        tuple: Estimated view factor and elapsed time (in seconds).
    """
    start_time = time.time()
    count = 0

    for _ in range(num_samples):
        theta = math.asin(math.sqrt(random.uniform(0, 1)))
        if theta < theta0:
            count += 1

    elapsed_time = time.time() - start_time
    view_factor = count / num_samples
    return view_factor, elapsed_time

def calculate_relative_error(estimated, analytic):
    """
    Calculate the relative error between the estimated and analytical values.

    Parameters:
        estimated (float): Estimated value.
        analytic (float): Analytical value.

    Returns:
        float: Relative error in percentage.
    """
    return abs((estimated - analytic) / analytic) * 100

def main():
    """
    Main function to run the Monte Carlo simulation and print the results.
    This function calculates the view factor between a point and a circular disk
    """
    disk_radius = 1  # radius of the disk
    height = 7  # perpendicular distance between the point and the disk center
    theta0 = math.atan(disk_radius / height)  # threshold angle in radians
    VF_analytic = 1 / (1 + height**2)
    sampling_sizes = [10**2, 10**4, 10**6, 10**8]

    print("Sampling Size\tEstimated View Factor\tRelative Error (%)\tElapsed Time (s)")

    for size in sampling_sizes:
        estimated_view_factor, elapsed_time = estimate_view_factor(theta0, size)
        relative_error = calculate_relative_error(estimated_view_factor, VF_analytic)
        print(f"{size:<14}\t{estimated_view_factor:.6f}\t\t{relative_error:.6f}\t\t{elapsed_time:.6f}")

# Run the main function
if __name__ == "__main__":
    main()
