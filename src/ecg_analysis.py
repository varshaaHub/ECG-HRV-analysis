# ECG Signal Processing and HRV Analysis
# Educational purpose only – Not for clinical use

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# --------------------------------------------------
# 1. Load ECG data
# --------------------------------------------------

# Read CSV file (contains multiple leads)
ecg_data = pd.read_csv("data/ecg.csv")

# Select ECG leads
ecg_signal = ecg_data["MLII"].values   # Modified Lead II
ecg_signal_v5 = ecg_data["V5"].values  # Chest lead V5

# Sampling frequency (MIT-BIH standard)
fs = 360  # Hz



# --------------------------------------------------
# 2. Bandpass filter (0.5–40 Hz)
# --------------------------------------------------

def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return filtfilt(b, a, signal)

filtered_ecg = bandpass_filter(ecg_signal, 0.5, 40, fs)
filtered_ecg_v5 = bandpass_filter(ecg_signal_v5, 0.5, 40, fs)



# --------------------------------------------------
# 3. R-peak detection (robust, prominence-based)
# --------------------------------------------------

peaks, _ = find_peaks(
    filtered_ecg,
    distance=0.6 * fs,
    prominence=0.4 * np.std(filtered_ecg)
)

peaks_v5, _ = find_peaks(
    filtered_ecg_v5,
    distance=0.6 * fs,
    prominence=0.4 * np.std(filtered_ecg_v5)
)

print("Number of R-peaks detected (MLII):", len(peaks))
print("Number of R-peaks detected (V5):", len(peaks_v5))



# --------------------------------------------------
# 4. Heart Rate calculation
# --------------------------------------------------

rr_intervals = np.diff(peaks) / fs
heart_rate = 60 / rr_intervals
avg_hr = np.mean(heart_rate)

rr_intervals_v5 = np.diff(peaks_v5) / fs
heart_rate_v5 = 60 / rr_intervals_v5
avg_hr_v5 = np.mean(heart_rate_v5)



# --------------------------------------------------
# 5. HRV metrics
# --------------------------------------------------
# SDNN: overall HRV (sympathetic + parasympathetic)
# RMSSD: short-term HRV (parasympathetic)

sdnn = np.std(rr_intervals)
rmssd = np.sqrt(np.mean(np.diff(rr_intervals) ** 2))

sdnn_v5 = np.std(rr_intervals_v5)
rmssd_v5 = np.sqrt(np.mean(np.diff(rr_intervals_v5) ** 2))



# --------------------------------------------------
# 6. Plot ECG segment with R-peaks (MLII & V5)
# --------------------------------------------------

segment_length = 3000  # ~8 seconds

# MLII segment
segment_mlii = filtered_ecg[:segment_length]
segment_peaks_mlii = peaks[peaks < segment_length]

# V5 segment
segment_v5 = filtered_ecg_v5[:segment_length]
segment_peaks_v5 = peaks_v5[peaks_v5 < segment_length]

plt.figure(figsize=(12, 6))

# Plot MLII
plt.subplot(2, 1, 1)
plt.plot(segment_mlii, label="Filtered ECG (MLII)")
plt.plot(segment_peaks_mlii,
         segment_mlii[segment_peaks_mlii],
         "r*", label="R-peaks")
plt.title("ECG Signal with R-Peak Detection – MLII Lead")
plt.ylabel("Amplitude")
plt.legend()

# Plot V5
plt.subplot(2, 1, 2)
plt.plot(segment_v5, label="Filtered ECG (V5)")
plt.plot(segment_peaks_v5,
         segment_v5[segment_peaks_v5],
         "r*", label="R-peaks")
plt.title("ECG Signal with R-Peak Detection – V5 Lead")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.savefig("plots/ecg_mlii_v5_comparison.png")
plt.show()



# --------------------------------------------------
# 7. Print results
# --------------------------------------------------

print("\n--- MLII Results ---")
print(f"Average Heart Rate: {avg_hr:.2f} bpm")
print(f"SDNN: {sdnn:.4f} s")
print(f"RMSSD: {rmssd:.4f} s")

print("\n--- V5 Results ---")
print(f"Average Heart Rate: {avg_hr_v5:.2f} bpm")
print(f"SDNN: {sdnn_v5:.4f} s")
print(f"RMSSD: {rmssd_v5:.4f} s")


