from email import header
import matplotlib.pyplot as plt
import csv

uwb = [50, 500, 600],[300, 300, 300]
wifi = [60, 50]

plt.figure(figsize=(8,6))
plt.hist(uwb, bins=100, alpha=0.5, label="uwb")
plt.hist(wifi, bins=100, alpha=0.5, label="wifi")
plt.xlabel("Frequency")
plt.ylabel("dB")
plt.legend(loc='upper right')
plt.savefig("hist_test_1.png")
