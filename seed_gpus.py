from app import create_app
from extensions import db
from models import GPU
from utilss import amazon_link

app = create_app()

with app.app_context():

    gpus = [

        # Entry Level
        GPU(name="Zebronics GT610 DDR3 2GB", vram=2, benchmark_score=800, wattage=30, price=3434,
            amazon_link=amazon_link("Zebronics GT610 DDR3 2GB graphics card")),

        GPU(name="Asus GT 730 2GB GDDR5", vram=2, benchmark_score=1200, wattage=38, price=3950,
            amazon_link=amazon_link("Asus GT 730 2GB GDDR5 graphics card")),

        GPU(name="Zebronics GT740 4GB DDR3", vram=4, benchmark_score=1500, wattage=64, price=3599,
            amazon_link=amazon_link("Zebronics GT740 4GB DDR3 graphics card")),

        GPU(name="Zebronics GT730 4GB DDR3", vram=4, benchmark_score=1100, wattage=38, price=4740,
            amazon_link=amazon_link("Zebronics GT730 4GB DDR3 graphics card")),

        GPU(name="PowerColor RX 550 2GB", vram=2, benchmark_score=3000, wattage=50, price=4649,
            amazon_link=amazon_link("PowerColor RX 550 2GB graphics card")),

        GPU(name="Colorful GT1030 4GB", vram=4, benchmark_score=3500, wattage=30, price=7825,
            amazon_link=amazon_link("Colorful GT1030 4GB graphics card")),

        # Budget Gaming
        GPU(name="ELBME GTX1050Ti 4GB", vram=4, benchmark_score=6000, wattage=75, price=8099,
            amazon_link=amazon_link("GTX 1050 Ti 4GB graphics card")),

        GPU(name="ASRock RX550 Phantom Gaming", vram=4, benchmark_score=3200, wattage=50, price=8880,
            amazon_link=amazon_link("ASRock RX550 Phantom Gaming graphics card")),

        GPU(name="INNO3D RTX 3050 6GB", vram=6, benchmark_score=12000, wattage=130, price=19990,
            amazon_link=amazon_link("INNO3D RTX 3050 6GB graphics card")),

        GPU(name="ASUS Dual RTX 3050 OC", vram=6, benchmark_score=11500, wattage=130, price=16099,
            amazon_link=amazon_link("ASUS Dual RTX 3050 OC graphics card")),

        GPU(name="Gigabyte RTX 5050 8GB", vram=8, benchmark_score=14000, wattage=150, price=15000,
            amazon_link=amazon_link("Gigabyte RTX 5050 8GB graphics card")),

        # Mid Range
        GPU(name="ZOTAC GTX 1660 SUPER 6GB", vram=6, benchmark_score=12500, wattage=125, price=19470,
            amazon_link=amazon_link("ZOTAC GTX 1660 SUPER 6GB graphics card")),

        GPU(name="Gigabyte RX 6600 8GB", vram=8, benchmark_score=15000, wattage=132, price=15930,
            amazon_link=amazon_link("Gigabyte RX 6600 8GB graphics card")),

        GPU(name="RTX 2060 6GB", vram=6, benchmark_score=13000, wattage=160, price=32990,
            amazon_link=amazon_link("RTX 2060 6GB graphics card")),

        GPU(name="RTX 3050 Ventus 6GB", vram=6, benchmark_score=11800, wattage=130, price=21495,
            amazon_link=amazon_link("RTX 3050 Ventus 6GB graphics card")),

        # Upper Mid Range
        GPU(name="RTX 4060 8GB", vram=8, benchmark_score=20000, wattage=160, price=31500,
            amazon_link=amazon_link("RTX 4060 8GB graphics card")),

        GPU(name="RX 9060 XT 8GB", vram=8, benchmark_score=21000, wattage=170, price=24379,
            amazon_link=amazon_link("RX 9060 XT 8GB graphics card")),

        GPU(name="RTX 3070 Ti 8GB", vram=8, benchmark_score=24000, wattage=290, price=24999,
            amazon_link=amazon_link("RTX 3070 Ti 8GB graphics card")),

        GPU(name="RTX 2080 SUPER 8GB", vram=8, benchmark_score=22000, wattage=250, price=19999,
            amazon_link=amazon_link("RTX 2080 SUPER 8GB graphics card")),

        # High End
        GPU(name="RTX 5060 Ti 16GB", vram=16, benchmark_score=28000, wattage=220, price=51389,
            amazon_link=amazon_link("RTX 5060 Ti 16GB graphics card")),

        GPU(name="RTX 5060 8GB", vram=8, benchmark_score=25000, wattage=200, price=40999,
            amazon_link=amazon_link("RTX 5060 8GB graphics card")),

        # Workstation / AI
        GPU(name="Sapphire Radeon AI PRO R9700", vram=16, benchmark_score=40000, wattage=300, price=159500,
            amazon_link=amazon_link("Sapphire Radeon AI PRO R9700 graphics card")),
    ]

    for gpu in gpus:
        db.session.add(gpu)

    db.session.commit()

    print("GPU data inserted successfully.")