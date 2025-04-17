# This script calculates the effect size Cohen's d

#Use this effect size if the sample size in your experiment is large and the two SDs are similar
#If the sample size is small, consider calculating Hedges' g, which is a bias-corrected version of Cohen's d
#If the standard deviations are very different, consider calculating Glass' delta, 
# Glass' delta uses the standard deviation of the control group only

# In a two group experiment...
# you will need to know the following values

# The sample sizes of each group (n1 & n2),
# the two group means (M1 & M2) and
# the corresponding standard deviations (SD1 & SD2)

# Use this effect size if theh two SDs are not very different
# If the two SDs are very different, consider calculating Glass' delta
# This calculation is based on Cohen's d formula in
# Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Hillsdale, NJ: Erlbaum.

# A short statement interepreting the calculated value is printed at the end of the output.

# If you use this code, please cite the references below.

import math

def calculate_cohens_d(M1, M2, SD1, SD2, n1, n2):
    # Calculate the mean difference
    mean_difference = M1 - M2

    # Calculate the pooled standard deviation
    SD_pooled = math.sqrt(((n1 - 1) * SD1**2 + (n2 - 1) * SD2**2) / (n1 + n2 - 2))

    # Calculate Cohen's d
    Cohens_d = mean_difference / SD_pooled

    return Cohens_d

def interpret_Cohens_d(d):
    if d < 0.2:
        return "The calculated effect size indicates a very small effect"
    elif 0.2 <= d < 0.5:
        return "The calculated effect size indicates a small effect"
    elif 0.5 <= d < 0.8:
        return "The calculated effect size indicates a medium effect"
    else:
        return "The calculated effect size indicates a large effect"

# Get user input for the values
M1 = float(input("Enter the mean of the experimental group or Group 1 (M1): "))
M2 = float(input("Enter the mean of the control group or Group 2 (M2): "))
SD1 = float(input("Enter the standard deviation of experimental group or Group 1 (SD1): "))
SD2 = float(input("Enter the standard deviation of control group or Group 2 (SD2): "))
n1 = int(input("Enter the sample size of experimental group or Group 1 (n1): "))
n2 = int(input("Enter the sample size of control group or Group 2 (n2): "))

# Calculate Cohen's d
Cohens_d = calculate_cohens_d(M1, M2, SD1, SD2, n1, n2)

print(f"Cohen's d is {Cohens_d:.2f}")
print()
# Interpret Cohen's d
print(interpret_Cohens_d(Cohens_d))

# References
print("References:")
print("Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Hillsdale, NJ: Erlbaum.")
print("Rami, M. K. (2025). Cohens_d [Computer software]. Github. https:/github.com/manishrami/Cohens_d")



