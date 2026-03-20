import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Dataset selection menu
    print("\nDataset Menu:")
    print("1 Default Dataset")
    print("2 Use Your Own Dataset")

    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            df = pd.read_csv("F:/Visualizer/covid_data.csv")
        case 2:
            path = input("Enter your dataset CSV path: ")
            df = pd.read_csv(path)
        case _:
            print("Invalid choice")
            exit()

    while True:
        print("\n========== MENU ==========")
        print("1 View Dataset")
        print("2 Show Statistics")
        print("3 Bar Chart (Top Countries)")
        print("4 Pie Chart")
        print("5 Heatmap")
        print("6 Scatter Plot")
        print("7 Exit")

        choice = int(input("\nEnter your choice: "))

        match choice:
            # View Dataset Information
            case 1:
                print("\n===== FIRST 5 ROWS =====")
                print(df.head())

                print("\n===== LAST 5 ROWS =====")
                print(df.tail())

                print("\n===== DATASET INFO =====")
                print(df.info())

                print("\n===== MISSING VALUES =====")
                print(df.isnull().sum())

            # Statistics
            case 2:
                print("\n===== COVID-19 STATISTICS =====")
                print("Total Cases :", df['Confirmed'].sum())
                print("Active Cases :", df['Active'].sum())
                print("Recovered :", df['Recovered'].sum())
                print("Deaths :", df['Deaths'].sum())

                print("\nTop 5 Countries by Total Cases\n")
                top = df.sort_values(by="Confirmed", ascending=False)
                print(top[['Country/Region','Confirmed']].head())

            # Bar Chart
            case 3:
                top_states = df.sort_values(by="Confirmed", ascending=False).head(10)
                fig = plt.figure(figsize=(12,6))
                plt.bar(top_states["Country/Region"],
                        top_states["Confirmed"],
                        color="royalblue")
                plt.title("Top 10 Countries by COVID Cases",fontsize=14)
                plt.xlabel("Countries",fontsize=12)
                plt.ylabel("Total Cases",fontsize=12)
                plt.xticks(rotation=45)
                plt.grid(axis="y",linestyle="--",alpha=0.6)
                plt.show()

                save=input("Save graph? (yes/no): ")

                match save.lower():
                    case "yes":
                        name=input("Enter file name: ")
                        fig.savefig(name+".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            # Pie Chart
            case 4:
                values = [
                    df['Active'].sum(),
                    df['Recovered'].sum(),
                    df['Deaths'].sum()
                ]

                labels = ["Active", "Recovered", "Deaths"]
                colors = ["#FFA500", "#4CAF50", "#FF4C4C"]
                explode = (0,0.08,0)
                fig = plt.figure(figsize=(7,7))

                def autopct_format(pct):
                    return f'{pct:.1f}%' if pct > 1 else ''

                plt.pie(values,
                        labels=labels,
                        colors=colors,
                        autopct=autopct_format,
                        startangle=140,
                        explode=explode,
                        textprops={'fontsize':12},
                        wedgeprops={'edgecolor':'white'})
                plt.title("COVID-19 Case Distribution",
                          fontsize=16,
                          weight='bold')
                plt.axis("equal")
                plt.show()

                save=input("Save graph? (yes/no): ")

                match save.lower():
                    case "yes":
                        name=input("Enter file name: ")
                        fig.savefig(name+".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            # Heatmap
            case 5:
                ratio_data = df[['Confirmed','Deaths','Recovered','Active']]
                corr = ratio_data.corr()
                fig = plt.figure(figsize=(6,5))
                sns.heatmap(corr,
                            annot=True,
                            cmap="coolwarm",
                            linewidths=1)
                plt.title("COVID Correlation Heatmap")
                plt.show()

                save=input("Save graph? (yes/no): ")

                match save.lower():
                    case "yes":
                        name=input("Enter file name: ")
                        fig.savefig(name+".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            # Scatter Plot
            case 6:
                fig = plt.figure(figsize=(8,6))
                plt.scatter(df["Confirmed"],
                            df["Deaths"],
                            color="purple")
                plt.title("Total Cases vs Deaths")
                plt.xlabel("Total Cases")
                plt.ylabel("Deaths")
                plt.grid(True)
                plt.show()

                save=input("Save graph? (yes/no): ")
                match save.lower():
                    case "yes":
                        name=input("Enter file name: ")
                        fig.savefig(name+".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            case 7:
                print("\nProgram Closed")
                break

            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()