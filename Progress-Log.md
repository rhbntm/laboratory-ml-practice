# Capstone-ML Progress Log

Keep entries short — a scannable trail, not a transcript. One entry per session.

Format:
```
## YYYY-MM-DD
- Covered: <concept(s) worked on>
- Got right: <what clicked>
- Confused about: <what didn't, or a mistake and why it happened>
- Open question: <anything to revisit next session>
```

---

## 2026-09-11
- Covered: ML fundamentals (dataset, features, target, labels, supervised classification), data leakage, feature selection (dropping identifiers like `equipment_id`), numerical vs categorical data, git repo initialization & ML environment setup (`numpy`, `pandas`, `scikit-learn`, `matplotlib`).
- Got right: Correctly identified that `equipment_id` is essential for the software/database layer but must be excluded from ML model features; recognized that `repair_cost_incurred` shouldn't be used to predict maintenance.
- Confused about: Initially swapped feature vs target roles (thought `maintenance_needed` was a feature during training and target in production); initial confusion on how data leakage manifests (timing of when information is recorded vs when prediction occurs).
- Open question: Why would generating synthetic data with strict deterministic rules (e.g., `if condition <= 3 then 1 else 0`) be bad for ML training/evaluation compared to probabilistic signal + noise?

