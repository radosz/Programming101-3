import numpy as np
import matplotlib.pyplot as plt

width = 0.6
color_bar = 'palegreen'
color_text = 'red'


def sort_histogram(histogram):
    keys = [x for x in histogram.keys() if x != "Others"]
    keys.sort()
    keys.append("Others")
    keys = tuple(keys)
    values = [histogram[x] for x in keys]
    max_value = max(values)
    values = tuple(values)
    return (values, keys, max_value)


def histogram_to_plot(histogram):
    ax = plt.subplots()[1]
    values, keys, max_value = sort_histogram(histogram)
    servers = values
    ind = np.arange(len(servers))  # the x locations for the groups
    rect = ax.bar(
        ind + width - width / 2, servers, width, color=color_bar)
    axes = plt.gca()
    max_value += max_value * 0.15
    axes.set_ylim([0, max_value])

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Count')
    ax.set_title('Servers')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(keys)  # Servers  names
    ax = autolabel(rect, ax)
    return ax


def print_plot(histogram):
    ax = histogram_to_plot(histogram)
    plt.show()


def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax.text(rect.get_x() + rect.get_width() / 2., height, '%d' % int(height),
                    ha='center', va='bottom', color=color_text)


def save_histogram(histogram, path_histogram):
    ax = histogram_to_plot(histogram)
    file_s = path_histogram + "/histogram.png"
    plt.savefig(file_s)


def main():
    his = {'nginx': 216, 'Others': 99, 'lghttp': 20, 'Apache': 14, 'IIS': 3}
    print_plot(his)
    save_histogram(his, "/home/rado_sz/Programming101-3/startbg/1-Scan-Bg-Web")

if __name__ == '__main__':
    main()
