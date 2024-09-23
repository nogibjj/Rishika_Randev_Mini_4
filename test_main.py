from main import generate_histogram, generate_summary_stats


def test_generate_stats():
    """testing out summary stats function"""
    summary, medians = generate_summary_stats()[0], generate_summary_stats()[1]
    assert int(summary.loc["mean"]["Spending_USD"]) == 2789
    assert medians["Life_Expectancy"] == 78.100


def test_generate_histogram():
    generate_histogram()


if __name__ == "__main__":
    test_generate_histogram()
    test_generate_stats()
