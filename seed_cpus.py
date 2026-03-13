from app import create_app
from extensions import db
from models import CPU
from utilss import amazon_link

app = create_app()

with app.app_context():

    cpus = [

        # INTEL 10TH GEN
        CPU("Intel Core i3-10100",4,8,8000,"LGA1200",8000,amazon_link("Intel Core i3-10100")),
        CPU("Intel Core i5-10400",6,12,12000,"LGA1200",11000,amazon_link("Intel Core i5-10400")),
        CPU("Intel Core i5-10600K",6,12,15000,"LGA1200",16000,amazon_link("Intel Core i5-10600K")),
        CPU("Intel Core i7-10700",8,16,17000,"LGA1200",20000,amazon_link("Intel Core i7-10700")),
        CPU("Intel Core i9-10900K",10,20,20000,"LGA1200",32000,amazon_link("Intel Core i9-10900K")),

        # INTEL 11TH GEN
        CPU("Intel Core i5-11400",6,12,13500,"LGA1200",13000,amazon_link("Intel Core i5-11400")),
        CPU("Intel Core i5-11600K",6,12,16500,"LGA1200",18000,amazon_link("Intel Core i5-11600K")),
        CPU("Intel Core i7-11700K",8,16,19000,"LGA1200",24000,amazon_link("Intel Core i7-11700K")),
        CPU("Intel Core i9-11900K",8,16,21000,"LGA1200",35000,amazon_link("Intel Core i9-11900K")),

        # INTEL 12TH GEN
        CPU("Intel Core i3-12100",4,8,14000,"LGA1700",9000,amazon_link("Intel Core i3-12100")),
        CPU("Intel Core i5-12400",6,12,18000,"LGA1700",15000,amazon_link("Intel Core i5-12400")),
        CPU("Intel Core i5-12600K",10,16,22000,"LGA1700",23000,amazon_link("Intel Core i5-12600K")),
        CPU("Intel Core i7-12700K",12,20,26000,"LGA1700",32000,amazon_link("Intel Core i7-12700K")),
        CPU("Intel Core i9-12900K",16,24,30000,"LGA1700",45000,amazon_link("Intel Core i9-12900K")),

        # INTEL 13TH GEN
        CPU("Intel Core i5-13400",10,16,21000,"LGA1700",18000,amazon_link("Intel Core i5-13400")),
        CPU("Intel Core i5-13600K",14,20,28000,"LGA1700",28000,amazon_link("Intel Core i5-13600K")),
        CPU("Intel Core i7-13700K",16,24,32000,"LGA1700",38000,amazon_link("Intel Core i7-13700K")),
        CPU("Intel Core i9-13900K",24,32,36000,"LGA1700",52000,amazon_link("Intel Core i9-13900K")),

        # INTEL 14TH GEN
        CPU("Intel Core i5-14400",10,16,22000,"LGA1700",20000,amazon_link("Intel Core i5-14400")),
        CPU("Intel Core i5-14600K",14,20,30000,"LGA1700",30000,amazon_link("Intel Core i5-14600K")),
        CPU("Intel Core i7-14700K",20,28,35000,"LGA1700",42000,amazon_link("Intel Core i7-14700K")),
        CPU("Intel Core i9-14900K",24,32,39000,"LGA1700",58000,amazon_link("Intel Core i9-14900K")),

        # INTEL CORE ULTRA
        CPU("Intel Core Ultra 5 245K",14,20,32000,"LGA1851",32000,amazon_link("Intel Core Ultra 5 245K")),
        CPU("Intel Core Ultra 7 265K",20,28,38000,"LGA1851",45000,amazon_link("Intel Core Ultra 7 265K")),
        CPU("Intel Core Ultra 9 285K",24,32,45000,"LGA1851",65000,amazon_link("Intel Core Ultra 9 285K")),

        # AMD RYZEN 3000
        CPU("Ryzen 3 3100",4,8,9000,"AM4",8500,amazon_link("Ryzen 3 3100")),
        CPU("Ryzen 5 3600",6,12,14000,"AM4",12000,amazon_link("Ryzen 5 3600")),
        CPU("Ryzen 7 3700X",8,16,18000,"AM4",20000,amazon_link("Ryzen 7 3700X")),
        CPU("Ryzen 9 3900X",12,24,24000,"AM4",35000,amazon_link("Ryzen 9 3900X")),

        # AMD RYZEN 5000
        CPU("Ryzen 5 5600",6,12,19000,"AM4",14000,amazon_link("Ryzen 5 5600")),
        CPU("Ryzen 5 5600X",6,12,20000,"AM4",16000,amazon_link("Ryzen 5 5600X")),
        CPU("Ryzen 7 5700X",8,16,23000,"AM4",22000,amazon_link("Ryzen 7 5700X")),
        CPU("Ryzen 7 5800X",8,16,25000,"AM4",25000,amazon_link("Ryzen 7 5800X")),
        CPU("Ryzen 9 5900X",12,24,31000,"AM4",34000,amazon_link("Ryzen 9 5900X")),
        CPU("Ryzen 9 5950X",16,32,35000,"AM4",45000,amazon_link("Ryzen 9 5950X")),

        # AMD RYZEN 7000 / 8000
        CPU("Ryzen 5 7600",6,12,23000,"AM5",19000,amazon_link("Ryzen 5 7600")),
        CPU("Ryzen 5 7600X",6,12,24000,"AM5",22000,amazon_link("Ryzen 5 7600X")),
        CPU("Ryzen 7 7700X",8,16,28000,"AM5",32000,amazon_link("Ryzen 7 7700X")),
        CPU("Ryzen 7 7800X3D",8,16,32000,"AM5",38000,amazon_link("Ryzen 7 7800X3D")),
        CPU("Ryzen 9 7900X",12,24,34000,"AM5",42000,amazon_link("Ryzen 9 7900X")),
        CPU("Ryzen 9 7950X",16,32,38000,"AM5",55000,amazon_link("Ryzen 9 7950X")),
        CPU("Ryzen 7 8700X",8,16,31000,"AM5",36000,amazon_link("Ryzen 7 8700X")),
        CPU("Ryzen 7 8800X3D",8,16,35000,"AM5",45000,amazon_link("Ryzen 7 8800X3D")),
        CPU("Ryzen 9 8900X",12,24,39000,"AM5",48000,amazon_link("Ryzen 9 8900X")),
        CPU("Ryzen 9 8950X",16,32,43000,"AM5",62000,amazon_link("Ryzen 9 8950X")),
    ]

    for cpu in cpus:
        db.session.add(cpu)

    db.session.commit()

    print("CPU data inserted successfully.")