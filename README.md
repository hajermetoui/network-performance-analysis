# Network Performance Analysis under Impairment

A controlled study of how packet loss, bandwidth, and delay affect TCP throughput, using an emulated network.

## Overview
A two-switch network with a controllable bottleneck link was built in Mininet. TCP throughput was measured with iperf3 while packet loss, bandwidth, and delay were each varied independently, isolating the effect of each factor.

## Key findings
- **Bandwidth:** throughput scales linearly with the configured limit.
- **Packet loss:** throughput collapses non-linearly — e.g. 9.4 → 1.7 Mbit/s as loss rises from 0% to 10% — due to TCP congestion control.
- **Delay:** throughput declines gradually as round-trip time grows.

## Contents
- `mynetwork.py` — Mininet network topology (4 hosts, 2 switches, bottleneck link)
- `plot_results.py` — generates the result figures from the measured data
- `fig_loss.png`, `fig_bandwidth.png`, `fig_delay.png` — result graphs
- `Network_Performance_Report.pdf` — full technical report

## Tools
Mininet · Open vSwitch · Linux · iperf3 · Python (matplotlib)
