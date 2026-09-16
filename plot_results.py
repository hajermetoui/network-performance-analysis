"""
plot_results.py — generates the three throughput figures from the
network performance experiments (Mininet, iperf3).
Run: python3 plot_results.py
"""
import matplotlib.pyplot as plt

# Measured throughput (Mbit/s), receiver-side, from iperf3
loss_x  = [0, 1, 2, 5, 10];      loss_y = [9.41, 9.19, 7.11, 5.23, 1.67]
bw_x    = [1, 5, 10, 20, 50];    bw_y   = [0.90, 4.72, 9.44, 18.9, 47.4]
delay_x = [1, 10, 50, 100, 200]; delay_y = [9.42, 9.37, 8.95, 8.08, 6.47]

BLUE = "#2c5a8c"

def chart(x, y, xlabel, title, fname):
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    ax.plot(x, y, marker='o', color=BLUE, linewidth=2, markersize=6,
            markerfacecolor=BLUE, markeredgecolor='white', zorder=3)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel("TCP throughput (Mbit/s)", fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=10)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    fig.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close(fig)

chart(loss_x,  loss_y,  "Packet loss (%)",             "Throughput vs. Packet Loss", "fig_loss.png")
chart(bw_x,    bw_y,    "Configured bandwidth (Mbit/s)", "Throughput vs. Bandwidth",   "fig_bandwidth.png")
chart(delay_x, delay_y, "One-way delay (ms)",           "Throughput vs. Delay",       "fig_delay.png")
print("Saved fig_loss.png, fig_bandwidth.png, fig_delay.png")
