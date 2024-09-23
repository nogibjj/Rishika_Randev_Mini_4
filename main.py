"""Main script for creating descriptive statistics
and a data visualization using seaborn & matplotlib."""

import seaborn as sns
import matplotlib.pyplot as plt


def load_data():
    """Loads a seaborn dataset with basic data on life expectancies
    of different countries vs. how much money they spent on healthcare
    per person in USD across several different years."""
    return sns.load_dataset("healthexp")


def generate_summary_stats():
    """Returns summary statistics from the healthcare dataset."""
    healthexp = load_data()
    return healthexp.describe(), healthexp.median(numeric_only=True)


def generate_histogram():
    """Generate histogram of healthcare spending in the US
    between 1970 and 2020."""
    data_frame = load_data()
    us_data = data_frame[data_frame["Country"] == "USA"]
    plt.plot(us_data["Year"], us_data["Spending_USD"], color="Blue")
    plt.xlabel("Healthcare Spending per Person in USD")
    plt.title("Healthcare Spending in the US From 1970-2020")
    plt.savefig("spending.png")
    plt.show()
