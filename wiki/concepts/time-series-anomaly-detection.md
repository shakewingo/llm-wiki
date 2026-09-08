---
id: time-series-anomaly-detection
title: Time-Series Anomaly Detection
type: concept
domains: [applied-ml, evaluation]
aliases: [KPI anomaly detection]
level: intermediate
relations:
  prerequisites: [classical-ml-methods]
  implemented_in: [spectral-residual-cnn, vae-lof-anomaly-detection]
sources: [yuque:127456364, yuque:145103815, yuque:145103757]
---

# Time-Series Anomaly Detection

Time-series anomaly detection identifies unusual points or segments relative to
temporal patterns, seasonality, trend, and local context.

Statistical residuals, density methods, isolation forests, reconstruction models,
and learned discriminators capture different anomaly definitions. Thresholding is
often the hardest operational choice: labels are scarce, rates drift, and alert
volume matters. Evaluation must state whether it uses point-level precision/recall,
segment adjustment, detection delay, or top-k ranking; tolerant metrics can make a
late or noisy detector appear better than it is.

## Sources

- [Stats / ML Algorithms](https://www.yuque.com/shakewin/woezs0/gkhfzndmawi1mp01)
- [SR-CNN](https://www.yuque.com/shakewin/woezs0/kogx0m65fye4qri6)
- [VAE + LOF](https://www.yuque.com/shakewin/woezs0/oucahnztr1pbh5qn)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[classical-ml-methods|Classical ML Methods]]
- Implemented in: [[spectral-residual-cnn|Spectral Residual CNN]], [[vae-lof-anomaly-detection|VAE–LOF Anomaly Detection]]

<!-- END GENERATED OBSIDIAN LINKS -->
