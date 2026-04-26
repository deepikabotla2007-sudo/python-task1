import random
import copy
import math
import numpy as np
import pandas as pd

def generate_students(n):
    data = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data, roll_number):
    mod_val = roll_number % 3
    if mod_val == 0:
        mod_val = 1

    for i in range(len(data)):
        if i % mod_val == 0:
            data[i]["marks"] += int(math.sqrt(data[i]["marks"]))
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 3
    return data

def manual_mean(data):
    total = 0
    for d in data:
        total += d["marks"]
    return total / len(data)

def analyze(original, modified):
    orig_marks = [d["marks"] for d in original]
    mod_marks = [d["marks"] for d in modified]

    mean_orig = np.mean(orig_marks)
    mean_mod = np.mean(mod_marks)
    std_dev = np.std(mod_marks)

    drift = abs(mean_orig - mean_mod)

    return mean_mod, drift, std_dev

def classify(drift, threshold, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"


roll_number = int(input("Enter roll number: "))
n = random.randint(10, 15)

original = generate_students(n)

shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

shallow_mod = mutate_data(shallow_copy, roll_number)
deep_mod = mutate_data(deep_copy, roll_number)

df_original = pd.DataFrame(original)
df_shallow = pd.DataFrame(shallow_mod)
df_deep = pd.DataFrame(deep_mod)

mean, drift, std_dev = analyze(original, deep_mod)

manual_avg = manual_mean(original)

threshold = 5

result = classify(drift, threshold, original, shallow_mod)


print("\n--- ORIGINAL DATA ---")
print(df_original)

print("\n--- SHALLOW COPY ---")
print(df_shallow)

print("\n--- DEEP COPY ---")
print(df_deep)

print("\nManual Mean:", manual_avg)
print("Drift:", drift)
print("Std Dev:", std_dev)

print("\nTuple Output:", (mean, drift, std_dev))
print("Final Classification:", result)