from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///climate_data.db'
db = SQLAlchemy(app)

# Define the ClimateData model
class ClimateData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(255), nullable=False)
    area_code = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    chances_of_rain = db.Column(db.Float, nullable=False)

# Create the database tables
# db.create_all()

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()

    climate = data.get('climate')
    area_code = data.get('area_code')
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    chances_of_rain = data.get('chances_of_rain')

    if not (climate and area_code and temperature and humidity and chances_of_rain):
        return jsonify({"success": False, "error": "Invalid payload"}), 400

    climate_data = ClimateData(
        climate=climate,
        area_code=area_code,
        temperature=temperature,
        humidity=humidity,
        chances_of_rain=chances_of_rain
    )

    db.session.add(climate_data)
    db.session.commit()

    return jsonify({"success": True, "error": None, "data": {"id": climate_data.id}})

@app.route('/fetch_all_records', methods=['GET'])
def fetch_all_records():
    records = ClimateData.query.all()

    data = [{"id": record.id, "climate": record.climate, "area_code": record.area_code, "temperature": record.temperature, "humidity": record.humidity, "chances_of_rain": record.chances_of_rain} for record in records]

    return jsonify(data)

@app.route('/fetch_records_by_area/<int:area_code>', methods=['GET'])
def fetch_records_by_area(area_code):
    records = ClimateData.query.filter_by(area_code=area_code).all()

    if not records:
        return jsonify({"success": False, "error": "No records found for the given area code"}), 404

    data = [{"id": record.id, "climate": record.climate, "area_code": record.area_code, "temperature": record.temperature, "humidity": record.humidity, "chances_of_rain": record.chances_of_rain} for record in records]

    return jsonify(data)

@app.route('/fetch_records_by_climate/<climate>', methods=['GET'])
def fetch_records_by_climate(climate):
    records = ClimateData.query.filter_by(climate=climate).all()

    if not records:
        return jsonify({"success": False, "error": "No records found for the given climate"}), 404

    data = [{"id": record.id, "climate": record.climate, "area_code": record.area_code, "temperature": record.temperature, "humidity": record.humidity, "chances_of_rain": record.chances_of_rain} for record in records]

    return jsonify(data)

if __name__ == '__main__':
    app.run()
