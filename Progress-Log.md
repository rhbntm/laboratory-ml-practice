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

## 2026-09-12
- Covered: Deterministic vs. probabilistic data generation (why ML isn't needed if a simple `if/else` achieves 100%), signal + Gaussian noise, class imbalance rationale (~32% positive to reflect real lab equipment stability), created and ran `generate_data.py` producing `equipment_data.csv` (400 records), learned vs hardcoded weights (type bias is learned by the model, not a pre-known input), client data feasibility criteria.
- Got right: Intuition on feature correlations (lower condition and higher days-since-maintenance increase risk); understood that real breakdowns are probabilistic; realized that `equipment_type` reflects baseline category fragility while `equipment_id` carries zero predictive signal; recognized that labeled maintenance logs are the true project go/no-go bottleneck.
- Confused about: Thought learning a deterministic rule was classic "overfitting" rather than an architectural misuse of ML; initial worry that not knowing true equipment type bias values would block modeling (clarified: models learn these weights from labeled data).
- Open question: Does the client actually have historical labeled maintenance records (or do we need proxy labels / manual labeling / reframing as decision support)? Next technical step: Stage 3 (Exploratory Data Analysis on `equipment_data.csv`).

