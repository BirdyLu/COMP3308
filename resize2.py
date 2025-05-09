import csv
import random

def sample_rows(input_path, output_path, sample_size=768, seed=None):
    """
    Reads every non-empty row from input_path, randomly samples `sample_size` of them
    (without regard to their labels), and writes the sample to output_path.
    """
    # 1) load all rows
    with open(input_path, newline='') as src:
        reader = csv.reader(src)
        all_rows = [row for row in reader if row]  # skip blank lines

    # 2) optional: fix the RNG for reproducibility
    if seed is not None:
        random.seed(seed)

    # 3) draw a sample without replacement
    sample = random.sample(all_rows, sample_size)

    # 4) write them back out
    with open(output_path, 'w', newline='') as dst:
        writer = csv.writer(dst)
        writer.writerows(sample)

if __name__ == "__main__":
    sample_rows(
        input_path  ="occupancy.csv",
        output_path ="occupancy_sampled.csv",
        sample_size =768,
        seed        =42      # or None for non-deterministic draws
    )
