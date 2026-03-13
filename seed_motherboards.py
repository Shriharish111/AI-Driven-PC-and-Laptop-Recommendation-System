from app import create_app
from extensions import db
from models import Motherboard
from utilss import amazon_link

app = create_app()

with app.app_context():

    motherboards = [

        # INTEL LGA1200 (DDR4)
        Motherboard("MSI H410M-A Pro","LGA1200","H410","DDR4",6200,amazon_link("MSI H410M-A Pro motherboard")),
        Motherboard("ASUS Prime H410M-E","LGA1200","H410","DDR4",6800,amazon_link("ASUS Prime H410M-E motherboard")),
        Motherboard("Gigabyte B460M DS3H","LGA1200","B460","DDR4",8000,amazon_link("Gigabyte B460M DS3H motherboard")),
        Motherboard("MSI B560M PRO-VDH","LGA1200","B560","DDR4",9500,amazon_link("MSI B560M PRO-VDH motherboard")),
        Motherboard("ASUS TUF Gaming B560M-PLUS","LGA1200","B560","DDR4",12500,amazon_link("ASUS TUF Gaming B560M-PLUS motherboard")),
        Motherboard("MSI Z490-A Pro","LGA1200","Z490","DDR4",16000,amazon_link("MSI Z490-A Pro motherboard")),

        # INTEL LGA1700 DDR4
        Motherboard("MSI PRO H610M-E DDR4","LGA1700","H610","DDR4",7200,amazon_link("MSI PRO H610M-E DDR4 motherboard")),
        Motherboard("Gigabyte H610M S2 DDR4","LGA1700","H610","DDR4",7000,amazon_link("Gigabyte H610M S2 DDR4 motherboard")),
        Motherboard("ASUS Prime B660M-A DDR4","LGA1700","B660","DDR4",11500,amazon_link("ASUS Prime B660M-A DDR4 motherboard")),
        Motherboard("MSI PRO B760M-A DDR4","LGA1700","B760","DDR4",13000,amazon_link("MSI PRO B760M-A DDR4 motherboard")),
        Motherboard("Gigabyte B760M DS3H AX DDR4","LGA1700","B760","DDR4",14500,amazon_link("Gigabyte B760M DS3H AX DDR4 motherboard")),

        # INTEL LGA1700 DDR5
        Motherboard("MSI PRO B760M-A WiFi DDR5","LGA1700","B760","DDR5",16500,amazon_link("MSI PRO B760M-A WiFi DDR5 motherboard")),
        Motherboard("ASUS Prime B760-PLUS DDR5","LGA1700","B760","DDR5",18000,amazon_link("ASUS Prime B760-PLUS DDR5 motherboard")),
        Motherboard("Gigabyte Z690 UD AX DDR5","LGA1700","Z690","DDR5",22000,amazon_link("Gigabyte Z690 UD AX DDR5 motherboard")),
        Motherboard("MSI PRO Z790-P WiFi DDR5","LGA1700","Z790","DDR5",25000,amazon_link("MSI PRO Z790-P WiFi DDR5 motherboard")),
        Motherboard("ASUS TUF Gaming Z790-PLUS WiFi","LGA1700","Z790","DDR5",28000,amazon_link("ASUS TUF Gaming Z790-PLUS WiFi motherboard")),
        Motherboard("ASUS ROG Strix Z790-E Gaming","LGA1700","Z790","DDR5",42000,amazon_link("ASUS ROG Strix Z790-E Gaming motherboard")),

        # AMD AM4 (DDR4)
        Motherboard("MSI A520M-A Pro","AM4","A520","DDR4",6000,amazon_link("MSI A520M-A Pro motherboard")),
        Motherboard("Gigabyte B450M DS3H V2","AM4","B450","DDR4",7000,amazon_link("Gigabyte B450M DS3H V2 motherboard")),
        Motherboard("ASUS Prime B450M-A II","AM4","B450","DDR4",7800,amazon_link("ASUS Prime B450M-A II motherboard")),
        Motherboard("MSI B550M PRO-VDH WiFi","AM4","B550","DDR4",11000,amazon_link("MSI B550M PRO-VDH WiFi motherboard")),
        Motherboard("Gigabyte B550 AORUS Elite","AM4","B550","DDR4",13500,amazon_link("Gigabyte B550 AORUS Elite motherboard")),
        Motherboard("ASUS TUF Gaming X570-PLUS","AM4","X570","DDR4",19000,amazon_link("ASUS TUF Gaming X570-PLUS motherboard")),

        # AMD AM5 (DDR5)
        Motherboard("MSI PRO A620M-E","AM5","A620","DDR5",10500,amazon_link("MSI PRO A620M-E motherboard")),
        Motherboard("Gigabyte A620M DS3H","AM5","A620","DDR5",11000,amazon_link("Gigabyte A620M DS3H motherboard")),
        Motherboard("ASUS Prime B650M-A","AM5","B650","DDR5",16000,amazon_link("ASUS Prime B650M-A motherboard")),
        Motherboard("MSI PRO B650M-A WiFi","AM5","B650","DDR5",18000,amazon_link("MSI PRO B650M-A WiFi motherboard")),

        # Mid / High End AM5
        Motherboard("Gigabyte B650 AORUS Elite AX","AM5","B650","DDR5",22000,amazon_link("Gigabyte B650 AORUS Elite AX motherboard")),
        Motherboard("ASUS TUF Gaming B650-PLUS WiFi","AM5","B650","DDR5",23000,amazon_link("ASUS TUF Gaming B650-PLUS WiFi motherboard")),
        Motherboard("MSI MAG B650 Tomahawk WiFi","AM5","B650","DDR5",24000,amazon_link("MSI MAG B650 Tomahawk WiFi motherboard")),
        Motherboard("Gigabyte X670 AORUS Elite AX","AM5","X670","DDR5",30000,amazon_link("Gigabyte X670 AORUS Elite AX motherboard")),
        Motherboard("ASUS ROG Strix X670E-E Gaming","AM5","X670E","DDR5",45000,amazon_link("ASUS ROG Strix X670E-E Gaming motherboard")),
        Motherboard("MSI MEG X670E ACE","AM5","X670E","DDR5",60000,amazon_link("MSI MEG X670E ACE motherboard")),

        # CREATOR / WORKSTATION
        Motherboard("ASUS ProArt Z790-Creator WiFi","LGA1700","Z790","DDR5",48000,amazon_link("ASUS ProArt Z790-Creator WiFi motherboard")),
        Motherboard("ASUS ProArt X670E-Creator WiFi","AM5","X670E","DDR5",52000,amazon_link("ASUS ProArt X670E-Creator WiFi motherboard")),
        Motherboard("Gigabyte Z790 AORUS Master","LGA1700","Z790","DDR5",50000,amazon_link("Gigabyte Z790 AORUS Master motherboard")),
        Motherboard("MSI MPG Z790 Carbon WiFi","LGA1700","Z790","DDR5",38000,amazon_link("MSI MPG Z790 Carbon WiFi motherboard")),
    ]

    for board in motherboards:
        db.session.add(board)

    db.session.commit()

    print("Motherboard data inserted successfully.")