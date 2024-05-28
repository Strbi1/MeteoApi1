"""Functions handling API endpoints."""

import database
import models


def getMeasurements():
    measurements = models.Measurement.query.all()
    measurements = map(lambda m: m.to_dict(), measurements)
    return list(measurements)


def createMeasurement(body):
    measurement = models.Measurement.from_dict(**body)
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


def getLocations():
    locations = models.Location.query.all()
    locations = map(lambda m: m.to_dict(), locations)
    return list(locations)


def createLocation(body):
    locations = models.Location.from_dict(**body)
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
    locations.id = body["id"]    
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


def getVariables():
    variables = models.Variable.query.all()
    variables = map(lambda m: m.to_dict(), variables)
    return list(variables)


def createVariable(body):
    variables = models.Variable.from_dict(**body)
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
    variables.id = body["id"]
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


def getSources():
    sources = models.Source.query.all()
    sources = map(lambda m: m.to_dict(), sources)
    return list(sources)


def createSource(body):
    sources = models.Source.from_dict(**body)
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
    sources.id = body["id"]
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


def getStations():
    stations = models.Station.query.all()
    stations = map(lambda m: m.to_dict(), stations)
    return list(stations)


def createStation(body):
    stations = models.Station.from_dict(**body)
    database.db.session.add(stations)
    database.db.session.commit()
    return stations.to_dict()


def getStationById(id):
    stations = models.Station.query.filter_by(id=id).first()
    if stations is None:
        return ("Stations not found.", 404)
    return stations.to_dict()


def updateStationById(body, id):
    stations = models.Station.query.filter_by(id=id).first()
    if stations is None:
        return ("Stations not found.", 404)
    stations.id = body["id"]
    stations.name = body["name"]
    stations.type = body["type"]
    stations.location_id = body["location_id"]
    stations.source_id = body["source_id"]
    database.db.session.commit()
    return 200


def removeStationById(id):
    stations = models.Station.query.filter_by(id=id).delete()
    if not stations:
        return ("Stations not found.", 404)
    database.db.session.commit()
    return 200

def getMeasurementSources():
    measurement_sources = models.MeasurementSource.query.all()
    measurement_sources = map(lambda m: m.to_dict(), measurement_sources)
    return list(measurement_sources)


def createMeasurementSources(body):
    measurement_sources = models.MeasurementSource.from_dict(**body)
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
    measurement_sources.id = body["id"]
    measurement_sources.name = body["name"]
    measurement_sources.location_id = body["location_id"]
    measurement_sources.source_id = body["source_id"]
    measurement_sources.type = body["type"]
    database.db.session.commit()
    return 200


def removeMeasurementSourceById(id):
    measurement_sources = models.MeasurementSource.query.filter_by(id=id).delete()
    if not measurement_sources:
        return ("MeasurementSources not found.", 404)
    database.db.session.commit()
    return 200


