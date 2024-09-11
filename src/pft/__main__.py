import argparse
from pathlib import Path

from .generator import ProjectGenerator
from .parser import TemplateParser


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Generate a project scaffold based on a *.pft template."
    )
    parser.add_argument("template", type=str, help="Path to the *.pft template file")

    # Parse the arguments
    args = parser.parse_args()

    # Parse the template file
    template_parser = TemplateParser(args.template)

    # Generate the project scaffold
    project_generator = ProjectGenerator(template_parser.directory_structure)
    base_path = Path.cwd()  # Or any other base path you want to use
    project_generator.create_scaffold(base_path)

    print(f"Project scaffold generated in {base_path}")


if __name__ == "__main__":
    main()
