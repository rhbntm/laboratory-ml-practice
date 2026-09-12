import numpy as np
import pandas as pd

# Set random seed so results are reproducible
np.random.seed(42)
n_samples = 400

# 1. Generate Features
equipment_ids = [f"EQ-{i:03d}" for i in range(1, n_samples + 1)]
equipment_types = np.random.choice(
    ["Microscope", "Centrifuge", "Spectrophotometer", "Autoclave"], 
    size=n_samples, 
    p=[0.35, 0.25, 0.20, 0.20]
)

# Realistic distributions
age_years = np.random.uniform(0.5, 10.0, size=n_samples).round(1)
usage_count = (age_years * np.random.uniform(30, 80, size=n_samples)).astype(int)
days_since_maintenance = np.random.randint(10, 365, size=n_samples)

# Condition score: starts higher for newer/low-use items, but with variance
raw_condition = 10 - (age_years * 0.5) - (usage_count / 150) + np.random.normal(0, 1.2, size=n_samples)
condition_score = np.clip(np.round(raw_condition), 1, 10).astype(int)

# 2. Fragility bias by equipment type (Spectrophotometers & Microscopes are more fragile)
type_risk_bias = {
    "Microscope": 0.3,
    "Spectrophotometer": 0.5,
    "Centrifuge": -0.2,
    "Autoclave": -0.1
}
type_bias_values = np.array([type_risk_bias[t] for t in equipment_types])

# 3. Composite Risk Score (Signal + Noise)
# Positive signs = increases risk; Negative signs = decreases risk
risk_score = (
    0.25 * (age_years / 10.0) +
    0.30 * (usage_count / usage_count.max()) +
    0.25 * (days_since_maintenance / 365.0) -
    0.40 * (condition_score / 10.0) +
    type_bias_values
)

# Add random real-world noise
noise = np.random.normal(0, 0.20, size=n_samples)
final_score = risk_score + noise

# 4. Target assignment: top ~30-35% at risk need maintenance (class imbalance)
threshold = np.percentile(final_score, 68)
maintenance_needed = (final_score >= threshold).astype(int)

# 5. Build and Save DataFrame
df = pd.DataFrame({
    "equipment_id": equipment_ids,
    "equipment_type": equipment_types,
    "age_years": age_years,
    "usage_count": usage_count,
    "days_since_maintenance": days_since_maintenance,
    "condition_score": condition_score,
    "maintenance_needed": maintenance_needed
})

df.to_csv("equipment_data.csv", index=False)
print(f"Generated {n_samples} records. Maintenance needed count:")
print(df["maintenance_needed"].value_counts(normalize=True))
