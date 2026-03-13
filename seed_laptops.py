from app import create_app
from extensions import db
from models import Laptop
from utilss import amazon_link

app = create_app()

with app.app_context():

    laptops = [

        # OFFICE / STUDENT
        Laptop("HP 15s i3 12th Gen",14000,2000,8,512,38000,"office",amazon_link("HP 15s i3 12th Gen laptop")),
        Laptop("Dell Inspiron 15 3520 i3",14000,2000,8,512,37000,"office",amazon_link("Dell Inspiron 15 3520 i3 laptop")),
        Laptop("Lenovo IdeaPad Slim 3 Ryzen 5 5500U",16000,2500,8,512,39000,"office",amazon_link("Lenovo IdeaPad Slim 3 Ryzen 5 5500U")),
        Laptop("ASUS Vivobook 15 i3 13th Gen",15000,2000,8,512,41000,"office",amazon_link("ASUS Vivobook 15 i3 13th Gen")),
        Laptop("Acer Aspire 3 Ryzen 3 5300U",12000,2000,8,512,34000,"office",amazon_link("Acer Aspire 3 Ryzen 3 5300U")),
        Laptop("Lenovo V15 i5 12th Gen",18000,2500,8,512,45000,"office",amazon_link("Lenovo V15 i5 12th Gen")),
        Laptop("HP 14s Ryzen 5 5500U",16000,2500,8,512,42000,"office",amazon_link("HP 14s Ryzen 5 5500U")),
        Laptop("Dell Vostro 3520 i5 12th Gen",18000,2500,8,512,48000,"office",amazon_link("Dell Vostro 3520 i5 12th Gen")),

        # MID RANGE
        Laptop("ASUS Vivobook 16X i5 13th Gen",20000,3000,16,512,55000,"balanced",amazon_link("ASUS Vivobook 16X i5 13th Gen")),
        Laptop("Lenovo IdeaPad Gaming 3 RTX 3050",20000,12000,16,512,68000,"gaming",amazon_link("Lenovo IdeaPad Gaming 3 RTX 3050")),
        Laptop("HP Pavilion 15 Ryzen 7 5700U",17000,3000,16,512,60000,"balanced",amazon_link("HP Pavilion 15 Ryzen 7 5700U")),
        Laptop("Acer Aspire 7 RTX 3050",21000,12000,16,512,65000,"gaming",amazon_link("Acer Aspire 7 RTX 3050")),
        Laptop("Dell G15 RTX 3050",22000,12000,16,512,72000,"gaming",amazon_link("Dell G15 RTX 3050")),
        Laptop("MSI GF63 Thin RTX 3050",21000,12000,16,512,70000,"gaming",amazon_link("MSI GF63 Thin RTX 3050")),

        # GAMING RTX 4050 / 4060 / 4070
        Laptop("ASUS TUF F15 RTX 3050",22000,12000,16,512,75000,"gaming",amazon_link("ASUS TUF F15 RTX 3050")),
        Laptop("Lenovo LOQ 15 RTX 4050",24000,17000,16,512,85000,"gaming",amazon_link("Lenovo LOQ 15 RTX 4050")),
        Laptop("HP Victus 15 RTX 4050",24000,17000,16,512,88000,"gaming",amazon_link("HP Victus 15 RTX 4050")),
        Laptop("Acer Nitro V RTX 4050",24000,17000,16,512,82000,"gaming",amazon_link("Acer Nitro V RTX 4050")),
        Laptop("MSI Katana 15 RTX 4060",26000,21000,16,512,105000,"gaming",amazon_link("MSI Katana 15 RTX 4060")),
        Laptop("ASUS ROG Strix G16 RTX 4060",27000,21000,16,1000,125000,"gaming",amazon_link("ASUS ROG Strix G16 RTX 4060")),
        Laptop("Lenovo Legion 5 RTX 4060",27000,21000,16,1000,130000,"gaming",amazon_link("Lenovo Legion 5 RTX 4060")),
        Laptop("Acer Predator Helios Neo RTX 4060",27000,21000,16,1000,128000,"gaming",amazon_link("Acer Predator Helios Neo RTX 4060")),
        Laptop("ASUS ROG Strix Scar 16 RTX 4070",30000,25000,32,1000,175000,"gaming",amazon_link("ASUS ROG Strix Scar 16 RTX 4070")),
        Laptop("Lenovo Legion Pro 5 RTX 4070",30000,25000,32,1000,170000,"gaming",amazon_link("Lenovo Legion Pro 5 RTX 4070")),

        # CREATOR
        Laptop("ASUS Vivobook Pro 15 OLED RTX 3050",22000,12000,16,1000,92000,"creator",amazon_link("ASUS Vivobook Pro 15 OLED RTX 3050")),
        Laptop("HP Envy x360 Ryzen 7",20000,3000,16,1000,95000,"creator",amazon_link("HP Envy x360 Ryzen 7")),
        Laptop("Dell Inspiron 16 Plus RTX 3050",23000,12000,16,1000,110000,"creator",amazon_link("Dell Inspiron 16 Plus RTX 3050")),
        Laptop("ASUS ProArt Studiobook RTX 4060",28000,21000,32,1000,160000,"creator",amazon_link("ASUS ProArt Studiobook RTX 4060")),
        Laptop("MSI Creator M16 RTX 4060",28000,21000,32,1000,155000,"creator",amazon_link("MSI Creator M16 RTX 4060")),
        Laptop("Lenovo Yoga Pro 7 RTX 4050",24000,17000,16,1000,125000,"creator",amazon_link("Lenovo Yoga Pro 7 RTX 4050")),

        # PREMIUM BUSINESS
        Laptop("MacBook Air M2",20000,5000,16,512,105000,"premium",amazon_link("MacBook Air M2")),
        Laptop("MacBook Air M3",26000,6000,16,512,120000,"premium",amazon_link("MacBook Air M3")),
        Laptop("MacBook Pro M3",32000,8000,16,1000,170000,"premium",amazon_link("MacBook Pro M3")),
        Laptop("Dell XPS 13",25000,4000,16,1000,160000,"premium",amazon_link("Dell XPS 13 laptop")),
        Laptop("HP Spectre x360",24000,4000,16,1000,155000,"premium",amazon_link("HP Spectre x360 laptop")),
        Laptop("Lenovo ThinkPad X13 Gen 4",23000,4000,16,1000,145000,"premium",amazon_link("Lenovo ThinkPad X13 Gen 4")),
        Laptop("ASUS Zenbook 14 OLED",22000,4000,16,1000,110000,"premium",amazon_link("ASUS Zenbook 14 OLED")),

        # HIGH END FLAGSHIP
        Laptop("ASUS ROG Zephyrus G14 RTX 4070",32000,25000,32,1000,185000,"gaming",amazon_link("ASUS ROG Zephyrus G14 RTX 4070")),
        Laptop("MSI Raider GE78 RTX 4080",35000,32000,32,2000,260000,"gaming",amazon_link("MSI Raider GE78 RTX 4080")),
        Laptop("ASUS ROG Strix Scar 18 RTX 4080",35000,32000,32,2000,280000,"gaming",amazon_link("ASUS ROG Strix Scar 18 RTX 4080")),
        Laptop("Acer Predator Helios 18 RTX 4080",35000,32000,32,2000,270000,"gaming",amazon_link("Acer Predator Helios 18 RTX 4080")),
        Laptop("MSI Titan GT77 RTX 4090",38000,38000,64,2000,400000,"gaming",amazon_link("MSI Titan GT77 RTX 4090")),
    ]

    for laptop in laptops:
        db.session.add(laptop)

    db.session.commit()

    print("Laptop data inserted successfully.")