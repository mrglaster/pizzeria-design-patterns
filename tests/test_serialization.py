import json
from unittest import TestCase
from src.modules.factory.convertion_factory.converter_factory import ConverterFactory


class TestConverters(TestCase):
    class Person:
        def __init__(self, name, diploma):
            self.name = name
            self.diploma = diploma

    class Diploma:
        def __init__(self, id, given_date, stamp):
            self.id = id
            self.given_date = given_date
            self.stamp = stamp

    class Stamp:
        def __init__(self, organization, id):
            self.organization = organization
            self.id = id

    class Organization:
        def __init__(self, name):
            self.name = name

    def test_nested_json(self):
        organization = self.Organization("University")
        stamp = self.Stamp(organization, 123)
        diploma = self.Diploma("D-12345", "2023-05-01", stamp)
        person = self.Person("Alice", diploma)
        a = {"a": [person]}
        factory = ConverterFactory()
        result = factory.serialize(a, 'json')
        expected= """{"a": [{"name": "Alice","diploma": {"id": "D-12345","given_date": "2023-05-01","stamp": {"organization": {"name": "University"},"id": 123}}}]}"""
        assert json.loads(expected) == json.loads(result)

    def test_nested_xml(self):
        organization = self.Organization("University")
        stamp = self.Stamp(organization, 123)
        diploma = self.Diploma("D-12345", "2023-05-01", stamp)
        person = self.Person("Alice", diploma)
        a = {"a": [person]}
        factory = ConverterFactory()
        result = factory.serialize(a, 'xml')
        expected = """<?xml version="1.0" ?>
<dict>
  <a>
    <item>
      <name>Alice</name>
      <diploma>
        <id>D-12345</id>
        <given_date>2023-05-01</given_date>
        <stamp>
          <organization>
            <name>University</name>
          </organization>
          <id>123</id>
        </stamp>
      </diploma>
    </item>
  </a>
</dict>
"""
        assert result == expected

