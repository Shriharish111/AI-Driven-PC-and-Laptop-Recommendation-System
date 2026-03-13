from app import create_app
from extensions import db
from models import RAM
from utilss import amazon_link

app = create_app()

with app.app_context():

    ram_modules = [

        # DDR4 Desktop (UDIMM)
        RAM("PreSolve 4GB DDR4 2666MHz",4,"DDR4",2666,"UDIMM",1999,amazon_link("PreSolve 4GB DDR4 2666MHz RAM")),
        RAM("Corsair Vengeance LPX 8GB DDR4 3200MHz",8,"DDR4",3200,"UDIMM",6090,amazon_link("Corsair Vengeance LPX 8GB DDR4 3200MHz")),
        RAM("EVM 8GB DDR4 3200MHz",8,"DDR4",3200,"UDIMM",4500,amazon_link("EVM 8GB DDR4 3200MHz RAM")),

        # DDR5 Desktop (UDIMM)
        RAM("EVM 8GB DDR5 4800MHz",8,"DDR5",4800,"UDIMM",8235,amazon_link("EVM 8GB DDR5 4800MHz RAM")),
        RAM("EVM 8GB DDR5 5600MHz",8,"DDR5",5600,"UDIMM",8525,amazon_link("EVM 8GB DDR5 5600MHz RAM")),
        RAM("EVM 16GB DDR5 4800MHz",16,"DDR5",4800,"UDIMM",14420,amazon_link("EVM 16GB DDR5 4800MHz RAM")),
        RAM("UDIMM 16GB DDR5 5600MHz",16,"DDR5",5600,"UDIMM",16000,amazon_link("16GB DDR5 5600MHz UDIMM RAM")),
        RAM("Kingston Fury Beast 16GB DDR5 6000MHz",16,"DDR5",6000,"UDIMM",22000,amazon_link("Kingston Fury Beast 16GB DDR5 6000MHz")),
        RAM("Corsair Vengeance 16GB DDR5 6000MHz",16,"DDR5",6000,"UDIMM",17999,amazon_link("Corsair Vengeance 16GB DDR5 6000MHz")),
        RAM("G.Skill Ripjaws S5 16GB DDR5 5200MHz",16,"DDR5",5200,"UDIMM",17000,amazon_link("G.Skill Ripjaws S5 16GB DDR5 5200MHz")),
        RAM("Adata XPG Lancer Blade 16GB DDR5 6000MHz",16,"DDR5",6000,"UDIMM",20000,amazon_link("Adata XPG Lancer Blade 16GB DDR5 6000MHz")),

        # 32GB Kits
        RAM("Patriot Viper Elite 5 RGB 32GB DDR5",32,"DDR5",6000,"UDIMM",19490,amazon_link("Patriot Viper Elite 5 RGB 32GB DDR5")),
        RAM("Corsair Vengeance RGB 32GB DDR5",32,"DDR5",6000,"UDIMM",19900,amazon_link("Corsair Vengeance RGB 32GB DDR5")),
        RAM("TeamGroup Delta RGB 32GB DDR5 5200MHz",32,"DDR5",5200,"UDIMM",30100,amazon_link("TeamGroup Delta RGB 32GB DDR5 5200MHz")),
        RAM("Acer Predator Vesta II 32GB DDR5 6000MHz",32,"DDR5",6000,"UDIMM",34999,amazon_link("Acer Predator Vesta II 32GB DDR5 6000MHz")),
        RAM("EVM 32GB DDR5 Desktop RAM",32,"DDR5",5200,"UDIMM",36829,amazon_link("EVM 32GB DDR5 Desktop RAM")),

        # High Capacity
        RAM("Crucial Pro 64GB DDR5",64,"DDR5",5600,"UDIMM",48500,amazon_link("Crucial Pro 64GB DDR5 RAM")),
        RAM("G.Skill Trident Z5 Neo 128GB DDR5 6000MHz",128,"DDR5",6000,"UDIMM",197500,amazon_link("G.Skill Trident Z5 Neo 128GB DDR5 6000MHz")),

        # Laptop RAM
        RAM("8GB DDR5 4800MHz Laptop RAM",8,"DDR5",4800,"SODIMM",4999,amazon_link("8GB DDR5 4800MHz laptop RAM")),
    ]

    for ram in ram_modules:
        db.session.add(ram)

    db.session.commit()

    print("RAM data inserted successfully.")