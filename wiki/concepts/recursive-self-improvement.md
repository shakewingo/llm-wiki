---
id: recursive-self-improvement
title: Recursive Self-Improvement
type: concept
domains: [post-training, agent-architecture]
aliases: [RSI]
level: advanced
relations:
  prerequisites: [supervised-fine-tuning, reinforcement-learning, agent-loop]
  contrasts_with: [direct-preference-optimization, group-relative-policy-optimization, rlhf]
sources: [yuque:288964571]
---

# Recursive Self-Improvement

RSI 的严格含义是：系统改进之后，"改进自己的能力"本身也变强了。分数上涨不等于 RSI。

核心区分：改进对象是谁？改进流程本身是否也在变强？

## 三类方法

| 类别 | 代表工作 | 改进对象 | 是否 RSI |
|------|---------|---------|---------|
| 模型自训练循环 | STaR, ReST/ReST-EM, Self-Rewarding LM, SPIN, R-Zero | 模型权重 M_k → M_{k+1} | 弱形式：数据生成者在变强，但改进流程是人写死的 |
| Agent/脚手架自修改 | STOP, Gödel Agent, Darwin Gödel Machine, ADAS | Agent 自己的代码或 prompt，包括改进器本身 | 最接近字面 RSI |
| 自动化科研 | AI Scientist, AlphaEvolve, Karpathy autoresearch | 另一个对象（算法、训练代码） | 通常不算 |

## 关键区分：autoresearch ≠ RSI

Karpathy 的 autoresearch 循环：固定强模型 agent 按 `program.md` 修改小 LLM 训练脚本 → 指标变好保留/变差回滚 → 整晚循环。被改进的是另一个小模型，做研究的 agent 本身没有变强。本质是"自动化研究 + 爬山式搜索"。

## 核心论文

- **STaR** (2022): 生成→验证→训练→新模型再生成，自举推理能力
- **GEPA** (2026): 遗传-Pareto prompt 进化，TaskLM + ReflectionLM + Evaluator 闭环
- **ModularRSI** (2026): 模块化 RSI，关注模块边界和失败对照
- **RRSI** (2026): 鲁棒 RSI，关注过拟合和候选选择
- **Dream-RSI** (2026): Google 的 RSI 演示系统，含完整实验循环
- **STOP** (Self-Taught Optimizer): 让改进器改进自己，最接近字面 RSI

## 工程基础

有效的 RSI 实验需要：
- 可替换的运行机制（agent loop、上下文预算、compaction）
- 可追溯的模型输入（input_messages、工具定义和响应记录）
- 独立验证器 + dev/test split + 多 seed 汇总
- 冻结源码/prompt/配置/任务协议以隔离变量

## Sources

- [RSI](https://www.yuque.com/shakewin/xhs6fk/owmvngalyva33nlr)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[supervised-fine-tuning|Supervised Fine-Tuning]], [[reinforcement-learning|Reinforcement Learning]], [[agent-loop|Agent Loop]]
- Contrasts with: [[direct-preference-optimization|Direct Preference Optimization]], [[group-relative-policy-optimization|Group Relative Policy Optimization]], [[rlhf|Reinforcement Learning from Human Feedback]]

<!-- END GENERATED OBSIDIAN LINKS -->
