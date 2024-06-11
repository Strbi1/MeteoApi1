"""Functions handling API endpoints."""

import database
import models


def getMeasurements(location=None):
    query = models.Measurement.query
    if location:
        query = query.filter(models.Location.name.ilike(f'%{location}%'))
    else:
        print("No name provided, returning all measurements")
    measurements = query.all()
    measurements = map(lambda m: m.to_dict(), measurements)
    return list(measurements)  


def createMeasurement(body):
    measurement = models.Measurement.from_dict(lat = body["lat"], long = body["long"], time = body["time"],
    variable = body["variable"], value = body["value"], unit = body["unit"], source_id = body["source_id"], location = body["location"], measurement_sources_id = body["measurement_sources_id"])
    database.db.session.add(measurement)
    database.db.session.commit()
    return measurement.to_dict()


def getMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    return measurement.to_dict()


def updateMeasurementById(body, id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    measurement.lat = body["lat"]
    measurement.long = body["long"]
    measurement.lat = body["lat"]
    measurement.time = body["time"]
    measurement.variable = body["variable"]
    measurement.value = body["value"]
    measurement.unit = body["unit"]
    measurement.source_id = body["source_id"]
    measurement.location = body["location"]   
    measurement.measurement_sources_id = body["measurement_sources_id"]
    database.db.session.commit()
    return 200


def removeMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).delete()
    if not measurement:
        return ("Measurement not found.", 404)
    database.db.session.commit()
    return 200

def getLocations(name=None):
    query = models.Location.query
    if name:
        query = query.filter(models.Location.name.ilike(f'%{name}%'))
    else:
        print("No name provided, returning all locations")
    locations = query.all() 
    locations = [l.to_dict() for l in locations] 
    return locations


def createLocation(body):
    locations = models.Location.from_dict(name=body["name"], lat=body["lat"], long = body["long"], country = body["country"], type = body["type"], elevation = body["elevation"])
    database.db.session.add(locations)
    database.db.session.commit()
    return locations.to_dict()


def getLocationById(id):
    locations = models.Location.query.filter_by(id=id).first()
    if locations is None:
        return ("Locations not found.", 404)
    return locations.to_dict()


def updateLocationById(body, id):
    locations = models.Location.query.filter_by(id=id).first()
    if locations is None:
        return ("Locations not found.", 404)  
    locations.name = body["name"]
    locations.lat = body["lat"]
    locations.long = body["long"]
    locations.country = body["country"]
    locations.type = body["type"]
    locations.elevation = body["elevation"]
    database.db.session.commit()
    return 200


def removeLocationById(id):
    locations = models.Location.query.filter_by(id=id).delete()
    if not locations:
        return ("Locations not found.", 404)
    database.db.session.commit()
    return 200

  
def getVariables(name=None):
    query = models.Variable.query
    if name:
        query = query.filter(models.Variable.name.ilike(f'%{name}%'))
    else:
        return []
    variables = query.all()
    variables = [v.to_dict() for v in variables]
    return variables


def createVariable(body):
    variables = models.Variable(name=body["name"], unit=body["unit"])
    database.db.session.add(variables)
    database.db.session.commit()
    return variables.to_dict()


def getVariableById(id):
    variables = models.Variable.query.filter_by(id=id).first()
    if variables is None:
        return ("Varibales not found.", 404)
    return variables.to_dict()


def updateVariableById(body, id):
    variables = models.Variable.query.filter_by(id=id).first()
    if variables is None:
        return ("Variables not found.", 404)
    variables.name = body["name"]
    variables.unit = body["unit"]
    database.db.session.commit()
    return 200


def removeVariableById(id):
    variables = models.Variable.query.filter_by(id=id).delete()
    if not variables:
        return ("Variables not found.", 404)
    database.db.session.commit()
    return 200


def getSource(code=None):
    query = models.Source.query
    if code:
        query = query.filter(models.Source.code.ilike(f'%{code}%'))
    else:
        return []
    sources = query.all()
    sources = [s.to_dict() for s in sources]
    return sources


def createSource(body):
    location = models.Location.query.filter_by(id=body['location_id']).first()
    if not location:
        return ("Location not found.", 404)
    source_data = {
        "name": body["name"],
        "code": body["code"],
        "description": body["description"],
        "location_id": location.id
    }
    sources = models.Source.from_dict(**source_data)
    database.db.session.add(sources)
    database.db.session.commit()
    return sources.to_dict()


def getSourceById(id):
    sources = models.Source.query.filter_by(id=id).first()
    if sources is None:
        return ("Sources not found.", 404)
    return sources.to_dict()


def updateSourceById(body, id):
    sources = models.Source.query.filter_by(id=id).first()
    if sources is None:
        return ("Sources not found.", 404)
    sources.code = body["code"]
    sources.name = body["name"]
    database.db.session.commit()
    return 200


def removeSourceById(id):
    sources = models.Source.query.filter_by(id=id).delete()
    if not sources:
        return ("Sources not found.", 404)
    database.db.session.commit()
    return 200


def getStation(type=None):
    query = models.Station.query
    if type:
        print(f"Filtering locations by name: {type}")
        query = query.filter(models.Station.type.ilike(f'%{type}%'))
    else:
        print("No name provided, returning all locations")
    stations = query.all()
    stations = [st.to_dict() for st in stations]
    return stations


def createStation(body):
    # Pronađem ili kreiraj location objekat
    location = models.Location.query.filter_by(id=body['location_id']).first()
    if not location:
        return ("Location not found.", 404)

    # Kreiram Station sa location objektom
    station_data = {
        "name": body["name"],
        "type": body["type"],
        "capacity": body["capacity"],
        "location_id": location.id
    }

    station = models.Station.from_dict(**station_data)
    database.db.session.add(station)
    database.db.session.commit()
    return station.to_dict()

def getStationById(id):
    stations = models.Station.query.filter_by(id=id).first()
    if stations is None:
        return ("Stations not found.", 404)
    return stations.to_dict()


def updateStationById(body, id):
    stations = models.Station.query.filter_by(id=id).first()
    if stations is None:
        return ("Stations not found.", 404)
    stations.name = body["name"]
    stations.type = body["type"]
    stations.capacity = body["capacity"]
    stations.location_id = body['location_id']
    database.db.session.commit()
    return 200

def removeStationById(id):
    stations = models.Station.query.filter_by(id=id).delete()
    if not stations:
        return ("Stations not found.", 404)
    database.db.session.commit()
    return 200


def getMeasurementSources(type=None):
    query = models.MeasurementSource.query
    if type:
        print(f"Filtering locations by name: {type}")
        query = query.filter(models.MeasurementSource.type.ilike(f'%{type}%'))
    else:
        print("No name provided, returning all locations")
    measurement_sources = query.all()
    measurement_sources = [ms.to_dict() for ms in measurement_sources]
    return measurement_sources


def createMeasurementSources(body):
    measurement_sources = models.MeasurementSource.from_dict(name=body["name"], lat=body["lat"], long=body['long'],type=body['type'])
    database.db.session.add(measurement_sources)
    database.db.session.commit()
    return measurement_sources.to_dict()


def getMeasurementSourceById(id):
    measurement_sources = models.MeasurementSource.query.filter_by(id=id).first()
    if measurement_sources is None:
        return ("MeasurementSources not found.", 404)
    return measurement_sources.to_dict()


def updateMeasurementSourceById(body, id):
    measurement_sources = models.MeasurementSource.query.filter_by(id=id).first()
    if measurement_sources is None:
        return ("MeasurementSources not found.", 404)
    measurement_sources.name = body["name"]
    measurement_sources.lat = body["lat"]
    measurement_sources.long = body["long"]
    measurement_sources.type = body["type"]
    database.db.session.commit()
    return 200


def removeMeasurementSourceById(id):
    measurement_sources = models.MeasurementSource.query.filter_by(id=id).delete()
    if not measurement_sources:
        return ("MeasurementSources not found.", 404)
    database.db.session.commit()
    return 200


