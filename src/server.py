import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.provider.report_data.report_data_provider import ReportDataProvider
from src.modules.service.init_service.start_service import StartService

app = FastAPI()
start_service = StartService()
report_data_provider = ReportDataProvider()


@app.get("/api/reports/formats")
async def get_formats():
    report_formats = ReportFormat.__members__.keys()
    response = {"report_formats": [{"name": report_format, "value": index} for index, report_format in
                                   enumerate(report_formats)]}
    return JSONResponse(content=response)


@app.get("/api/reports/types")
async def get_report_types():
    return {"report_types": list(report_data_provider.repository_factory.repositories.keys())}


@app.get("/api/reports/{report_type}/{report_format}")
async def get_report(report_type: str, report_format: str):
    if not ReportDataProvider.is_valid_type(report_type) or not ReportDataProvider.is_valid_format(report_format):
        raise HTTPException(status_code=400, detail="Invalid report type or format")
    try:
        result = report_data_provider.get_requested_report(report_format=report_format, report_type=report_type)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating report: {e}")


def main():
    start_service.create()
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == '__main__':
    main()
