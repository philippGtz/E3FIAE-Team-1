from flask import Flask, request, send_file, session
import index
from config import Config
from models import db, Orders, BikeComputers, Users
from items import initialize_database
import subprocess
import csv
import io

app = Flask(__name__)

def get_git_info():
    try:
        commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        git_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=1']).strip().decode('utf-8')
        return commit_id, git_tag
    except subprocess.CalledProcessError:
        return None, None

app.config.from_object(Config)

app.secret_key = app.config["SECRET_KEY"]

db.init_app(app)

app.register_blueprint(index.bp_index)

@app.context_processor
def inject_git_info():
    commit_id, git_tag = get_git_info()
    return dict(commit_id=commit_id, git_tag=git_tag)

@app.context_processor
def inject_user_info():
    
    user_data = {'first_name': '', 'last_name': ''}
    
    if session.get('user_id'):
        user = Users.query.filter_by(user_id=session.get('user_id')).first()
        if user:
            user_data['first_name'] = user.first_name or ''
            user_data['last_name'] = user.last_name or ''
    
    return dict(
        user_first_name=user_data['first_name'],
        user_last_name=user_data['last_name']
    )

@app.route('/export_csv', methods=['POST'])
def export_csv():
    
    filter_option = request.form.get('filter')
    user_id = session.get('user_id')
    
    if not user_id:
        return "Nicht authentifiziert", 401
    
    all_orders = Orders.query.filter_by(user_id=user_id).all()
    
    filtered_orders = []
    for order in all_orders:
        if filter_option == 'offen' and order.sap_terminnummer is None:
            filtered_orders.append(order)
        elif filter_option == 'erfasst' and order.sap_terminnummer is not None and order.delivery_date is None:
            filtered_orders.append(order)
        elif filter_option == 'erledigt' and order.delivery_date is not None:
            filtered_orders.append(order)
    
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow(['Bestellung ID', 'Artikel', 'Menge', 'SAP-Terminnummer', 'Lieferdatum', 'Status'])
    
    for order in filtered_orders:
        bike_computer = BikeComputers.query.filter_by(bc_id=order.bc_id).first()
        bike_name = bike_computer.bc_material if bike_computer else 'Unknown'
        
        sap_term = order.sap_terminnummer if order.sap_terminnummer else 'N/A'
        delivery_date = order.delivery_date.strftime('%d.%m.%Y') if order.delivery_date else 'N/A'
        status = order.order_status if order.order_status else filter_option
        
        csv_writer.writerow([order.order_id, bike_name, order.quantity, sap_term, delivery_date, status])
    
    csv_buffer.seek(0)
    byte_buffer = io.BytesIO(csv_buffer.getvalue().encode('utf-8'))
    
    return send_file(
        byte_buffer,
        mimetype='text/csv',
        as_attachment=True,
        download_name='bestellungen.csv'
    )

if __name__ == '__main__':
  initialize_database(app)
  app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
  print('Start aus Entwicklungsumgebung')
else:
  print('Start von Webserver')