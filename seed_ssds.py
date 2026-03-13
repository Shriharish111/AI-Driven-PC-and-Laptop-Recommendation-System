from app import create_app
from extensions import db
from models import SSD
from utilss import amazon_link

app = create_app()

with app.app_context():

    ssds = [

        # SATA SSD
        SSD("Crucial BX500 240GB","SATA",240,500,1650,amazon_link("Crucial BX500 240GB SSD")),
        SSD("Crucial BX500 480GB","SATA",480,500,2750,amazon_link("Crucial BX500 480GB SSD")),
        SSD("WD Green 480GB","SATA",480,500,2800,amazon_link("WD Green 480GB SSD")),
        SSD("WD Blue 1TB SATA","SATA",1000,500,5200,amazon_link("WD Blue 1TB SATA SSD")),
        SSD("Samsung 870 EVO 500GB","SATA",500,500,4800,amazon_link("Samsung 870 EVO 500GB SSD")),
        SSD("Samsung 870 EVO 1TB","SATA",1000,500,7800,amazon_link("Samsung 870 EVO 1TB SSD")),
        SSD("Kingston A400 480GB","SATA",480,500,2900,amazon_link("Kingston A400 480GB SSD")),
        SSD("Kingston A400 960GB","SATA",960,500,5000,amazon_link("Kingston A400 960GB SSD")),

        # NVMe Gen3
        SSD("WD Blue SN570 500GB","NVMe Gen3",500,1500,3200,amazon_link("WD Blue SN570 500GB NVMe SSD")),
        SSD("WD Blue SN570 1TB","NVMe Gen3",1000,1500,5400,amazon_link("WD Blue SN570 1TB NVMe SSD")),
        SSD("Crucial P3 500GB","NVMe Gen3",500,1500,3000,amazon_link("Crucial P3 500GB NVMe SSD")),
        SSD("Crucial P3 1TB","NVMe Gen3",1000,1500,5200,amazon_link("Crucial P3 1TB NVMe SSD")),
        SSD("Kingston NV2 500GB","NVMe Gen3",500,1500,2900,amazon_link("Kingston NV2 500GB NVMe SSD")),
        SSD("Kingston NV2 1TB","NVMe Gen3",1000,1500,4800,amazon_link("Kingston NV2 1TB NVMe SSD")),
        SSD("Samsung 970 EVO Plus 500GB","NVMe Gen3",500,1500,4500,amazon_link("Samsung 970 EVO Plus 500GB NVMe SSD")),
        SSD("Samsung 970 EVO Plus 1TB","NVMe Gen3",1000,1500,7500,amazon_link("Samsung 970 EVO Plus 1TB NVMe SSD")),

        # NVMe Gen4
        SSD("WD Black SN770 500GB","NVMe Gen4",500,3000,4200,amazon_link("WD Black SN770 500GB NVMe SSD")),
        SSD("WD Black SN770 1TB","NVMe Gen4",1000,3000,6500,amazon_link("WD Black SN770 1TB NVMe SSD")),
        SSD("WD Black SN850X 1TB","NVMe Gen4",1000,3200,9800,amazon_link("WD Black SN850X 1TB NVMe SSD")),
        SSD("Samsung 980 Pro 1TB","NVMe Gen4",1000,3200,9500,amazon_link("Samsung 980 Pro 1TB NVMe SSD")),
        SSD("Samsung 990 Pro 1TB","NVMe Gen4",1000,3400,12500,amazon_link("Samsung 990 Pro 1TB NVMe SSD")),
        SSD("Crucial P5 Plus 1TB","NVMe Gen4",1000,3000,7800,amazon_link("Crucial P5 Plus 1TB NVMe SSD")),
        SSD("Kingston KC3000 1TB","NVMe Gen4",1000,3100,8500,amazon_link("Kingston KC3000 1TB NVMe SSD")),
        SSD("Adata XPG Gammix S70 Blade 1TB","NVMe Gen4",1000,3000,7200,amazon_link("Adata XPG Gammix S70 Blade 1TB SSD")),
        SSD("MSI Spatium M450 1TB","NVMe Gen4",1000,2900,6000,amazon_link("MSI Spatium M450 1TB NVMe SSD")),
        SSD("Corsair MP600 Pro 1TB","NVMe Gen4",1000,3200,10500,amazon_link("Corsair MP600 Pro 1TB NVMe SSD")),

        # NVMe Gen5
        SSD("Crucial T700 1TB","NVMe Gen5",1000,6000,18500,amazon_link("Crucial T700 1TB NVMe Gen5 SSD")),
        SSD("Crucial T700 2TB","NVMe Gen5",2000,6000,28000,amazon_link("Crucial T700 2TB NVMe Gen5 SSD")),
        SSD("Corsair MP700 1TB","NVMe Gen5",1000,6000,20000,amazon_link("Corsair MP700 1TB NVMe Gen5 SSD")),
        SSD("MSI Spatium M570 2TB","NVMe Gen5",2000,6000,30000,amazon_link("MSI Spatium M570 2TB NVMe Gen5 SSD")),
        SSD("Gigabyte Aorus Gen5 10000 2TB","NVMe Gen5",2000,6000,32000,amazon_link("Gigabyte Aorus Gen5 10000 2TB SSD")),

        # High Capacity
        SSD("WD Black SN850X 2TB","NVMe Gen4",2000,3200,17500,amazon_link("WD Black SN850X 2TB NVMe SSD")),
        SSD("Samsung 990 Pro 2TB","NVMe Gen4",2000,3400,21000,amazon_link("Samsung 990 Pro 2TB NVMe SSD")),
        SSD("Kingston KC3000 2TB","NVMe Gen4",2000,3100,16000,amazon_link("Kingston KC3000 2TB NVMe SSD")),
        SSD("Crucial P3 Plus 2TB","NVMe Gen4",2000,3000,11500,amazon_link("Crucial P3 Plus 2TB NVMe SSD")),
        SSD("Samsung 870 EVO 4TB","SATA",4000,500,32000,amazon_link("Samsung 870 EVO 4TB SSD")),
    ]

    for ssd in ssds:
        db.session.add(ssd)

    db.session.commit()

    print("SSD data inserted successfully.")