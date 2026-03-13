from app import create_app
from extensions import db
from models import PSU
from utilss import amazon_link

app = create_app()

with app.app_context():

    psus = [

        # 450W – 550W (Budget)
        PSU("Ant Esports VS450L",450,"Bronze",2200,amazon_link("Ant Esports VS450L power supply")),
        PSU("Circle Desire DXP 450W",450,"Bronze",2100,amazon_link("Circle Desire DXP 450W PSU")),
        PSU("Corsair CV450",450,"Bronze",3400,amazon_link("Corsair CV450 power supply")),
        PSU("Cooler Master MWE 450 V2",450,"Bronze",3800,amazon_link("Cooler Master MWE 450 V2 PSU")),
        PSU("DeepCool PK550D",550,"Bronze",4200,amazon_link("DeepCool PK550D PSU")),
        PSU("MSI MAG A550BN",550,"Bronze",4500,amazon_link("MSI MAG A550BN PSU")),

        # 550W – 650W (Mid Range)
        PSU("Corsair CV550",550,"Bronze",4200,amazon_link("Corsair CV550 PSU")),
        PSU("Corsair CX650",650,"Bronze",6500,amazon_link("Corsair CX650 PSU")),
        PSU("Cooler Master MWE 650 Bronze V2",650,"Bronze",6800,amazon_link("Cooler Master MWE 650 Bronze V2 PSU")),
        PSU("DeepCool PM650D",650,"Gold",7500,amazon_link("DeepCool PM650D PSU")),
        PSU("MSI MAG A650BN",650,"Bronze",5800,amazon_link("MSI MAG A650BN PSU")),
        PSU("Gigabyte P650B",650,"Bronze",5500,amazon_link("Gigabyte P650B PSU")),

        # 650W – 750W
        PSU("Corsair RM650 Gold",650,"Gold",9500,amazon_link("Corsair RM650 Gold PSU")),
        PSU("Corsair RM750e",750,"Gold",10500,amazon_link("Corsair RM750e PSU")),
        PSU("MSI MPG A750GF",750,"Gold",9800,amazon_link("MSI MPG A750GF PSU")),
        PSU("DeepCool DQ750-M-V2L",750,"Gold",8800,amazon_link("DeepCool DQ750-M-V2L PSU")),
        PSU("Cooler Master MWE 750 Gold V2",750,"Gold",9200,amazon_link("Cooler Master MWE 750 Gold V2 PSU")),
        PSU("Gigabyte UD750GM",750,"Gold",8500,amazon_link("Gigabyte UD750GM PSU")),

        # 750W – 850W
        PSU("Corsair RM850",850,"Gold",12500,amazon_link("Corsair RM850 PSU")),
        PSU("Corsair RM850x",850,"Gold",14000,amazon_link("Corsair RM850x PSU")),
        PSU("MSI MPG A850GF",850,"Gold",12000,amazon_link("MSI MPG A850GF PSU")),
        PSU("Cooler Master MWE 850 Gold V2",850,"Gold",11500,amazon_link("Cooler Master MWE 850 Gold V2 PSU")),
        PSU("DeepCool PX850G ATX 3.0",850,"Gold",13000,amazon_link("DeepCool PX850G ATX 3.0 PSU")),
        PSU("Gigabyte UD850GM PG5 ATX 3.0",850,"Gold",11800,amazon_link("Gigabyte UD850GM PG5 PSU")),

        # 1000W+
        PSU("Corsair RM1000x",1000,"Gold",17000,amazon_link("Corsair RM1000x PSU")),
        PSU("Corsair HX1000",1000,"Platinum",20000,amazon_link("Corsair HX1000 PSU")),
        PSU("MSI MPG A1000G",1000,"Gold",18500,amazon_link("MSI MPG A1000G PSU")),
        PSU("DeepCool PX1000G ATX 3.0",1000,"Gold",19000,amazon_link("DeepCool PX1000G ATX 3.0 PSU")),
        PSU("Cooler Master MWE 1050 Gold V2",1050,"Gold",16500,amazon_link("Cooler Master MWE 1050 Gold V2 PSU")),
        PSU("ASUS ROG Thor 1000W Platinum",1000,"Platinum",28000,amazon_link("ASUS ROG Thor 1000W Platinum PSU")),

        # Premium
        PSU("Corsair HX1200 Platinum",1200,"Platinum",25000,amazon_link("Corsair HX1200 Platinum PSU")),
        PSU("ASUS ROG Thor 1200W Platinum",1200,"Platinum",35000,amazon_link("ASUS ROG Thor 1200W Platinum PSU")),
        PSU("MSI MEG Ai1300P",1300,"Platinum",38000,amazon_link("MSI MEG Ai1300P PSU")),
        PSU("Seasonic PRIME TX-1000",1000,"Platinum",30000,amazon_link("Seasonic PRIME TX-1000 PSU")),
    ]

    for psu in psus:
        db.session.add(psu)

    db.session.commit()

    print("PSU data inserted successfully.")