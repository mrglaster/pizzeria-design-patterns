import json

import connexion

from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.factory.object_factory.object_factory import ObjectFactory
from src.modules.factory.report_factory.report_factory import ReportFactory
from src.modules.repository.measurment_unit_repository import MeasurementUnitRepository

app = connexion.FlaskApp(__name__)


@app.route("/api/reports/report_formats", methods=["GET"])
def get_formats():
    report_formats = ReportFormat.__members__.keys()
    response = {"report_formats": []}
    cntr = 1
    for report_format in report_formats:
        response['report_formats'].append({"name": report_format, "value": cntr})
        cntr += 1
    return response


if __name__ == '__main__':
    app.add_api("swagger.yml")
    app.run(port=8080)
