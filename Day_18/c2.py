def normal_way():
    results = []
    print("  [Normal Function] Starting to build the entire list...")
    for i in range(3):
        print(f"  [Normal Function] Cooking item {i}...")
        results.append(i)
    print("  [Normal Function] Finished! Handing over the heavy list.")
    return results

print("--- STARTING NORMAL ---")
for item in normal_way():
    print(f"Received: {item}")