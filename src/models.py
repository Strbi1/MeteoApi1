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

    lat: float
    long: float
    time: str
    variable: str
    value: float
    unit: str
    source_id: int
    location_id: int
    measurement_sources_id: int


class MeasurementDict(_MeasurementDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TMeasurement(typing.Protocol):
    """
    SQLAlchemy model protocol.

    merenja

    Attrs:
        id: Identifikacioni broj
        lat: Geografska širina
        long: Geografska dužina
        time: Vreme merenja
        variable: Naziv meteorološke promenljive
        value: Vrednost meteorološke promenljive
        unit: Jedinica merene promenljive
        source_id: ID izvora podataka
        location_id: ID lokacije
        measurement_sources_id: ID izvor merenja

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    lat: 'sqlalchemy.Column[float]'
    long: 'sqlalchemy.Column[float]'
    time: 'sqlalchemy.Column[datetime.datetime]'
    variable: 'sqlalchemy.Column[str]'
    value: 'sqlalchemy.Column[float]'
    unit: 'sqlalchemy.Column[str]'
    source_id: 'sqlalchemy.Column[int]'
    location_id: 'sqlalchemy.Column[int]'
    measurement_sources_id: 'sqlalchemy.Column[int]'

    def __init__(self, lat: float, long: float, time: datetime.datetime, variable: str, value: float, unit: str, source_id: int, location_id: int, measurement_sources_id: int, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj
            lat: Geografska širina
            long: Geografska dužina
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive
            unit: Jedinica merene promenljive
            source_id: ID izvora podataka
            location_id: ID lokacije
            measurement_sources_id: ID izvor merenja

        """
        ...

    @classmethod
    def from_dict(cls, lat: float, long: float, time: datetime.datetime, variable: str, value: float, unit: str, source_id: int, location_id: int, measurement_sources_id: int, id: typing.Optional[int] = None) -> "TMeasurement":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj
            lat: Geografska širina
            long: Geografska dužina
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive
            unit: Jedinica merene promenljive
            source_id: ID izvora podataka
            location_id: ID lokacije
            measurement_sources_id: ID izvor merenja

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


class LocationDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str
    lat: float
    long: float
    country: str
    type: str
    elevation: int


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

    def __init__(self, id: int, name: str, lat: float, long: float, country: str, type: str, elevation: int) -> None:
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
    def from_dict(cls, id: int, name: str, lat: float, long: float, country: str, type: str, elevation: int) -> "TLocation":
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


class VariableDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str
    unit: str


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

    def __init__(self, id: int, name: str, unit: str) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteorološke varijable
            unit: Jedinica promenljive

        """
        ...

    @classmethod
    def from_dict(cls, id: int, name: str, unit: str) -> "TVariable":
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


class SourceDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    code: str
    name: str


class TSource(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Naziv izvora podataka

    Attrs:
        id: Identifikacioni broj (kluč)
        code: Kod (skraćeni naziv)
        name: Naziv izvora podataka

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    code: 'sqlalchemy.Column[str]'
    name: 'sqlalchemy.Column[str]'

    def __init__(self, id: int, code: str, name: str) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora podataka

        """
        ...

    @classmethod
    def from_dict(cls, id: int, code: str, name: str) -> "TSource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora podataka

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


class StationDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str
    type: str
    source_id: int
    location_id: int


class TStation(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Stanice za merenje

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv meteoroloških stanica
        type: Tip stanice
        source_id: ID izvora podataka
        location_id: ID lokacije

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    type: 'sqlalchemy.Column[str]'
    source_id: 'sqlalchemy.Column[int]'
    location_id: 'sqlalchemy.Column[int]'

    def __init__(self, id: int, name: str, type: str, source_id: int, location_id: int) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteoroloških stanica
            type: Tip stanice
            source_id: ID izvora podataka
            location_id: ID lokacije

        """
        ...

    @classmethod
    def from_dict(cls, id: int, name: str, type: str, source_id: int, location_id: int) -> "TStation":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteoroloških stanica
            type: Tip stanice
            source_id: ID izvora podataka
            location_id: ID lokacije

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


class MeasurementSourceDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str
    location_id: int
    source_id: int
    type: str


class TMeasurementSource(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Naziv izvora merenja

    Attrs:
        id: Identifikacioni broj (kluč)
        name: Naziv izvora merenja
        location_id: ID lokacije stanice
        source_id: ID izvora podataka
        type: Tip merenja

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    location_id: 'sqlalchemy.Column[int]'
    source_id: 'sqlalchemy.Column[int]'
    type: 'sqlalchemy.Column[str]'

    def __init__(self, id: int, name: str, location_id: int, source_id: int, type: str) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (kluč)
            name: Naziv izvora merenja
            location_id: ID lokacije stanice
            source_id: ID izvora podataka
            type: Tip merenja

        """
        ...

    @classmethod
    def from_dict(cls, id: int, name: str, location_id: int, source_id: int, type: str) -> "TMeasurementSource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (kluč)
            name: Naziv izvora merenja
            location_id: ID lokacije stanice
            source_id: ID izvora podataka
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
