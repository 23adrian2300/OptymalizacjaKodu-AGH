#!/usr/bin/python3

import csv
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import re


OUTPUT_FILES_DIR = "."
MAX_GFLOPS = 27.0 # should be 44.8 in my processor's case, lowered to make the plots more readable


def get_series_entries(fname_pattern):
    entries = []
    for entry in os.scandir(OUTPUT_FILES_DIR):
        if entry.is_file() and \
        fname_pattern.match(entry.name):
            entries.append(entry)
    return entries


def get_legend_str(fname):
    return fname.replace("output_", "").replace(".csv", "")


def get_labels_order(labels):
    A = [(int(labels[i].replace("MMult", "").split("_")[-1]), i) for i in range(len(labels))]
    return [e[1] for e in sorted(A)]


def plot(fname_pattern_str, save_fname):
    print(f"plotting {fname_pattern_str}")
    fname_pattern = re.compile(fname_pattern_str)
    series_entries = get_series_entries(fname_pattern)

    figure(figsize=(9, 6), dpi=80)
    # Avoid repeating label colors
    # colormap = plt.cm.nipy_spectral#
    colormap1 = plt.cm.nipy_spectral
    colormap2 = plt.cm.tab10
    #colors = colormap(np.linspace(0, 0.9, len(series_entries)))
    # Generowanie 20 kolorów z palety tab20
    colors1 = colormap1(np.linspace(0, 1, 20))

    # Dodanie kolejnych 3 kolorów z palety tab10
    colors2 = colormap2(np.linspace(0, 1, 10))

    # Połączenie kolorów
    colors = np.vstack([colors1, colors2])

    # Wybranie tylko 23 unikalnych kolorów
    colors = colors[np.random.choice(colors.shape[0], len(series_entries), replace=False), :]
    ax = plt.gca()
    ax.set_prop_cycle('color', colors)
    
    for entry in series_entries:
        with open(entry.path) as f:  
            line_reader = csv.reader(f, delimiter=',')
            xlabel, ylabel = tuple(v.strip() for v in next(line_reader))
            x = []
            y = []
            for row in line_reader:
                x.append(int(row[0]))
                y.append(float(row[1]))
            plt.plot(x, y, label=get_legend_str(entry.name), marker="o")
    
    ax.set_xlim([40, 800])
    ax.set_ylim([0, MAX_GFLOPS])            
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    handles, labels = ax.get_legend_handles_labels()
    order = get_labels_order(labels)
    plt.legend([handles[idx] for idx in order], [labels[idx] for idx in order], bbox_to_anchor=(1.04, 0.5), loc="center left")
    plt.subplots_adjust(right=0.75)

    plt.savefig(save_fname, bbox_inches="tight")
    print(f"saved as {save_fname}")


plot("^output_MMult0.csv$", "plot_initial.png")
plot("^output_MMult[0-9]+.csv$", "plot_common.png")
plot("^output_(MMult0|MMult_1x4_[0-9])+.csv$", "plot_1x4.png")
plot("^output_(MMult0|MMult_4x4_[0-9]+).csv$", "plot_4x4.png")
plot("^output_MMult(_[0-9]+x[0-9]+_)?[0-9]+.csv$", "plot_all.png")