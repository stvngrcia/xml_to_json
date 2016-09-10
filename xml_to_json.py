import json
import sys
import xmltodict
"""
    - This class takes the name of an xml file. Then it creates or opens a
        file with the same name, but with the extension .json where the results
        will be stored. It first converts the xml file to a dictionary and
        converts the dictionary in to a json.
    - Sources:
    https://github.com/martinblech/xmltodict
    https://pythonadventures.wordpress.com/2014/12/29/xml-to-dict-xml-to-json/
"""


class to_json():
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.xml_attribs = True

# receiving the name of the file and the a True flag to process name spaces
    def convert(self):
        # Opening / creating a json file to store the conversion reults
        file_json = open(self.xml_file+".json", 'w')

        try:
            # Opening the xml file with read binary format
            file_xml = open(self.xml_file, "rb")
        except:
            return "File does not exist"

        # Converting the xml file contentents into json
        with file_xml as files:
            try:
                # First converting the xml file to a dictionary
                data = xmltodict.parse(files, xml_attribs=True)
            except:
                return "xml file format is invalid"
            # Converting to json and formatting it
            xml_contents = json.dumps(data, indent=4)

        # writing the xml into the json file
        file_json.write(xml_contents)

        # Closing files
        file_json.close()
        file_xml.close()
        return True

if __name__ == '__main__':
    # Sending the name of the file
    to_json(sys.argv[1]).convert()
