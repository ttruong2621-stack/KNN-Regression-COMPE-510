from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/Concrete_Data.xls")


def main() -> None:
    """Inspect the data."""

    data = pd.read_excel(DATA_PATH)

    print("Dataset shape:", data.shape)

    print("\nColumn names:")
    for number, column in enumerate(data.columns, start=1):
        print(f"{number}. {column}")

    print("\nDuplicate rows:")
    print(data.duplicated().sum())

    print("\nNegative-value rows:")
    print((data < 0).any(axis=1).sum())

    print("\nMissing values:")
    print(data.isna().sum())

    print("\nData types:")
    print(data.dtypes)

    print("\nSummary statistics:")
    print(data.describe())

    # Remove duplicate to prevent identical samples appearing in both training and testing sets
    data = pd.read_excel(DATA_PATH, engine="calamine")

    print("Original shape:", data.shape)

    data = data.drop_duplicates().reset_index(drop=True)

    print("Shape after removing duplicates:", data.shape)


if __name__ == "__main__":
    main()
