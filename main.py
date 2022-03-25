import pandas as pd
import statistics
import eda
import datetime


def summary_statistics():
    print(f"[CALC STATS][TIME - {datetime.datetime.now()}]")
    data = import_data()
    statistics.summary_statistics(data)


def exploratory_analysis():
    print(f"[EXP. ANALYSIS][TIME - {datetime.datetime.now()}]")
    data = import_data()
    eda.exploratory_analysis(data)


def import_data():
    data = pd.read_excel('../data/transacties.xlsx')

    print(data)

    return data



