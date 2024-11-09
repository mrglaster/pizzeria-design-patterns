from dataclasses import dataclass


@dataclass
class TransactionsFilterDTO:
    storage: dict
    nomenclature: dict
