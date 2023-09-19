from app import app, db, ClimateData

# Create the application context
app.app_context().push()

# Create the database tables
db.create_all()

# Sample data
sample_data = [
    {"climate": "hot", "area_code": 111, "temperature": 25, "humidity": 88, "chances_of_rain": 40},
    {"climate": "humid", "area_code": 222, "temperature": 30, "humidity": 90, "chances_of_rain": 50},
    {"climate": "rainy", "area_code": 333, "temperature": 20, "humidity": 75, "chances_of_rain": 60},
    {"climate": "cold", "area_code": 444, "temperature": 10, "humidity": 50, "chances_of_rain": 10},
]

# Add sample data to the database
for data in sample_data:
    climate_data = ClimateData(
        climate=data["climate"],
        area_code=data["area_code"],
        temperature=data["temperature"],
        humidity=data["humidity"],
        chances_of_rain=data["chances_of_rain"],
    )
    db.session.add(climate_data)

# Commit the changes
db.session.commit()
