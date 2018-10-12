from flask_restful import Resource
from models.ncer import NcerModel

ERROR_BLANK_PARAM = "'{}' cannot be blank."
ERROR_DUPLICATE_ENTRY = "'{}' cannot be blank."


class Ncer(Resource):
    @classmethod
    def get(cls, chrom: str, start: int, end: int):
        return {"ncer": [each.json() for each in NcerModel.get_percentile_for_range(chrom, start, end)]}, 200
