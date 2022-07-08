from xml.etree.ElementTree import XMLParser


class ValueCubes:
    color_values = {'red': 0, 'green': 0, 'blue': 0}
    depth = 0

    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        self.color_values[attrib['color']] += self.depth

    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass            # We do not need to do anything with data.

    def close(self):    # Called when all data has been parsed.
        pass


vc = ValueCubes()
parser = XMLParser(target=vc)

with open("./cubes-pyramid.xml", "r") as f:
    xml_str = f.read()

parser.feed(xml_str)
parser.close()
print(vc.color_values['red'], vc.color_values['green'], vc.color_values['blue'])
