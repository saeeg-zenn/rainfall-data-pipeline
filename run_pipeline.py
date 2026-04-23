from modules.load_data import load_data
from modules.clean_data import clean_data
from modules.normalize_data import normalize_data
from modules.validate import validate_signals
from modules.trace import generate_trace_id, attach_trace
from modules.output import generate_output
from modules.logger import log

import json

# Step 1: Load
df = load_data("your_file_name.csv")
log("Data loaded")

# Step 2: Clean
df = clean_data(df)
log("Data cleaned")

# Step 3: Normalize → SIGNALS
signals = normalize_data(df)
log("Converted to signals")

# Step 4: Validate
signals = validate_signals(signals)
log("Signals validated")

# Step 5: Trace
trace_id = generate_trace_id()
signals = attach_trace(signals, trace_id)
log(f"Trace ID assigned: {trace_id}")

# Step 6: Generate structured output
output = generate_output(signals)
log("Output generated")

# Step 7: Save output
with open('output/final_output.json', 'w') as f:
    json.dump(output, f, indent=4)

print("Final Output:")
print(output)