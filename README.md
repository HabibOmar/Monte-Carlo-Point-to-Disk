# Monte Carlo View Factor Estimation: Point to Disk

This project estimates the view factor between a point and a circular disk using Monte Carlo simulation. The view factor is a measure of the fraction of radiation leaving one surface that strikes another surface.

## Description

The script estimates the view factor by generating random direction cosines and calculating whether they intersect within the disk's radius. It compares the estimated view factor with an analytical value and calculates the relative error.

## Prerequisites

- Python 3.x
- NumPy

## Usage

### Clone the repository:

```bash
git clone https://github.com/HabibOmar/Monte-Carlo-Point-to-Disk.git
cd monte-carlo-view-factor
```
### Install the required dependencies:
```bash
pip install numpy
```
### Run the script:
```bash
python montecarlo_view_factor.py
```

## Parameters
* Radius (disk_radius): Represents the radius of the circular disk. Units: millimeters (mm).
* Height (height): Represents the height of the point above the disk. Units: millimeters (mm).
* Sampling Size (num_samples or SamplingSize): Number of random samples generated in the Monte Carlo simulation. Higher sampling sizes generally lead to more accurate estimates but increase computation time.
* Theta0 (theta0): The threshold angle, calculated as atan(R/H).

## Example Output

Sampling Size | Estimated View Factor | Relative Error (%) | Elapsed Time (s)
------------- | ------------- | ------------- | -------------
100 | 0.010000 | 50.000000 | 0.000000
10000 | 0.020800 | 4.000000 | 0.018544
1000000 | 0.019819 | 0.905000 | 1.067744
100000000 | 0.019990 | 0.052100 | 79.544530


### Output Explanation
* Sampling Size: Number of random samples used in the Monte Carlo simulation.
* Estimated View Factor: The view factor estimated from the Monte Carlo simulation.
* Relative Error (%): The relative error between the estimated view factor and the analytical value.
* Elapsed Time (s): The time taken to perform the simulation.