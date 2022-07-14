import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

def plot(runs, show):
    fig, ax = plt.subplots(figsize=(10, 6), layout='tight')
    ax.set(xscale='log', yscale='log', ylim=(3e-5,5e-2))
    sns.scatterplot(
        x='Effective Resolution',
        y='Relative Error',
        style='Variable',
        markers={'Total Energy': 's', 'Temperature': '^'},
        size='Polynomial Order',
        palette='bright',
        hue='State Variables',
        sizes=(40, 200),
        alpha=.7,
        ax=ax,
        data=runs,
    )
    plt.legend(loc='upper right')
    if show:
        plt.show()
    return fig


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get input arguments')
    parser.add_argument('-f',
                        dest='conv_result_file',
                        type=str,
                        help='Path to the CSV file')
    parser.add_argument('-o',
                        dest='output_file',
                        type=str,
                        help='Output file for figure')
    parser.add_argument('--show',
                        default=False,
                        action='store_true',
                        help='Show figure')
    args = parser.parse_args()
    runs = pd.read_csv(args.conv_result_file)
    
    fig = plot(runs, args.show)
    if args.output_file:
        plt.savefig(args.output_file)
