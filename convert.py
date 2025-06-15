import pandas as pd
import yaml

df3 = pd.read_csv('/Users/kaiagao/Documents/top_total_models_by_concept.csv')

# Convert to list of dictionaries
records3 = df3.to_dict(orient='records')

# Save to YAML
yaml_file_path3 = "_data/leaderboard_total.yml"
with open(yaml_file_path3, 'w') as file:
    yaml.dump(records3, file, sort_keys=False)