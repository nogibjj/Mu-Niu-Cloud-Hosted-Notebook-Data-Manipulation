from lib import load, summary, visualize

data_path = "student_performance.csv"

if __name__ == "__main__":
    load(data_path)
    summary(data_path)
    visualize(data_path)
