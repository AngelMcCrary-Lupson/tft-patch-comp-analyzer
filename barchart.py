import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

def gen_graph(file):
    with open(file) as f:
        comp_data = json.load(f)

    labels = ['First', 'Second', 'Third', 'Fourth']

    comp_array = {
        "Space Shrooms": [],
        "4 Vanguards 4 Mystics": [],
        "6 Cybers": [],
        "Jinx Brawlers": [],
        "6 Sorcs": [],
        "6 BM Slowroll": [],
        "6 Rebels": [],
        "Mech Sorcs": [],
        "Protectors": [],
        "Comp Not Found": []
    }

    for num in range(1,5):
        num_str = f"{num}"
        comp_weight = comp_data[num_str]
        for comp in comp_array.keys():
            comp_array[comp].append(comp_weight[comp])

    x = np.arange(len(labels))  # the label locations
    width = 0.05  # the width of the bars

    fig, ax = plt.subplots()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 10, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    index = 0
    for comp_name in comp_array.keys():
        rect = ax.bar(x + index*width, comp_array[comp_name], width, label=comp_name)
        autolabel(rect)
        x_coor = x + index*width

        index += 1
        if index >= 10:
            index = 0

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by placement and comp')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    fig.tight_layout()

    # plt.show() For showing the graph without GUI implementation
    return fig
