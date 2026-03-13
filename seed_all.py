import subprocess
import sys

seed_files = [
    "seed_cpus.py",
    "seed_gpus.py",
    "seed_ram.py",
    "seed_ssds.py",
    "seed_motherboards.py",
    "seed_psu.py",
    "seed_laptops.py"
]

for seed in seed_files:
    print(f"Running {seed}...")
    result = subprocess.run([sys.executable, seed])

    if result.returncode != 0:
        print(f"Error while running {seed}")
        break

print("Seeding complete.")