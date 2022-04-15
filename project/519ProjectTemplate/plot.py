import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def read_csv_file():
    with open('results.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        compile_times = defaultdict(list)
        key_gen_times = defaultdict(list)
        encrypt_times = defaultdict(list)
        exec_times = defaultdict(list)
        decrypt_times = defaultdict(list)
        ref_exec_times = defaultdict(list)
        mse = defaultdict(list)

        sim_count = defaultdict(list)

        next(csv_reader)
        for row in csv_reader:
            compile_times[int(row[0])].append((float(row[2])))
            key_gen_times[int(row[0])].append((float(row[3])))
            encrypt_times[int(row[0])].append((float(row[4])))
            exec_times[int(row[0])].append((float(row[5])))
            decrypt_times[int(row[0])].append((float(row[6])))
            ref_exec_times[int(row[0])].append((float(row[7])))
            mse[int(row[0])].append((float(row[8])))

        plot_box_chart(compile_times, "Compile Time vs Number of Nodes", "Compile Time (ms)","Number of Nodes")
        plot_box_chart(key_gen_times, "Key Generation Time vs Number of Nodes", "Key Generation Time (ms)","Number of Nodes")
        plot_box_chart(encrypt_times, "Encryption Time vs Number of Nodes", "Encryption Time (ms)","Number of Nodes")
        plot_box_chart(exec_times, "Execution Time vs Number of Nodes", "Execution Time (ms)","Number of Nodes")
        plot_box_chart(decrypt_times, "Decryption Time vs Number of Nodes", "Decryption Time (ms)","Number of Nodes")
        plot_box_chart(ref_exec_times, "Reference Execution Time vs Number of Nodes", "Reference Execution Time (ms)","Number of Nodes")
        plot_box_chart(mse, "Mse vs Number of Nodes", "Mse","Number of Nodes")


def plot_box_chart(nodes_to_times, plot_name, y_axis_name, x_axis_name):   
    data = []
    red_circle = dict(markerfacecolor='white', marker='o', markeredgecolor='red')
    for key in nodes_to_times:
        data.append(nodes_to_times[key])

    fig, ax = plt.subplots()
    ax.boxplot(data, flierprops=red_circle)
    ax.set_xticklabels(nodes_to_times.keys())
    ax.set_xlabel(x_axis_name)
    ax.set_ylabel(y_axis_name)
    ax.set_title(plot_name, fontweight='bold')
    plt.savefig(plot_name.replace(" ","")+f".png")  

if __name__ == "__main__":
    read_csv_file()    