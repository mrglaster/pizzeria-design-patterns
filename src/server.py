from datetime import datetime

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.report.report.base.abstract_report import PlainTextReport
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.dto.filter_dto import FilterDTO
from src.modules.dto.transactions_filter_dto import TransactionsFilterDTO
from src.modules.dto.turnovers_dto import TurnoversDTO
from src.modules.factory.process_factory.process_factory import ProcessFactory
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.provider.format.format_provider import FormatProvider
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


@app.get("/api/filtration/{domain_type}/{report_format}")
async def get_filtered_data(domain_type: str, report_format: str, filter_dto: FilterDTO):
    if not ReportDataProvider.is_valid_type(
            domain_type) or filter_dto is None or not ReportDataProvider.is_valid_format(report_format):
        raise HTTPException(status_code=400, detail=f"Unknown domain {domain_type}")
    prototype = DomainPrototype()
    prototype.create_from_repository(domain_type)
    for filtration_option in filter_dto.filters:
        prototype.filter_by(field_name=filtration_option.field_name,
                            filter_type=FilterType(filtration_option.filter_type),
                            value=filtration_option.field_value)
    report = ReportDataProvider.report_factory.get_report_class_instance(
        FormatProvider.get_format(format_data=report_format))
    report.create(prototype.get_data())
    if issubclass(report.__class__, PlainTextReport):
        result = report.get_result()
        return result
    return report.get_result_b64()


@app.post("/api/warehouse/transactions/{report_format}")
async def get_transactions(report_format: str, filter_dto: TransactionsFilterDTO):
    if not ReportDataProvider.is_valid_format(report_format):
        raise HTTPException(status_code=400, detail=f"Unknown report format {report_format}")
    prototype = DomainPrototype().create_from_repository('storage_transaction')
    report = ReportDataProvider.report_factory.get_report_class_instance(
        FormatProvider.get_format(format_data=report_format))

    if not filter_dto or (not filter_dto.storage and not filter_dto.nomenclature):
        report.create(prototype.get_data())
        if issubclass(report.__class__, PlainTextReport):
            result = report.get_result()
            return result
        return report.get_result_b64()
    try:
        if filter_dto.storage:
            for i in filter_dto.storage.keys():
                if not i.endswith("_ft"):
                    ft = FilterType(filter_dto.storage[f'{i}_ft']) if filter_dto.storage[f'{i}_ft'] else FilterType.LIKE
                    prototype = prototype.filter_by(field_name=f'storage|{i}', value=filter_dto.storage[i],
                                                    filter_type=ft)
        if filter_dto.nomenclature:
            for i in filter_dto.storage.keys():
                if not i.endswith("_ft"):
                    ft = FilterType(filter_dto.storage[f'{i}_ft']) if filter_dto.storage[f'{i}_ft'] else FilterType.LIKE
                    prototype = prototype.filter_by(field_name=f'nomenclature|{i}', value=filter_dto.storage[i],
                                                    filter_type=ft)
        report.create(prototype.get_data())
        if issubclass(report.__class__, PlainTextReport):
            result = report.get_result()
            return result
        return report.get_result_b64()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'bad request: {e}')


@app.post("/api/warehouse/turnovers/{report_format}")
def get_warehouse_turnovers(report_format: str, request_dto: TurnoversDTO):
    if not ReportDataProvider.is_valid_format(report_format):
        raise HTTPException(status_code=400, detail=f"Unknown report format {report_format}")
    try:
        begin_date = datetime.strptime(str(request_dto.begin_date), "%Y-%m-%d %H:%M:%S.%f")
        end_date = datetime.strptime(str(request_dto.end_date), "%Y-%m-%d %H:%M:%S.%f")
        prototype = DomainPrototype().create_from_repository('storage_transaction')
        prototype = prototype.filter_by(field_name='transaction_time', filter_type=FilterType.LESS_THAN,
                                        value=end_date).filter_by(field_name='transaction_time',
                                                                              filter_type=FilterType.GREATER_THAN,
                                                                              value=begin_date)
        if request_dto.storage:
            for i in request_dto.storage.keys():
                if not i.endswith("_ft"):
                    ft = FilterType(request_dto.storage[f'{i}_ft']) if request_dto.storage[
                        f'{i}_ft'] else FilterType.LIKE
                    prototype = prototype.filter_by(field_name=f'storage|{i}', value=request_dto.storage[i],
                                                    filter_type=ft)
        if request_dto.nomenclature:
            for i in request_dto.storage.keys():
                if not i.endswith('_ft'):
                    ft = FilterType(request_dto.storage[f'{i}_ft']) if request_dto.storage[
                        f'{i}_ft'] else FilterType.LIKE
                    prototype = prototype.filter_by(field_name=f'nomenclature|{i}', value=request_dto.storage[i],
                                                    filter_type=ft)
        process_factory = ProcessFactory()
        data =  list(prototype.get_data())
        if not data:
            return {}
        turns = process_factory.execute_process("storage_turnover", data)
        report = ReportDataProvider.report_factory.get_report_class_instance(
            FormatProvider.get_format(format_data=report_format))
        report.create(turns)
        if issubclass(report.__class__, PlainTextReport):
            result = report.get_result()
            return result
        return report.get_result_b64()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'bad request: {e}')


def main():
    start_service.create()
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == '__main__':
    main()
