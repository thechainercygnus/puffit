import os

from rich import print

from src.pft.generator import ProjectGenerator
from src.pft.parser import TemplateParser

for template in os.listdir('templates'):
     if template.endswith('.pft'):
        template_path = os.path.join('templates', template)
        print(f"Parsing {template}")
        p = TemplateParser(template_path)
        g = ProjectGenerator(p.directory_structure)
        g.create_scaffold('sample_out')