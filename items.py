from flask import Flask
from models import BikeComputers, Users, Orders, db
from config import Config


def initialize_database(app):
    with app.app_context():
        print('Hier in app.app_context()') 
        db.drop_all() 
        db.create_all()

        items = [
                BikeComputers(
                    bc_material="GPKO3000",
                    bc_material_desc_short="GPS-RADCOMPUTER KONFIGURIERBAR",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GPKO4000",
                    bc_material_desc_short="GPS-RADCOMPUTER KONFIGURIERBAR SERIALNR.",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GORK1000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 16GB (BLAU)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bc_material="GOSK1000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 16GB (SCHWARZ)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GOWK1000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 16GB (WEISS)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GOBM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (BLAU)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bc_material="GORM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (ROT)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GOSM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (SCHWARZ)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GOWM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 32GB (WEISS)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GOBL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (BLAU)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bc_material="GORL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (ROT)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GOSL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (SCHWARZ)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GOWL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER OFFROAD 64GB (WEISS)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRBK1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 16GB (BLAU)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bc_material="GRRK1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 16GB (ROT)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRSK1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 16GB (SCHWARZ)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRWK1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 16GB (WEISS)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRBM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 32GB (BLAU)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bc_material="GRRM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 32GB (ROT)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRSM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 32GB (SCHWARZ)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRWM1000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 32GB (WEISS)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRBL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 64GB (BLAU)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-1.jpg"
                ),
                BikeComputers(
                    bc_material="GRRL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 64GB (ROT)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRSL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 64GB (SCHWARZ)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                BikeComputers(
                    bc_material="GRWL2000",
                    bc_material_desc_short="GPS-RADCOMPUTER ROAD 64GB (WEISS)",
                    bc_material_desc_long="Langbeschreibung Bsp",
                    bc_language="DE",
                    bc_image="fc-2.jpg"
                ),
                ]

        db.session.add_all(items)
        db.session.commit()

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

        bestellung = Orders(
            user_id=1,
            order_id=1,
            bc_id=1,
            quantity=2
        )

        db.session.add(user)
        db.session.commit()

        db.session.add(bestellung)  # Add the order to the session
        db.session.commit()  # Commit the order to the database