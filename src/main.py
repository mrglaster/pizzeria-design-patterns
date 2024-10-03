import connexion

from src.modules.domain.report.report_format.report_format import ReportFormat

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


@app.route("/api/reports/range/<format>", methods=['GET'])
def get_report_range():
    pass

if __name__ == '__main__':
    app.add_api("swagger.yml")
    app.run(port=8080)
