import xml.etree.ElementTree as ET
from xml.dom import minidom


class XMLEncoder:
    def encode(self, obj):
        root = ET.Element(self._get_element_name(obj))
        self._build_xml(obj, root)
        return self._prettify(root)

    def _build_xml(self, obj, parent):
        if isinstance(obj, dict):
            for key, value in obj.items():
                processed_key = self._process_key(key)
                child = ET.SubElement(parent, processed_key)
                self._build_xml(value, child)
        elif hasattr(obj, '__dict__'):
            for key, value in obj.__dict__.items():
                processed_key = self._process_key(key)
                child = ET.SubElement(parent, processed_key)
                self._build_xml(value, child)
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                child = ET.SubElement(parent, "item")
                self._build_xml(item, child)
        else:
            parent.text = str(obj)

    def _process_key(self, key):
        if '__' in key:
            key = key.split('__', 1)[1]
        return key.lstrip('_')

    def _get_element_name(self, obj):
        if hasattr(obj, '__class__'):
            return obj.__class__.__name__
        return str(obj)

    def _prettify(self, elem):
        rough_string = ET.tostring(elem, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(XMLEncoder, cls).__new__(cls)
        return cls.instance
