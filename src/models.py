"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import datetime
import typing

import sqlalchemy
from sqlalchemy import orm

from open_alchemy import models

Base = models.Base  # type: ignore


class _MeasurementDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    time: str
    variable: "VariableDict"
    value: float
    source: "SourceDict"
    location: "LocationDict"
    measurement_sources: "MeasurementSourceDict"


class MeasurementDict(_MeasurementDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TMeasurement(typing.Protocol):
    """
    SQLAlchemy model protocol.

    merenja

    Attrs:
        id: Identifikacioni broj
        time: Vreme merenja
        variable: Naziv meteorološke promenljive
        value: Vrednost meteorološke promenljive
        source: Izvora podataka
        location: Naziv lokacije
        measurement_sources: Izvor merenja

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    time: 'sqlalchemy.Column[datetime.datetime]'
    variable: 'sqlalchemy.Column["TVariable"]'
    value: 'sqlalchemy.Column[float]'
    source: 'sqlalchemy.Column["TSource"]'
    location: 'sqlalchemy.Column["TLocation"]'
    measurement_sources: 'sqlalchemy.Column["TMeasurementSource"]'

    def __init__(self, time: datetime.datetime, variable: "TVariable", value: float, source: "TSource", location: "TLocation", measurement_sources: "TMeasurementSource", id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive
            source: Izvora podataka
            location: Naziv lokacije
            measurement_sources: Izvor merenja

        """
        ...

    @classmethod
    def from_dict(cls, time: datetime.datetime, variable: "VariableDict", value: float, source: "SourceDict", location: "LocationDict", measurement_sources: "MeasurementSourceDict", id: typing.Optional[int] = None) -> "TMeasurement":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive
            source: Izvora podataka
            location: Naziv lokacije
            measurement_sources: Izvor merenja

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMeasurement":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MeasurementDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Measurement: typing.Type[TMeasurement] = models.Measurement  # type: ignore


class _LocationDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    lat: float
    long: float
    country: str
    type: str
    elevation: int


class LocationDict(_LocationDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TLocation(typing.Protocol):
    """
    SQLAlchemy model protocol.

    lokacije

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv lokacije
        lat: Geografska širina
        long: Geografska dužina
        country: Država lokacije
        type: Vrsta lokacije
        elevation: Nadmorska visina

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    lat: 'sqlalchemy.Column[float]'
    long: 'sqlalchemy.Column[float]'
    country: 'sqlalchemy.Column[str]'
    type: 'sqlalchemy.Column[str]'
    elevation: 'sqlalchemy.Column[int]'

    def __init__(self, name: str, lat: float, long: float, country: str, type: str, elevation: int, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv lokacije
            lat: Geografska širina
            long: Geografska dužina
            country: Država lokacije
            type: Vrsta lokacije
            elevation: Nadmorska visina

        """
        ...

    @classmethod
    def from_dict(cls, name: str, lat: float, long: float, country: str, type: str, elevation: int, id: typing.Optional[int] = None) -> "TLocation":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv lokacije
            lat: Geografska širina
            long: Geografska dužina
            country: Država lokacije
            type: Vrsta lokacije
            elevation: Nadmorska visina

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TLocation":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> LocationDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Location: typing.Type[TLocation] = models.Location  # type: ignore


class _VariableDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    unit: str


class VariableDict(_VariableDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TVariable(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Meteorološka promenljiva

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv meteorološke varijable
        unit: Jedinica promenljive

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    unit: 'sqlalchemy.Column[str]'

    def __init__(self, name: str, unit: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteorološke varijable
            unit: Jedinica promenljive

        """
        ...

    @classmethod
    def from_dict(cls, name: str, unit: str, id: typing.Optional[int] = None) -> "TVariable":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteorološke varijable
            unit: Jedinica promenljive

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TVariable":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> VariableDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Variable: typing.Type[TVariable] = models.Variable  # type: ignore


class _SourceDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    code: str
    name: str
    location: "LocationDict"
    description: str


class SourceDict(_SourceDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TSource(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Naziv izvora podataka

    Attrs:
        id: Identifikacioni broj (kluč)
        code: Kod (skraćeni naziv)
        name: Naziv izvora podataka
        location: Informacije o lokaciji
        description: Opis izvora

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    code: 'sqlalchemy.Column[str]'
    name: 'sqlalchemy.Column[str]'
    location: 'sqlalchemy.Column["TLocation"]'
    description: 'sqlalchemy.Column[str]'

    def __init__(self, code: str, name: str, location: "TLocation", description: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora podataka
            location: Informacije o lokaciji
            description: Opis izvora

        """
        ...

    @classmethod
    def from_dict(cls, code: str, name: str, location: "LocationDict", description: str, id: typing.Optional[int] = None) -> "TSource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora podataka
            location: Informacije o lokaciji
            description: Opis izvora

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TSource":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> SourceDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Source: typing.Type[TSource] = models.Source  # type: ignore


class _StationDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    type: str
    capacity: int
    location: "LocationDict"


class StationDict(_StationDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TStation(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Stanice za merenje

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv meteoroloških stanica
        type: Tip stanice
        capacity: Kpacitet stanice
        location: Informacije o lokaciji

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    type: 'sqlalchemy.Column[str]'
    capacity: 'sqlalchemy.Column[int]'
    location: 'sqlalchemy.Column["TLocation"]'

    def __init__(self, name: str, type: str, capacity: int, location: "TLocation", id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteoroloških stanica
            type: Tip stanice
            capacity: Kpacitet stanice
            location: Informacije o lokaciji

        """
        ...

    @classmethod
    def from_dict(cls, name: str, type: str, capacity: int, location: "LocationDict", id: typing.Optional[int] = None) -> "TStation":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteoroloških stanica
            type: Tip stanice
            capacity: Kpacitet stanice
            location: Informacije o lokaciji

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TStation":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> StationDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Station: typing.Type[TStation] = models.Station  # type: ignore


class _MeasurementSourceDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    lat: float
    long: float
    type: str


class MeasurementSourceDict(_MeasurementSourceDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TMeasurementSource(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Naziv izvora merenja

    Attrs:
        id: Identifikacioni broj (kluč)
        name: Naziv izvora merenja
        lat: Geografska širina
        long: Geografska dužina
        type: Tip merenja

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    lat: 'sqlalchemy.Column[float]'
    long: 'sqlalchemy.Column[float]'
    type: 'sqlalchemy.Column[str]'

    def __init__(self, name: str, lat: float, long: float, type: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (kluč)
            name: Naziv izvora merenja
            lat: Geografska širina
            long: Geografska dužina
            type: Tip merenja

        """
        ...

    @classmethod
    def from_dict(cls, name: str, lat: float, long: float, type: str, id: typing.Optional[int] = None) -> "TMeasurementSource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (kluč)
            name: Naziv izvora merenja
            lat: Geografska širina
            long: Geografska dužina
            type: Tip merenja

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMeasurementSource":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MeasurementSourceDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


MeasurementSource: typing.Type[TMeasurementSource] = models.MeasurementSource  # type: ignore
