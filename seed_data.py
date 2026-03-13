from app import app
from extensions import db
from models import CPU, GPU, RAM, SSD, Motherboard, PSU, Laptop


with app.app_context():

    # Clear existing data (optional)
    db.drop_all()
    db.create_all()

    # ---------------- CPUs ----------------
    cpu1 = CPU(name="Ryzen 5 5600X", cores=6, threads=12, benchmark_score=18000, price=15000, socket="AM4")
    cpu2 = CPU(name="Intel i5 12400F", cores=6, threads=12, benchmark_score=19000, price=16000, socket="LGA1700")
    cpu3 = CPU(name="Ryzen 7 5800X", cores=8, threads=16, benchmark_score=22000, price=22000, socket="AM4")

    # ---------------- GPUs ----------------
    gpu1 = GPU(name="RTX 3060", vram=12, benchmark_score=17000, price=25000, wattage=550)
    gpu2 = GPU(name="RTX 4060", vram=8, benchmark_score=20000, price=30000, wattage=600)
    gpu3 = GPU(name="RX 6600", vram=8, benchmark_score=16000, price=22000, wattage=500)

    # ---------------- RAM ----------------
    ram1 = RAM(size=16, type="DDR4", price=4000)
    ram2 = RAM(size=32, type="DDR4", price=8000)

    # ---------------- SSD ----------------
    ssd1 = SSD(capacity=512, speed_score=3000, price=3500)
    ssd2 = SSD(capacity=1000, speed_score=3500, price=6000)

    # ---------------- Motherboard ----------------
    mb1 = Motherboard(name="B550 Board", socket="AM4", chipset="B550", price=9000)
    mb2 = Motherboard(name="B660 Board", socket="LGA1700", chipset="B660", price=10000)

    # ---------------- PSU ----------------
    psu1 = PSU(wattage=550, efficiency="80+ Bronze", price=4000)
    psu2 = PSU(wattage=650, efficiency="80+ Gold", price=6000)

    # ---------------- Laptops ----------------
    laptop1 = Laptop(name="Acer Nitro 5", cpu_score=18000, gpu_score=17000, ram=16, storage_score=3000, price=75000)
    laptop2 = Laptop(name="ASUS TUF F15", cpu_score=20000, gpu_score=20000, ram=16, storage_score=3500, price=85000)
    laptop3 = Laptop(name="HP Victus", cpu_score=17000, gpu_score=16000, ram=8, storage_score=2500, price=65000)

    db.session.add_all([
        cpu1, cpu2, cpu3,
        gpu1, gpu2, gpu3,
        ram1, ram2,
        ssd1, ssd2,
        mb1, mb2,
        psu1, psu2,
        laptop1, laptop2, laptop3
    ])

    db.session.commit()

    print("Sample data inserted successfully!")
