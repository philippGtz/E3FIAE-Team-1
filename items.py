from flask import Flask
from models import BikeComputers, Users, Orders, db
from config import Config


def initialize_database(app):
    with app.app_context():
        print('Hier in app.app_context()') 
        if app.config.get('RESET_DATABASE', False):
            print('Datenbank wird zurückgesetzt...')
            db.drop_all()
        db.create_all()

        items = [
                BikeComputers(
                    bes_art_code="GPKO3000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER KONFIGURIERBAR",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GPKO4000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER KONFIGURIERBAR SERIALNR.",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GORK1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 16GB (BLAU)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOSK1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 16GB (SCHWARZ)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOWK1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 16GB (WEISS)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOBM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (BLAU)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bes_art_code="GORM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (ROT)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-3.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOSM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (SCHWARZ)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-3.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOWM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (WEISS)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-3.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOBL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (BLAU)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bes_art_code="GORL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (ROT)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-3.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOSL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (SCHWARZ)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GOWL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (WEISS)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRBK1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 16GB (BLAU)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRRK1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 16GB (ROT)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-3.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRSK1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 16GB (SCHWARZ)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRWK1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 16GB (WEISS)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRBM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 32GB (BLAU)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRRM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 32GB (ROT)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-3.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRSM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 32GB (SCHWARZ)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRWM1000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 32GB (WEISS)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRBL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 64GB (BLAU)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRRL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 64GB (ROT)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-3.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRSL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 64GB (SCHWARZ)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bes_art_code="GRWL2000",
                    bes_art_code_desc_short="GPS-RADCOMPUTER ROAD 64GB (WEISS)",
                    bes_art_code_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                ]

        db.session.add_all(items)
        db.session.commit()

        # Überprüfe, ob der Admin-User bereits existiert
        existing_user = Users.query.filter_by(email="admin@example.com").first()
        if not existing_user:
            user = Users(
                email="admin@example.com",
                first_name="Admin",
                last_name="User",
                password="password",
                address="Parkstrasse",
                house_number="7",
                postal_code="69168",
                city="Wiesloch",
                country="Germany",
                iban="DE89370400440532013000",
                phone_number="01234567890"
            )
            db.session.add(user)
            db.session.commit()

        # Überprüfe, ob die Bestellung bereits existiert
        existing_order = Orders.query.filter_by(user_id=1, bes_id=1).first()
        if not existing_order:
            bestellung = Orders(
                user_id=1,
                bes_id=1,
                bc_id=1,
                bes_menge=2,
                bes_status = "offen",
            )
            db.session.add(bestellung)
            db.session.commit()
        db.session.commit()  # Commit the order to the database