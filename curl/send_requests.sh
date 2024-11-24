#!/bin/bash

# GET /api/reports/formats
curl -X GET http://127.0.0.1:8080/api/reports/formats

# GET /api/reports/types
curl -X GET http://127.0.0.1:8080/api/reports/types

# POST /api/configuration/dump/save
curl -X POST http://127.0.0.1:8080/api/configuration/dump/save

# POST /api/configuration/dump/load
curl -X POST http://127.0.0.1:8080/api/configuration/dump/load

# GET /api/reports/nomenclature/FORMAT_CSV
curl -X GET http://127.0.0.1:8080/api/reports/nomenclature/FORMAT_CSV

# GET /api/warehouse/transactions/FORMAT_JSON
curl -X GET http://127.0.0.1:8080/api/warehouse/transactions/FORMAT_JSON

# PUT /api/nomenclature/put/
curl -X PUT http://127.0.0.1:8080/api/nomenclature/put/ \
-H "Content-Type: application/json" \
-d '{
  "nomenclature": {
    "name": "DEMO NOM",
    "uid": "ea091763-8c64-4873-9d70-f1de3d0fa90d",
    "full_name": "FULL_NAME",
    "nomenclature_group": {
      "name": "ингредиент",
      "uid": "1dc65ce8-354b-41d2-9648-b86a8f8fd150"
    },
    "measurement_unit": {
      "name": "г",
      "uid": "935134fb-92df-4817-a1a5-a26db39e4e34",
      "unit": 1,
      "base_measurement_unit": null
    }
  }
}'

# PATCH /api/nomenclature/update
curl -X PATCH http://127.0.0.1:8080/api/nomenclature/update \
-H "Content-Type: application/json" \
-d '{
  "uid": "ea091763-8c64-4873-9d70-f1de3d0fa90d",
  "nomenclature": {
    "name": "DEMO NOM ALT",
    "uid": "ea091763-8c64-4873-9d70-f1de3d0fa90d",
    "full_name": "FULL_NAME",
    "nomenclature_group": {
      "name": "ингредиент",
      "uid": "1dc65ce8-354b-41d2-9648-b86a8f8fd150"
    },
    "measurement_unit": {
      "name": "г",
      "uid": "935134fb-92df-4817-a1a5-a26db39e4e34",
      "unit": 1,
      "base_measurement_unit": null
    }
  }
}'

# DELETE /api/nomenclature/delete/ea091763-8c64-4873-9d70-f1de3d0fa90d
curl -X DELETE http://127.0.0.1:8080/api/nomenclature/delete/ea091763-8c64-4873-9d70-f1de3d0fa90d

# GET /api/reports/measurement_unit/7
curl -X GET http://127.0.0.1:8080/api/reports/measurement_unit/7

# GET /api/reports/measurement_unit/1
curl -X GET http://127.0.0.1:8080/api/reports/measurement_unit/1

# POST /api/configuration/blocking/date/set
curl -X POST http://127.0.0.1:8080/api/configuration/blocking/date/set

# GET /api/configuration/blocking/date/get
curl -X GET http://127.0.0.1:8080/api/configuration/blocking/date/get

# GET /api/warehouse/turnovers/inrange/FORMAT_JSON
curl -X GET http://127.0.0.1:8080/api/warehouse/turnovers/inrange/FORMAT_JSON
