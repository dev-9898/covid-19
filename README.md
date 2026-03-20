
---

# COVID-19

## Project Description

The **COVID-19 Data Visualizer** is a Python-based data analysis project that allows users to explore COVID-19 datasets and generate different types of visualizations. The program provides a menu-driven interface to view data, statistics, and graphical reports such as bar charts, pie charts, heatmaps, and scatter plots.

This project uses Python libraries like **NumPy, Pandas, Matplotlib, and Seaborn** for data processing and visualization.

---

## Features 

* View dataset information
* Display statistical summary of COVID-19 data
* Top countries COVID cases bar chart
* COVID case distribution pie chart
* Correlation heatmap
* Scatter plot of cases vs deaths
* Option to save graphs as images
* Support for custom datasets

---

## Technologies Used 

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

---

## Project Structure 

```
COVID-19-Visualizer/
│
├── covid_19.py          # Main Python program
├── covid_data.csv       # Default dataset
├── Graphs/              # Saved graphs (optional)
└── README.md            # Project documentation
```

---

## Installation 

### 1 Install Python

Make sure Python 3.x is installed.

### 2 Install required libraries

Run this command:

```bash
pip install numpy pandas matplotlib seaborn
```

---

## Menu Options 

The program provides the following options:

| Option | Function        |
| ------ | --------------- |
| 1      | View Dataset    |
| 2      | Show Statistics |
| 3      | Bar Chart       |
| 4      | Pie Chart       |
| 5      | Heatmap         |
| 6      | Scatter Plot    |
| 7      | Exit            |

---

## Dataset Format 

Your dataset should contain these columns:

* Country/Region
* Confirmed
* Active
* Recovered
* Deaths

Example:

| Country | Confirmed | Active | Recovered | Deaths |
| ------- | --------- | ------ | --------- | ------ |
| India   | 45000000  | 50000  | 44400000  | 530000 |

---

## Example Visualizations 

The project generates:

* Bar charts for top affected countries
* Pie chart for case distribution
* Heatmap for correlation analysis
* Scatter plot for case relationships

---

## Future Improvements 

Possible enhancements:

* GUI interface (Tkinter or Streamlit)
* Real-time API data
* More graph types
* Export reports as PDF
* Country filter option

---

## Author 

**Dev Rathod**

---

If you want, I can also make a **professional GitHub README** (with badges, screenshots section, and better formatting) which looks impressive for placements since you are preparing for IT jobs.
