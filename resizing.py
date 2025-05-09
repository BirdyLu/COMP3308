import csv
import random

INPUT_FILE    = "occupancy.csv"
OUTPUT_FILE   = "occupancy_pruned.csv"
DROP_NO       = 1146
DROP_YES      = 112
RANDOM_SEED   = 42  # for reproducibility

def main():
    random.seed(RANDOM_SEED)

    # 1) Read in everything, separate header and body
    with open(INPUT_FILE, newline="") as f:
        reader = csv.reader(f)
        rows   = list(reader)

    # 2) Partition into yes/no
    no_rows  = [r for r in rows if r[-1].strip().lower() == "no"]
    yes_rows = [r for r in rows if r[-1].strip().lower() == "yes"]

    # 3) Compute how many to keep
    keep_no  = len(no_rows)  - DROP_NO
    keep_yes = len(yes_rows) - DROP_YES

    if keep_no < 0 or keep_yes < 0:
        raise ValueError(
            f"Cannot drop {DROP_NO} no-rows / {DROP_YES} yes-rows: "
            f"only {len(no_rows)} no and {len(yes_rows)} yes available."
        )

    # 4) Randomly sample the rows to keep
    kept_no  = random.sample(no_rows,  keep_no)
    kept_yes = random.sample(yes_rows, keep_yes)

    # 5) Combine, shuffle, and write out
    output_rows = kept_no + kept_yes
    random.shuffle(output_rows)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)

    print(f"Kept {keep_no} no-rows and {keep_yes} yes-rows → wrote {len(output_rows)} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
