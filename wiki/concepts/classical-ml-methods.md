---
id: classical-ml-methods
title: Classical ML Methods
type: concept
domains: [foundations, applied-ml]
aliases: [classical machine learning]
level: foundational
relations:
  enables: [time-series-anomaly-detection]
sources: [yuque:127456364, yuque:222857934]
---

# Classical ML Methods

Classical ML remains useful when data is tabular, labels are scarce, latency is
tight, or interpretability matters. Decision trees split features to reduce impurity;
bagging reduces variance; boosting fits successive residual errors; regularized
linear models provide strong simple baselines.

Unsupervised methods expose structure without labels. PCA preserves directions of
maximum variance, ICA seeks statistically independent components, density clustering
finds irregular clusters, and isolation methods detect points separated quickly by
random partitions. Each method embeds assumptions about scale, distance, density,
or linearity, so preprocessing and evaluation must match the data-generating process.

## Sources

- [Stats / ML Algorithm Overview](https://www.yuque.com/shakewin/woezs0/gkhfzndmawi1mp01)
- [CS7641 ML](https://www.yuque.com/shakewin/fidaqi/evbvouf8opoc9aix)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Enables: [[time-series-anomaly-detection|Time-Series Anomaly Detection]]

<!-- END GENERATED OBSIDIAN LINKS -->
