"""Reusable EDA helpers for the FoodHub data analysis notebook."""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_numeric_distribution(
    df: pd.DataFrame,
    column: str,
    title: str | None = None,
    figsize: tuple[float, float] = (12, 4),
) -> None:
    """Plot histogram+KDE and boxplot side-by-side, then print describe() summary."""
    label = title or column.replace("_", " ").title()

    fig, axes = plt.subplots(1, 2, figsize=figsize)

    sns.histplot(data=df, x=column, kde=True, ax=axes[0])
    axes[0].set_title(f"Distribution of {label}")
    axes[0].set_xlabel(label)

    sns.boxplot(data=df, x=column, ax=axes[1])
    axes[1].set_title(f"Boxplot of {label}")
    axes[1].set_xlabel(label)

    fig.tight_layout()
    plt.show()

    print(df[column].describe())


def plot_categorical_summary(
    df: pd.DataFrame,
    column: str,
    title: str | None = None,
    figsize: tuple[float, float] = (10, 4),
    sort_by_frequency: bool = True,
) -> None:
    """Plot countplot (sorted by frequency by default) and print value proportions."""
    label = title or column.replace("_", " ").title()
    order = df[column].value_counts().index.tolist() if sort_by_frequency else None

    plt.figure(figsize=figsize)
    ax = sns.countplot(data=df, x=column, order=order)
    ax.set_title(f"Order count by {label}")
    ax.set_xlabel(label)
    ax.set_ylabel("Order count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    print(df[column].value_counts(normalize=True).round(4))
