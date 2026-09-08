---
id: vae-lof-anomaly-detection
title: VAE–LOF Anomaly Detection
type: concept
domains: [applied-ml, anomaly-detection]
aliases: [LOF-VAE]
level: advanced
relations:
  prerequisites: [time-series-anomaly-detection, variational-autoencoder]
  contrasts_with: [spectral-residual-cnn]
sources: [yuque:145103757]
---

# VAE–LOF Anomaly Detection

This hybrid uses Local Outlier Factor to remove obvious anomalies or create weak
labels before fitting a VAE-based KPI detector.

LOF compares a point's local density with its neighbors, while the VAE learns a
probabilistic normal representation and reconstruction objective. The combination
can retain more normal training data than aggressive filtering, but neighborhood
size, top-k selection, and loss weighting are dataset-sensitive. Evidence from a
small KPI collection does not establish generality, so cross-service validation and
ablation are essential.

## Source

- [VAE + LOF Anomaly Detection](https://www.yuque.com/shakewin/woezs0/oucahnztr1pbh5qn)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[time-series-anomaly-detection|Time-Series Anomaly Detection]], [[variational-autoencoder|Variational Autoencoder]]
- Contrasts with: [[spectral-residual-cnn|Spectral Residual CNN]]

<!-- END GENERATED OBSIDIAN LINKS -->
