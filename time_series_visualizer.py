import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates = True, names=["date","views"], header=0)

# Clean data
df = df.drop(df[(df['views'] > df['views'].quantile(0.975)) |(df['views'] < df['views'].quantile(0.025))].index)


def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots()
    ax=plt.plot(df.index,df["views"])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=df
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    df_bar=df_bar.groupby(["year","month"]).mean().reset_index()

    # Draw bar plot
    fig,ax=plt.subplots()
    ax=sns.barplot(data=df_bar, x="year",y="views", hue="month", hue_order=["January", "February", "March", "April","May", "June", "July", "August", "September", "October", "November", "December"])
    ax.set(xlabel='Years', ylabel='Average Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(15,6))
    sns.boxplot(data=df_box, x="year", y="views", ax=ax[0], palette="pastel")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Average Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(data=df_box, x="month", y="views", order=month_order, ax=ax[1], palette="pastel")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Average Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
