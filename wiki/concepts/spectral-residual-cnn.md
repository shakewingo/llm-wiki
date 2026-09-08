---
id: spectral-residual-cnn
title: Spectral Residual CNN
type: concept
domains: [applied-ml, anomaly-detection]
aliases: [SR-CNN]
level: advanced
relations:
  prerequisites: [time-series-anomaly-detection]
  contrasts_with: [vae-lof-anomaly-detection]
sources: [yuque:145103815]
---

# Spectral Residual CNN

SR-CNN transforms a sliding time-series window into a spectral-residual saliency map
and uses a small one-dimensional CNN to classify anomalies instead of relying only
on a fixed saliency threshold.

The spectral residual removes the locally averaged log-amplitude spectrum, exposing
surprising frequency components before transforming back to time. Synthetic anomaly
injection supplies training labels when real labels are scarce. Boundary estimation
places the newest point away from the FFT window edge. Risks include unrealistic
synthetic anomalies and evaluation metrics that forgive excessive delay.

## Source

- [Time-Series Anomaly Detection at Microsoft](https://www.yuque.com/shakewin/woezs0/kogx0m65fye4qri6)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[time-series-anomaly-detection|Time-Series Anomaly Detection]]
- Contrasts with: [[vae-lof-anomaly-detection|VAE–LOF Anomaly Detection]]

<!-- END GENERATED OBSIDIAN LINKS -->
