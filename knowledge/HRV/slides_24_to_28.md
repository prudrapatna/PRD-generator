# HRV Data (Slides 24-28)
Source: Tidal Progress Deck

## Slide 24: HRV (RMSSD): Raw vs SPLAT

| Time of day | Model | MAE [ms] | RMSE [ms] | Pearson r | Spearman ⍴ | MAPE [%] | NA Percentage [%] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| All-day | Our DL (raw) | 6.95 | 13.85 | 0.797 | 0.869 | 21.1 | 0.0 |
| All-day | Our DL (SPLAT) | 7.15 | 13.92 | 0.790 | 0.863 | 23.0 | 0.0 |
| All-day | Fitbit Legacy | 54.2 | 97.3 | 0.201 | 0.414 | 219.4 | 16.5 |
| Daytime (9a-9p) | Our DL (raw) | 7.05 | 13.85 | 0.799 | 0.866 | 21.1 | 0.0 |
| Daytime (9a-9p) | Our DL (SPLAT) | 7.25 | 13.96 | 0.790 | 0.863 | 23.0 | 0.0 |
| Daytime (9a-9p) | Fitbit Legacy | 56.4 | 99.2 | 0.213 | 0.416 | 225.3 | 16.7 |
| Night-time (1a-6a) | Our DL (raw) | 4.60 | 7.87 | 0.92 | 0.910 | 11.8 | 0.0 |
| Night-time (1a-6a) | Our DL (SPLAT) | 4.61 | 7.78 | 0.92 | 0.916 | 12.4 | 0.0 |
| Night-time (1a-6a) | Fitbit Legacy | 10.2 | 31.7 | 0.389 | 0.764 | 30.7 | 5.0 |
| Nightly | Our DL (raw) | 3.42 | 5.71 | 0.947 | 0.929 | 10.3 | 0.0 |
| Nightly | Our DL (SPLAT) | 3.68 | 6.06 | 0.937 | 0.927 | 11.1 | 0.0 |
| Nightly | Fitbit Legacy | 20.9 | 49.6 | 0.194 | 0.580 | 80.3 | 4.8 |


## Slide 25: HRV (RMSSD) Comparisons

| Time of day | Model | MAE [ms] | RMSE [ms] | Pearson r | Spearman ⍴ | MAPE [%] | NA Percentage [%] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| All-day | Our DL (raw)* | 6.95 | 13.85 | 0.80 | 0.87 | 21.1 | 0.0 |
| All-day | Our DL (SPLAT)* | 7.15 | 13.92 | 0.79 | 0.86 | 23.0 | 0.0 |
| All-day | Fitbit Legacy | 54.2 | 97.3 | 0.20 | 0.41 | 219.4 | 16.5 |
| Rehman et al., 2024 | Corsano | 12.53 | - | - | 0.7 | - | 45.0 |
| Rehman et al., 2024 | Whoop | 9.42 | - | - | 0.76 | - | 60.0 |
| Daytime (9a-9p) | Our DL (raw) | 7.05 | 13.85 | 0.80 | 0.87 | 21.1 | 0.0 |
| Daytime (9a-9p) | Our DL (SPLAT) | 7.25 | 13.96 | 0.79 | 0.86 | 23.0 | 0.0 |
| Daytime (9a-9p) | Fitbit Legacy | 56.4 | 99.2 | 0.21 | 0.42 | 225.3 | 16.7 |
| Daytime (9a-9p) | Corsano | 17.99 | - | - | 0.58 | - | 65.0 |
| Daytime (9a-9p) | Whoop | 11.86 | - | - | 0.67 | - | 80.0 |
| Night-time (1a-6a) | Our DL (raw) | 4.60 | 7.87 | 0.92 | 0.91 | 11.8 | 0.0 |
| Night-time (1a-6a) | Our DL (SPLAT) | 4.61 | 7.78 | 0.92 | 0.92 | 12.4 | 0.0 |
| Night-time (1a-6a) | Fitbit Legacy | 10.2 | 31.7 | 0.39 | 0.76 | 30.7 | 5.0 |
| Night-time (1a-6a) | Corsano | 6.89 | - | - | 0.89 | - | 30.0 |
| Night-time (1a-6a) | Whoop | 7.14 | - | - | 0.86 | - | 35.0 |

*\*All day for our models are skewed towards daytime performance because many participants did not wear the device to sleep*


## Slide 26: HRV: 5-min RMSSD

| Time of day | Model | MAE [ms] | RMSE [ms] | Pearson r | Spearman ⍴ | Availability [%] |
| --- | --- | --- | --- | --- | --- | --- |
| All-day | Our DL (raw)* | 6.95 | 13.85 | 0.80 | 0.87 | ~100 |
| All-day | Our DL (SPLAT)* | 7.15 | 13.92 | 0.79 | 0.86 | ~100 |
| Ref: Rehman et al., 2024 | Corsano | 12.53 | - | - | 0.70 | 55 |
| Ref: Rehman et al., 2024 | Whoop | 9.42 | - | - | 0.76 | 40 |
| Daytime (9a-9p) | Our DL (raw) | 7.05 | 13.85 | 0.80 | 0.87 | ~100 |
| Daytime (9a-9p) | Our DL (SPLAT) | 7.25 | 13.96 | 0.79 | 0.86 | ~100 |
| Daytime (9a-9p) | Corsano | 17.99 | - | - | 0.58 | 35 |
| Daytime (9a-9p) | Whoop | 11.86 | - | - | 0.67 | 20 |
| Night-time (1a-6a) | Our DL (raw) | 4.60 | 7.87 | 0.92 | 0.91 | ~100 |
| Night-time (1a-6a) | Our DL (SPLAT) | 4.61 | 7.78 | 0.92 | 0.92 | ~100 |
| Night-time (1a-6a) | Corsano | 6.89 | - | - | 0.89 | 70 |
| Night-time (1a-6a) | Whoop | 7.14 | - | - | 0.86 | 65 |

*\*All-day for our models are skewed towards daytime performance because many participants did not wear the device to sleep*


## Slide 27: HRV (RMSSD) Comparisons

| Time of day | Model | MAE [ms] | Pearson r | MAPE [%] |
| --- | --- | --- | --- | --- |
| Nightly | Our DL (raw) | 3.42 | 0.95 | 10.3 |
| Nightly | Our DL (SPLAT) | 3.68 | 0.94 | 11.1 |
| Nightly | Fitbit Legacy | 20.9 | 0.19 | 80.3 |
| Dial et al. 2025 | Garmin (Fenix 6) | 5.29 | 0.96 | 10.5 |
| Dial et al. 2025 | Oura (Gen 3) | 3.91 | 0.97 | 7.15 |
| Dial et al. 2025 | Oura (Gen 4) | 3.93 | 0.99 | 6.0 |
| Dial et al. 2025 | Polar (Grit X Pro) | 7.27 | 0.86 | 16.3 |
| Dial et al. 2025 | WHOOP (4.0) | 4.17 | 0.96 | 8.2 |


## Slide 28: Nightly RMSSD

| Time of day | Model | MAE [ms] | Pearson r | MAPE [%] |
| --- | --- | --- | --- | --- |
| Nightly | Our DL (raw) | 3.42 | 0.95 | 10.3 |
| Nightly | Our DL (SPLAT) | 3.68 | 0.94 | 11.1 |
| Nightly | Our DL (raw): Gated | 3.70 | 0.94 | 13.4 |
| Nightly | Our DL (SPLAT): Gated | 2.50 | 0.97 | 10.1 |
| Nightly | Fitbit Legacy | 20.9 | 0.19 | 80.3 |
| Nightly | Fitbit Legacy: Gated✢ | 6.4 | 0.59 | 50.8 |
| Dial et al. 2025 | Garmin (Fenix 6) | 5.29 | 0.96 | 10.5 |
| Dial et al. 2025 | Oura (Gen 3) | 3.91 | 0.97 | 7.15 |
| Dial et al. 2025 | Oura (Gen 4) | 3.93 | 0.99 | 6.0 |
| Dial et al. 2025 | Polar (Grit X Pro) | 7.27 | 0.86 | 16.3 |
| Dial et al. 2025 | WHOOP (4.0) | 4.17 | 0.96 | 8.2 |

*✢In prod, Fitbit algo predictions for each 5-min window are gated by IBI coverage and median value is used; here gating is based on DL confidence for comparison and mean value of 5-min predictions is used*