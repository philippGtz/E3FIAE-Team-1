from flask import Blueprint, render_template, abort, request, redirect, url_for, flash, session, jsonify
from models import Users, db, BikeComputers, Orders

bp_index = Blueprint('index', __name__)

items = {
    'FC-001': {
        'id': 'FC-001',
        'title': 'Fahrradcomputer blau',
        'summary': 'Fahrradcomputer in der Farbe blau',
        'image_url': '/static/images/fc-1.jpg',
        'description': 'Ein robuster Fahrradcomputer mit Farbdisplay. Ideal für den täglichen Gebrauch.',
        'price': '€ 199,00'
    },
    'FC-002': {
        'id': 'FC-002',
        'title': 'Fahrradcomputer grau',
        'summary': 'Fahrradcomputer in der Farbe grau',
        'image_url': '/static/images/fc-2.jpg',
        'description': 'Eleganter Fahrradcomputer mit langen Batterielaufzeiten.',
        'price': '€ 199,00'
    },
    'FC-003': {
        'id': 'FC-003',
        'title': 'Fahrradcomputer grün',
        'summary': 'Fahrradcomputer in der Farbe grün',
        'image_url': '/static/images/fc-3.jpg',
        'description': 'Leichter Fahrradcomputer mit einfacher Bedienung.',
        'price': '€ 199,00'
    }
}


@bp_index.route('/')
def index():
    return render_template('index.html')


@bp_index.route('/catalog')
def catalog():
    items = BikeComputers.query.all()
    return render_template('catalog.html', items=items)


@bp_index.route('/detail/<int:item_id>')
def detail(item_id):
    item = BikeComputers.query.filter_by(bc_id=item_id).first()
    if not item:
        abort(404)
    user = None
    if session.get('user_id'):
        user = Users.query.filter_by(user_id=session.get('user_id')).first()
    return render_template('detail.html', item=item, user=user)

@bp_index.route('/login', methods=['POST'])
def login():
    print("Pressed Login Button")
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Email: {email}, Password: {password}")

    user = Users.query.filter_by(email=email).first()

    if user and user.password == password:
        session['user_email'] = email
        session['user_id'] = user.user_id
        session['user_first_name'] = user.first_name
        session['user_last_name'] = user.last_name
        flash('Login erfolgreich!', 'success')
        return jsonify({'success': True, 'message': 'Login erfolgreich!'})
    else:
        return jsonify({'success': False, 'message': 'Falsches Passwort. Versuchen Sie es noch einmal.'})


@bp_index.route('/logout')
def logout():
    session.clear()
    flash('Sie wurden erfolgreich abgemeldet.', 'success')
    return redirect(url_for('index.index'))


@bp_index.route('/profile')
def profile():
    if 'user_email' not in session:
        flash('Bitte melden Sie sich zunächst an.', 'warning')
        return redirect(url_for('index.index'))
    
    user_email = session.get('user_email')
    user = Users.query.filter_by(email=user_email).first()
    
    if not user:
        session.clear()
        flash('Benutzerkonto nicht gefunden.', 'danger')
        return redirect(url_for('index.index'))
    
    return render_template('profile.html', user=user)


@bp_index.route('/update-iban', methods=['POST'])
def update_iban():
    if 'user_id' not in session:
        flash('Bitte melden Sie sich zunächst an.', 'warning')
        return redirect(url_for('index.index'))
    
    user_id = session.get('user_id')
    iban = request.form.get('iban')
    
    # Convert empty strings to None
    iban = iban if iban.strip() else None
    
    user = Users.query.filter_by(user_id=user_id).first()
    if not user:
        flash('Benutzer nicht gefunden.', 'danger')
        return redirect(url_for('index.index'))
    
    try:
        user.iban = iban
        db.session.commit()
        flash('IBAN erfolgreich gespeichert!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Fehler beim Speichern der IBAN: {str(e)}', 'danger')
    
    return redirect(url_for('index.profile'))


@bp_index.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    address = request.form.get('address')
    house_number = request.form.get('house_number')
    postal_code = request.form.get('postal_code')
    city = request.form.get('city')
    country = request.form.get('country')
    iban = request.form.get('iban')
    phone_number = request.form.get('phone_number')

    if Users.query.filter_by(email=email).first():
        flash('Ein Benutzer mit dieser E-Mail existiert bereits.', 'danger')
        return redirect(url_for('index.index'))

    # Convert empty strings to None for unique fields
    iban = iban if iban.strip() else None
    phone_number = phone_number if phone_number.strip() else None

    new_user = Users(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password,
        address=address,
        house_number=house_number,
        postal_code=postal_code,
        city=city,
        country=country,
        iban=iban,
        phone_number=phone_number
    )


    db.session.add(new_user)
    db.session.commit()

    user = Users.query.filter_by(email=email).first()

    session['user_email'] = email
    session['user_id'] = user.user_id
    flash('Registrierung erfolgreich! Sie können sich jetzt anmelden.', 'success')
    return redirect(url_for('index.index'))


@bp_index.route('/place-order', methods=['POST'])
def place_order():
    if 'user_id' not in session:
        flash('Bitte melden Sie sich zunächst an.', 'warning')
        return redirect(url_for('index.index'))
    
    user_id = session.get('user_id')
    
    # Überprüfe, ob der Benutzer eine IBAN hat
    user = Users.query.filter_by(user_id=user_id).first()
    if not user or not user.iban:
        flash('Bitte hinterlegen Sie eine IBAN in Ihrem Profil, um Bestellungen zu tätigen.', 'danger')
        return redirect(url_for('index.profile'))
    
    bc_id = request.form.get('bc_id')
    bes_menge = request.form.get('bes_menge')
    
    try:
        bc_id = int(bc_id)
        bes_menge = int(bes_menge)
        
        if bes_menge <= 0:
            flash('Die Menge muss größer als 0 sein.', 'danger')
            return redirect(url_for('index.detail', item_id=bc_id))
        
        # Überprüfe, ob das Produkt existiert
        bike_computer = BikeComputers.query.filter_by(bc_id=bc_id).first()
        if not bike_computer:
            flash('Produkt nicht gefunden.', 'danger')
            return redirect(url_for('index.catalog'))
        
        # Erstelle neue Bestellung
        new_order = Orders(
            user_id=user_id,
            bc_id=bc_id,
            bes_menge=bes_menge
        )
        
        db.session.add(new_order)
        db.session.commit()
        
        flash(f'Bestellung erfolgreich! {bes_menge} x {bike_computer.bes_art_code} wurde bestellt.', 'success')
        return redirect(url_for('index.orders'))
    
    except (ValueError, TypeError):
        flash('Ungültige Eingabe.', 'danger')
        return redirect(url_for('index.catalog'))


@bp_index.route('/orders')
def orders():
    if 'user_id' not in session:
        flash('Bitte melden Sie sich zunächst an.', 'warning')
        return redirect(url_for('index.index'))
    
    user_id = session.get('user_id')
    user_orders = Orders.query.filter_by(user_id=user_id).all()
    
    # Lade die Produktdetails für jede Bestellung
    orders_with_details = []
    for order in user_orders:
        bike_computer = BikeComputers.query.filter_by(bc_id=order.bc_id).first()
        orders_with_details.append({
            'order': order,
            'bike_computer': bike_computer
        })
    
    return render_template('orders.html', orders=orders_with_details)


@bp_index.route('/anlage')
def anlage():
    return render_template('anlage.html')

@bp_index.route('/sapapi', methods=['POST'])
def update_bes_sap_doc_number():
    bes_id = request.form.get('bes_id')
    bes_sap_doc_number = request.form.get('sap_terminnummer')

    if not bes_id or not bes_sap_doc_number:
        return jsonify({'success': False, 'message': 'bes_id und bes_sap_doc_number sind erforderlich.'}), 400

    order = Orders.query.filter_by(bes_id=bes_id).first()
    if not order:
        return jsonify({'success': False, 'message': 'Bestellung nicht gefunden.'}), 404

    try:
        order.bes_sap_doc_number = bes_sap_doc_number
        db.session.commit()
        return jsonify({'success': True, 'message': f'Bestellung {bes_id} erfolgreich mit SAP-Terminnummer {bes_sap_doc_number} aktualisiert.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': f'Fehler beim Aktualisieren der SAP-Terminnummer: {str(e)}'}), 500


@bp_index.route('/sapapi', methods=['GET'])
def get_orders_without_bes_sap_doc_number():
    orders = Orders.query.filter(Orders.bes_sap_doc_number.is_(None)).all()
    orders_data = []
    for order in orders:
        bike_computer = BikeComputers.query.filter_by(bc_id=order.bc_id).first()
        order_data = order.__dict__
        order_data.pop('_sa_instance_state', None)
        if bike_computer:
            order_data.update({
                'bes_art_code': bike_computer.bes_art_code,
                'bes_art_code_desc_short': bike_computer.bes_art_code_desc_short,
                'bc_language': bike_computer.bc_language,
                'bes_art_code_desc_long': bike_computer.bes_art_code_desc_long,
                'bc_image': bike_computer.bc_image
            })
        orders_data.append(order_data)
    return jsonify(orders_data)


@bp_index.route('/sapapi', methods=['PUT'])
def update_order_status_and_delivery():
    bes_sap_doc_number = request.form.get('sap_terminnummer')
    bes_status = request.form.get('bes_status')
    bes_lieferdatum = request.form.get('bes_lieferdatum')
    print("best_status:", bes_status)
    print("best_lieferdatum:", bes_lieferdatum)

    if not bes_sap_doc_number:
        return jsonify({'success': False, 'message': 'bes_sap_doc_number ist erforderlich.'}), 400

    order = Orders.query.filter_by(bes_sap_doc_number=bes_sap_doc_number).first()
    if not order:
        return jsonify({'success': False, 'message': 'Bestellung nicht gefunden.'}), 404

    try:
        if bes_status:
            order.bes_status = bes_status
        if bes_lieferdatum:
            order.bes_lieferdatum = bes_lieferdatum
        db.session.commit()
        return jsonify({'success': True, 'message': f'Bestellung mit SAP-Terminnummer {bes_sap_doc_number} erfolgreich aktualisiert.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': f'Fehler beim Aktualisieren der Bestellung: {str(e)}'}), 500


@bp_index.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
