from yaml import YAMLObject, Loader, Dumper
from pathlib import Path

file_str = "/Users/antonvopilov/Google-Drive/Projects/mkdocs-template/mkdocs.yml"


class MyYAMLObject(YAMLObject):
    yaml_loader = Loader
    yaml_dumper = Dumper

    yaml_tag = u'...'
    yaml_flow_style = ...

    @classmethod
    def from_yaml(cls, loader, node):
        # return data
        pass

    @classmethod
    def to_yaml(cls, dumper, data):
        # ...
        # return node
        pass


