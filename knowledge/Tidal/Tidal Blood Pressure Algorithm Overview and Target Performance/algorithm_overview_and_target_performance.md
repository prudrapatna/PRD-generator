# Tidal Principles of Operation and Algorithm Development

## Revision History

| Rev | Author | Revision Summary |
| :--- | :--- | :--- |
| A | Ming-Zher Poh | Initial version. |

---

## Table of Contents

1.  [Purpose](#1-purpose)
2.  [Scope](#2-scope)
3.  [Introduction](#3-introduction)
4.  [Principles of Operation](#4-principles-of-operation)
    *   [4.1 Background Information](#41-background-information)
    *   [4.2 Definition of Hypertension and Reference Device](#42-definition-of-hypertension-and-reference-device)
    *   [4.3 Overview of the Google Hypertension Notification Algorithm](#43-overview-of-the-google-hypertension-notification-algorithm)
        *   [4.3.1 Height Input](#431-height-input)
        *   [4.3.2 On-device Waveform Compression](#432-on-device-waveform-compression)
        *   [4.3.3 Waveform Decompression](#433-waveform-decompression)
        *   [4.3.4 Signal Quality Check](#434-signal-quality-check)
        *   [4.3.5 Waveform Foundation Model](#435-waveform-foundation-model)
        *   [4.3.6 User-level Aggregation](#436-user-level-aggregation)
        *   [4.3.7 Wear Duration Check](#437-wear-duration-check)
        *   [4.3.8 Wear Pattern Check](#438-wear-pattern-check)
        *   [4.3.9 Hypertension Classification](#439-hypertension-classification)
5.  [Model Development](#5-model-development)
    *   [5.1 Waveform Foundation Model](#51-waveform-foundation-model)
        *   [5.1.1 Dataset](#511-dataset)
        *   [5.1.2 Model Architecture](#512-model-architecture)
        *   [5.1.3 Self-supervised Learning](#513-self-supervised-learning)
    *   [5.2 Hypertension Classification Model](#52-hypertension-classification-model)
        *   [5.2.1 Supervised Learning](#521-supervised-learning)
        *   [5.2.2 Operating Point / Threshold Selection](#522-operating-point--threshold-selection)
        *   [5.2.3 Algorithm Testing](#523-algorithm-testing)

---

## 1. Purpose

This document describes the technical principles that guided the development of the algorithm for the Google Hypertension Notification feature, along with details of how the algorithm works. The Google Hypertension Notification feature is also known as Project Tidal.

## 2. Scope

This document describes the principles of operation and development of the algorithm for the Google Hypertension Notification feature.

## 3. Introduction

Hypertension is the largest modifiable public health challenge and remains the leading risk factor for cardiovascular disease and death globally, accounting for 10.4 million deaths per year. Often asymptomatic, it significantly raises risks of stroke, heart attack, kidney disease, and heart failure. The sustained force of blood against artery walls damages vessels, leading to severe complications, often before symptoms manifest.

The Google Hypertension Notification feature is a software-only mobile medical application intended to identify signs suggestive of hypertension by analyzing photoplethysmography (PPG) and motion data acquired from qualified compatible consumer wrist-worn products.

## 4. Principles of Operation

### 4.1. Background Information

Mean arterial pressure (MAP) is the driving force for flow in the systemic circulation and is determined by cardiac output (CO) and total peripheral resistance, which is also known as systemic vascular resistance (SVR). CO in turn is determined by stroke volume (SV) and heart rate (HR).

Individuals with established hypertension have increased SVR. CO and SV are generally normal or reduced, although HR may be higher than in normals (Lund-Johansen, Clin Sci, 1980). Hypertension induces changes in collagen and elastin, leading to vascular stiffness and remodeling (Kim, Clin Hypertens, 2023). This relationship between arterial stiffness and BP is reciprocal. Increased arterial stiffness diminishes the artery's capacity to expand and contract with blood pressure fluctuations. Consequently, reduced elasticity can elevate systolic BP and pulse pressure. Stiffer arteries cannot adequately accommodate the blood surge during each heartbeat, leading to this elevation. Furthermore, pulse waves travel faster in stiff arteries, resulting in a quicker return of the reflected wave to the heart, which coincides with the systolic phase. This phenomenon further raises systolic BP and widens pulse pressure, which in turn can further exacerbate arterial stiffening.

The invention of photoplethysmography (PPG) technology enables recordings of the contour of the pulse waveform to be obtained in a non-invasive manner (Hertzman, Proc Soc Exp Biol Med, 1937). The effects of hypertension on the dynamics of the arterial system manifest as alterations in the pulse contour that have been observed in both the finger and radial pulse waveform (Dillon and Hertzman, Am Heart J, 1941). These changes are hypothesized to be due to an increase in pulse wave velocity associated with an increase in vessel stiffness, resulting in a faster return of the reflected pulse wave.

### 4.2. Definition of Hypertension and Reference Device

Hypertension is defined as 24-hour average systolic BP (SBP) ≥130 mmHg and/or diastolic BP (DBP) ≥ 80 mmHg based on reference 24-hour ambulatory BP monitoring (ABPM) in accordance with the International Society of Hypertension (ISH) Global Hypertension Practice guidelines (Unger et al., Hypertension, 2020).

### 4.3. Overview of the Google Hypertension Notification Algorithm

An overview of the system design for the Google Hypertension Notification is shown in Figure 1. The observation window for the feature is every 30 days from the day a user enrolls to the feature. This is a passive and recurring detection feature, i.e after every 30 days a new observation period starts automatically. By leveraging passive longitudinal observations, we aggregate multiple measurements over time to find stable patterns suggestive of hypertension.

To be able to run the classification algorithm and generate a notification if a user shows signs suggestive of hypertension, the minimum conditions to be met include at least 14 valid wear days in a 30 day window, where a valid day is defined as having at least 12 hours of wear time in a single day.

The Google Hypertension Notification feature leverages the information contained in the wrist PPG pulse waveform contour, information from motion signals measured by a tri-axial accelerometer, and a user’s self-reported height. The wrist-worn wearable sensors relevant to this application are:

*   **Green PPG (wavelength centered at 528 nm)**
    *   The watch’s light emitting diodes (LEDs) emit controlled pulses of light and capture the returned light using photodiodes. The emitted photons reflect off skin, tissue, bones and blood. An analog front end (AFE) controls the LEDs and converts the analog current received by the photodiodes into a digital PPG signal. Changes associated with peripheral perfusion, due to contraction of the heart, enable measurement of pulsatility, heart rate, and pulse waveform contour in the PPG signal.
*   **Tri-axial accelerometer (x, y, z)**
    *   Data from the corresponding time-aligned tri-axial accelerometer (ACCEL) is useful to provide information on the magnitude of motion associated with each pulse in the PPG signal. This is helpful for the model to learn which sections of the PPG waveform to pay attention to.

> **Figure 1.** Overview of the Google Hypertension Notification feature. (Note: Image not included in text extraction)

Details of the different parts are described below:

#### 4.3.1. Height Input

The user is prompted to confirm their height in feet and inches (if in the US) or in centimeters (if OUS) as part of enrolling in the feature. The value is pre-populated from their user profile. Body height serves as an input to the Google Hypertension Notification algorithm because the shape of the PPG waveform is directly related to the time it takes for the pulse wave to travel through the arterial tree, which is assumed to be proportional to body height (Millasseau et al., J Hypertens, 2006).

If the user’s height is outside of the global limits (the shortest height recorded is 1 ft 9.5 in and the tallest height is 8 ft 11 in), it is considered invalid. A value will not be pre-populated and the user will need to enter a valid height. The self-reported height information is sent to the Fitbit backend and stored in a converted millimeter unit. If the user updates their height in the Fitbit Profile post-onboarding, the HTN algorithm will leverage the new value. The HTN algorithm converts the height units to inches for subsequent processing.

#### 4.3.2. On-device Waveform Compression

First, the DC component of the green PPG signal is removed. The PPG signal is then bandpass filtered using a fourth-order Butterworth filter (0.5-12 Hz) and dynamically normalized using an exponential moving average of the mean and standard deviation (alpha=0.01). The preprocessed PPG and tri-axis ACCEL signals sampled at 25 Hz are then compressed into tokens using an on-device sensor compression encoder to enable power and memory efficient data transfer. The sensor compression tokens are transmitted to the Fitbit cloud backend periodically during syncs with wrist worn device.

#### 4.3.3. Waveform Decompression

In the cloud backend, the tokens are passed to a sensor compression decoder to decompress and reconstruct the PPG and tri-axis ACCEL signals. The signals are divided into 15-sec segments for further processing. The PPG and ACCEL signals are bandpass filtered at 1-12 Hz and 0.5-50 Hz, respectively. The magnitude of the tri-axis ACCEL signals is computed as: `sqrt(x^2 + y^2 + z^2)`.

#### 4.3.4. Signal Quality Check

Next, a series of quality checks are performed to determine if the PPG and magnitude ACCEL waveforms are valid:

*   The corresponding HR from the PPG signal must be between 30 to 200 bpm
*   The PPG and magnitude ACCEL signals cannot be flat lines (i.e. standard deviation must > 0.1)
*   The PPG and magnitude ACCEL sampling rate must be 25 Hz
*   The PPG data must have a signal quality index (SQI) ≥ 0.5 based on template matching (Li and Clifford, Physiol Meas, 2012)
*   The Pearson correlation coefficient of PPG and the corresponding magnitude ACCEL vector magnitude must be < 0.9 to exclude periodic motion artifacts
*   Height check - performed during onboarding (4.3.1). If height was modified we repeat the checks.

#### 4.3.5. Waveform Foundation Model

If the PPG and magnitude ACCEL waveforms pass the quality checks, they are passed to a machine learning (ML)-based Waveform Foundation Model. The Waveform Foundation Model is a general purpose ML model trained to create rich representations, also called embeddings, from multimodal physiological waveforms. For each pair of PPG and magnitude ACCEL segments, the Waveform Foundation Model produces an embedding containing 256 elements. These embeddings contain features the ML model learned to extract from the input waveforms. For the Google Hypertension Notification algorithm, the most important features are correlated to key PPG features that have been reported to be associated with blood pressure (Figure 2), including the b-d area (Liang et al., Diagnostics, 2018), b-d slope, d/a ratio, b/a ratio (Hashimoto et al., Am J Hypertens, 2005; Hashimoto et al., J Hypertens, 2002) of the second derivative and maximum slope during systole.

> **Figure 2.** Magnitude of correlation coefficients between the top ten elements of the waveform embeddings (by feature importance for the Google Hypertension Notification algorithm) and known PPG features. (Note: Image not included)

#### 4.3.6. User-level Aggregation

After waveform embeddings are created for all valid segments in the 30 day window, they are mean-aggregated by hour of day across days to create up to 24 hour-of-day embeddings. These hour-of-day embeddings are then mean-aggregated to produce a single user embedding (Figure 3). Lastly, the user’s height is Z-score normalized and concatenated to the user embedding, forming a vector of 257 elements representing the final user embedding.

> **Figure 3.** Aggregation of waveform embeddings to create a user-level embedding. (Note: Image not included)

#### 4.3.7. Wear Duration Check

Before proceeding to the Hypertension Classification stage, we check if the user wore the device for a sufficient amount of time. A minimum wear duration is ≥ 14 valid days of wear in the 30 day observation window, where a valid day is defined as having ≥ 12 hours of wear per day. The number of valid wear days do not have to be contiguous. If the user does not meet the wear duration requirement, no further processing is conducted and no hypertension notification is triggered.

#### 4.3.8. Wear Pattern Check

If the user meets the wear duration requirement, we check their wear patterns to determine if the user embedding contains measurements during the night (sleep) or only during daytime. This is done using data from the on-device sleep classifier, which is outside the Tidal feature and outside the Tidal SaMD boundary, to compute the total duration of sleep for the day. If the total duration of sleep is greater than 3 hours, the 257-element user embedding is passed to the All-day model (trained on data across all 24 hours of the day) for hypertension classification. If not, it is passed to the Awake model (trained on data across the hours of 9a to 9p only) for hypertension classification.

#### 4.3.9. Hypertension Classification

The hypertension classification model returns a predicted probability of hypertension, also called a hypertension score, ranging from 0 to 1. Figure 4 shows the key morphological characteristics of the PPG waveform associated with model-predicted probability of hypertension. The visual differences are most pronounced in the maximum slope during systole (seen in the first derivative) and the b-d area of the second derivative.

> **Figure 4.** Mean template PPG waveforms with low to high model-predicted hypertension. (Note: Image not included)

The predicted probability of hypertension is correlated with the mean 24-hour blood pressure (Figure 5). If the predicted probability of hypertension exceeds a fixed threshold (0.5699093902474069), a notification indicating signs suggestive of hypertension is triggered. If not, no notification is produced.

> **Figure 5.** Correlation between hypertension classification model predicted probability of hypertension (HTN) and 24-hour mean arterial pressure (MAP) from ambulatory blood pressure monitoring (ABPM). (Note: Image not included)

## 5. Model Development

### 5.1. Waveform Foundation Model

To develop a general purpose ML model capable of extracting meaningful representations (embeddings) from wrist PPG and accelerometer data that are useful for multiple downstream applications, we leveraged approximately 500,000 hours of consented watch sensor data collected across multiple IRB-approved studies conducted by Fitbit to train a general CNN encoder that produces embeddings from input PPG and accelerometer recordings in a self-supervised manner based on contrastive learning.

#### 5.1.1. Dataset

Summary demographic information of the dataset used to train the Waveform Foundation Model is provided in Table 1.

**Table 1. Participant Characteristics in Waveform Foundation Dataset.**

| Characteristic | Training (N = 1,614) | Tuning (N = 495) | Combined (N = 2,109) |
| :--- | :--- | :--- | :--- |
| **Age, years** | 40.5 ± 13.3 | 41.5 ± 14.0 | 40.7 ± 13.5 |
| *Missing* | 13 (0.8%) | 5 (1.0%) | 18 (0.9%) |
| **Female** | 572 (35.7%) | 169 (34.1%) | 741 (35.1%) |
| *Missing* | 13 (0.8%) | 5 (1.0%) | 18 (0.9%) |
| **BMI, kg/m²** | 26.5 ± 6.0 | 26.9 ± 5.6 | 26.6 ± 5.9 |
| *Missing* | 13 (0.8%) | 5 (1.0%) | 18 (0.9%) |
| **Monk Skin Tone (MST)** | | | |
| MST 1-4 | 644 (39.9%) | 201 (40.6%) | 845 (40.1%) |
| MST 5-7 | 319 (19.8%) | 112 (22.6%) | 431 (20.4%) |
| MST 8-10 | 21 (1.3%) | 20 (4.0%) | 41 (1.9%) |
| *Missing* | 630 (39.0%) | 162 (32.7%) | 792 (37.6%) |

#### 5.1.2. Model Architecture

The Waveform Foundation Model uses an EfficientNet B1 architecture with ~5.1 million parameters. The model inputs are 15-second segments of concomitant PPG and magnitude ACCEL waveforms stacked channel-wise. The model produces an embedding with 256 elements.

#### 5.1.3. Self-supervised Learning

We trained the Waveform Foundation Model using a self-supervised learning method based on participant contrastive learning (Diamant et al., PLoS Comput Biol, 2022, Abbaspourazad et al., ICLR, 2024). The only labels required to train participant contrastive learning are which PPG and ACCEL comes from which patient. Participant contrastive learning maps PPG and ACCEL segments acquired at different times from a given participant to the same region within a contrastive latent space. This approach relies on the shared underlying biology of different PPG and ACCEL measurements taken from the same participant to form positive pairs; negative pairs constitute PPG and ACCEL measurements obtained from different participants. The resulting embeddings are constructed in a manner to ensure that different PPG and ACCEL segments, which arise from the same participant, are more similar to one another relative to PPG and ACCEL-embeddings arising from different patients. This is an effective pre-training strategy for downstream tasks like hypertension detection because chronic high blood pressure is driven by structural traits—like arterial stiffness and vessel wall thickness—that remain relatively constant over time. By encouraging the model to identify what makes a specific participant's waveform unique, it implicitly learns to recognize these "stiffness signatures" in the waveforms, effectively teaching itself the markers of vascular health without needing explicit blood pressure labels.

### 5.2. Hypertension Classification Model

To develop the algorithm for the proposed Hypertension Notification feature, we used labeled data from 663 participants from 44 different states across the US in an IRB-approved study conducted in free-living conditions. Participants wore an FDA-cleared ABPM for 24 hours that served as the reference ground truth for hypertension status (defined as 24-hour mean SBP/DBP ≥ 130/80 mmHg) while also providing up to 14 days of raw wrist PPG and accelerometer data from a Google Pixel Watch. A summary of the demographics of the study population used for labeled algorithm development is shown in Table 2.

**Table 2. Participant Characteristics in Labeled Datasets.**

| Characteristic | Training (N = 663) | Test (N = 196) |
| :--- | :--- | :--- |
| **Age, years** | 42.3 ± 13.1 | 41.9 ± 16.9 |
| **Female** | 282 (42.5%) | 109 (55.6%) |
| **BMI, kg/m²** | 27.7 ± 6.4 | 29.5 ± 6.9 |
| **Race/Ethnicity** | | |
| Hispanic | 60 (9.0%) | 33 (16.8%) |
| Non-Hispanic White | 262 (39.5%) | 88 (44.9%) |
| Non-Hispanic Black | 141 (21.3%) | 67 (34.2%) |
| Non-Hispanic Asian | 172 (25.9%) | 6 (3.1%) |
| Other | 28 (4.2%) | 2 (1.0%) |
| **Monk Skin Tone (MST)** | | |
| MST 1-4 | 311 (46.9%) | 81 (41.3%) |
| MST 5-7 | 280 (42.2%) | 71 (36.2%) |
| MST 8-10 | 69 (10.4%) | 36 (18.4%) |
| *Missing* | 3 (0.5%) | 8 (4.1%) |
| **Systolic BP, mmHg (24h ABPM)** | 120.4 ± 12.6 | 125.4 ± 13.3 |
| **Diastolic BP, mmHg (24h ABPM)** | 72.9 ± 8.8 | 75.2 ± 9.7 |
| **Hypertension status (24h ABPM ≥130/80)** | 169 (25.5%) | 76 (38.8%) |

#### 5.2.1. Supervised Learning

We trained logistic regression models for hypertension classification using L2 regularization. The input is a 257-length user-level embedding created by concatenating the normalized user height with the mean-aggregated waveform embeddings of 256 elements. The labels are the presence of hypertension defined as mean 24-hour ABPM SBP/DBP ≥ 130/80 mmHg.

Blood pressure (BP) exhibits a circadian rhythm and typically dips in the nighttime during sleep. As such, mean BP computed using daytime measurements alone is generally higher than mean BP computed across all day including sleep. Since some users may not wear their wrist-worn device to sleep, we trained two logistic regression models to account for the different wear patterns and potential shifts in baselines. The first model, an All-day model, is trained using user-level embeddings aggregated across all 24 hours of the day. The second model, an Awake model, is meant for users who do not wear their wrist-worn device to sleep, and is trained using user-level embeddings aggregated across the hours of 9a to 9p only. Both models are trained to predict the same label - the presence of hypertension defined as mean 24-hour ABPM SBP/DBP ≥ 130/80 mmHg.

#### 5.2.2. Operating Point / Threshold Selection

We determined the operating point (threshold) to trigger a hypertension notification for the All-day and Daytime model individually by performing 10-fold stratified cross validation. Predictions across all folds were aggregated and the receiving operating characteristic (ROC) curve was computed. Finally, the threshold that maximized sensitivity at a specificity of 94.5% was identified.

#### 5.2.3. Algorithm Testing

To test our algorithms, we conducted a prospective, multi-center study across five sites in the US. The study design included two required study visits in addition to an at-home, free-living period over seven consecutive days.

Participants were provided with an ABPM, with the correct size cuff for each, and trained on proper use of each device. They were instructed to wear the ABPM for 24 hours, starting from the end of the first in-office visit. The ABPM was configured to measure BP every 20 min, from 7 AM to 11 PM, and hourly from 11 PM to 7 AM. In addition, participants were instructed to wear a Google Pixel watch throughout the entire duration of the at-home study, including during sleep.

None of the participants in the study were taking antihypertensive medications for a diagnosis of HTN. A summary of the demographics of the study population used for external testing is shown in Table 2. The study population included a broad representation across demographic factors including age, sex, race, and skin tone. The data from this 196-participant cohort was maintained as a strictly sequestered, independent data set that was completely independent of all training data.

The performance accuracy results are shown in Table 3. In this test cohort, 76 (38.8%) participants met the criteria for hypertension based on 24h ABPM measurements. Our hypertension classifier achieved a sensitivity and specificity of 52.6% (40.8, 64.2) and 92.5% (86.2, 96.5), respectively, for detecting hypertension. The positive predictive value (PPV) and negative predictive values (NPV) were 81.6% (68.0, 91.2) and 75.5% (67.7, 82.2), respectively.

In comparison, a model that does not take into account the user’s height achieved lower sensitivity and specificity for detecting hypertension.

**Table 3. Test Accuracy of the Hypertension Classifier to Identify Hypertension Based on 24-hour Ambulatory Blood Pressure Monitoring (≥130/80 mmHg)**

| Model | Sensitivity | Specificity | PPV | NPV | AUROC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Google Hypertension Notification** | 52.6 (40.8, 64.2) | 92.5 (86.2, 96.5) | 81.6 (68.0, 91.2) | 75.5 (67.7, 82.2) | 0.851 (0.794, 0.901) |
| **Without user height as input** | 43.4 (32.1, 55.3) | 93.3 (87.3, 97.1) | 80.5 (65.1, 91.2) | 72.3 (64.5, 79.1) | 0.825 (0.763, 0.883) |
