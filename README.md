ECG signal processing and heart rate variability (HRV) analysis using Python.

---

## Project Overview

This project focuses on ECG signal processing and heart rate variability (HRV) analysis using Python. Raw ECG signals are filtered to remove noise, R-peaks are detected, and clinically relevant HRV metrics such as SDNN and RMSSD are computed. The analysis is performed on two ECG leads (MLII and V5) to assess the robustness of R-peak detection and HRV estimation across different leads.

This project is intended for educational and signal analysis purposes and is **not for clinical diagnosis**.

---

## Dataset

The ECG data used in this project is obtained from the **MIT-BIH Arrhythmia Database**, a widely used public dataset for ECG research.

- Source: MIT-BIH Arrhythmia Database  
- Sampling frequency: **360 Hz**
- Leads used:
  - **MLII** (Modified Lead II)
  - **V5** (Precordial chest lead)

Due to data redistribution policies, raw ECG files are **not included** in this repository.

### How to obtain the data
You may download the dataset from:
- https://physionet.org/content/mitdb/
- or Kaggle (MIT-BIH Arrhythmia Database – Simple CSVs)

Place the ECG CSV file inside a local `data/` folder before running the code.

---

## Methodology

The analysis pipeline consists of the following steps:

1. **ECG Signal Loading**
   - ECG signals are read from a CSV file containing multiple leads.

2. **Bandpass Filtering**
   - A Butterworth bandpass filter (0.5–40 Hz) is applied to remove baseline wander and high-frequency noise.

3. **R-Peak Detection**
   - R-peaks are detected using a prominence-based peak detection approach.
   - A minimum distance constraint ensures physiologically valid heartbeats.

4. **Heart Rate Calculation**
   - RR intervals are computed from detected R-peaks.
   - Instantaneous and average heart rate are calculated.

5. **Heart Rate Variability (HRV) Metrics**
   - **SDNN**: Standard deviation of NN (RR) intervals, representing overall HRV.
   - **RMSSD**: Root mean square of successive RR interval differences, reflecting short-term parasympathetic activity.

6. **Multi-Lead Comparison**
   - HR and HRV metrics are computed independently for MLII and V5 leads.
   - Results are compared to assess consistency across ECG leads.

---

## Results

The analysis produces:
- Average heart rate (bpm)
- HRV metrics (SDNN and RMSSD)
- ECG plots with detected R-peaks for both MLII and V5 leads

Example outputs include:
- ECG waveform with R-peak annotations
- Side-by-side visualization of MLII and V5 leads

All generated plots are saved in the `plots/` directory.

---

## Interpretation (Educational)

- A physiologically normal average heart rate was observed.
- SDNN indicated moderate-to-high overall heart rate variability.
- RMSSD showed elevated short-term variability, suggesting strong parasympathetic modulation.

These results are interpreted **only for educational signal analysis**, as they are based on short-duration, single-subject ECG data.


