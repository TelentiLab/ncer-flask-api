from typing import Dict, Union, List
from sqlalchemy import and_
import math
from db import db

NcerJSON = Dict[str, Union[int, str]]


class NcerModel(db.Model):
    __tablename__ = "ncer"

    id = db.Column(db.Integer, primary_key=True)
    chrom = db.Column(db.String(8), nullable=False)
    start = db.Column(db.Integer, nullable=False)
    end = db.Column(db.Integer, nullable=False)
    percentile = db.Column(db.String(10), nullable=False)

    def json(self) -> NcerJSON:
        return {
            "id": self.id,
            "chrom": self.chrom,
            "start": self.start,
            "end": self.end,
            "percentile": self.percentile,
        }

    @classmethod
    def get_percentile_for_range(cls, chrom: str, start: int, end: int) -> List["NcerModel"]:
        start_pos = math.floor(start / 10) * 10
        end_pos = math.ceil(end / 10) * 10
        return cls.query.filter(and_(cls.start >= start_pos, cls.end <= end_pos, cls.chrom == chrom)).all()

    @classmethod
    def get_percentile(cls, chrom: str, start: int, end: int) -> "NcerModel":
        return cls.query.filter(and_(cls.start == start, cls.end == end, cls.chrom == chrom)).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
