from lib import load, summary, visualize

import pandas as pd
import warnings

warnings.filterwarnings("ignore")

path = "student_performance.csv"
original_data = pd.read_csv(path)


def test_load():
    result_load_data = load(path)
    assert original_data.equals(result_load_data), "Test has failed."


def test_summary():
    data = load(path)
    result_summary = summary(path)
    expected_final_mean = data["final_grade"].mean()
    result_final_mean = result_summary.iloc[1, 2]
    assert expected_final_mean == result_final_mean, "Test has failed."


def test_visualize():
    assert visualize(path) is None, "Test has failed."


if __name__ == "__main__":
    test_load()
    test_summary()
    test_visualize()
