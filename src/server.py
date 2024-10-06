import connexion
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.provider.report_data.report_data_provider import ReportDataProvider
from src.modules.service.init_service.start_service import StartService

app = connexion.FlaskApp(__name__)
start_service = StartService()
report_data_provider = ReportDataProvider()


@app.route("/api/reports/formats", methods=["GET"])
def get_formats():
    report_formats = ReportFormat.__members__.keys()
    response = {"report_formats": []}
    cntr = 1
    for report_format in report_formats:
        response['report_formats'].append({"name": report_format, "value": cntr})
        cntr += 1
    return response


@app.route("/api/reports/types", methods=["GET"])
def get_report_types():
    return {"report_types": list(report_data_provider.report_factory.repositories.keys())}


@app.route("/api/reports/<report_type>/<report_format>")
def get_report(report_type: str, report_format: str):
    if report_format is None or not ReportDataProvider.is_valid_type(report_type):
        return "Invalid format", 400
    try:
        result = report_data_provider.get_requested_report(report_format=report_format, report_type=report_type)
        return result
    except Exception as e:
        return f"{e}", 400


def main():
    start_service.create()
    app.add_api("swagger.yml")
    app.run(port=8080)


if __name__ == '__main__':
    main()
