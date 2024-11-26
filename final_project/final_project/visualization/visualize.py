import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore
import seaborn as sns # type: ignore

def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
    data=df,
    x="date",
    y="value",
    hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");

def top_countries(df,processed_covid_df):
    top_countries = (
        processed_covid_df
        .select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(20)
        .transform_column(
            column_name="country_region",
            function=lambda x: "red" if x in df else "lightblue",
            dest_column_name="color"
        )
    )

    return top_countries

def barplot_highligh(df):
    sns.barplot(
        data=df,
        x="value",
        y="country_region",
        palette=list(df.color)
    );

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");