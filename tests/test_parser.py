import pytest

from puffit.parser import TemplateParser


@pytest.fixture
def sample_template():
    return """\
    dir1/
        file1.txt
        dir2/
            file2.txt
    """


def test_templateparser_initialization(sample_template):
    parser = TemplateParser(sample_template)

    assert isinstance(parser, TemplateParser)
    assert (
        parser._original
        == "    dir1/\n        file1.txt\n        dir2/\n            file2.txt\n"
    )
    assert len(parser._original_lines) == 4


def test_clean_input_removes_comments():
    template = """dir1/ # This is a comment
    file1.txt // Another comment
    """
    parser = TemplateParser(template)
    cleaned = parser._clean_input(template)

    expected_output = "dir1/\n    file1.txt\n"
    assert cleaned == expected_output


def test_build_directory_structure(sample_template):
    parser = TemplateParser(sample_template)
    structure = parser.directory_structure

    expected_structure = {"dir1/": {"file1.txt": None, "dir2/": {"file2.txt": None}}}
    assert structure == expected_structure


def test_get_line_type():
    assert TemplateParser._get_line_type("dir1/") == "D"
    assert TemplateParser._get_line_type("file.txt") == "F"


def test_generate_line_symbol_matrix(sample_template):
    parser = TemplateParser(sample_template)
    assert parser.line_symbol_matrix == (
        "IIIIDDDDD",
        "IIIIIIIIFFFFFFFFF",
        "IIIIIIIIDDDDD",
        "IIIIIIIIIIIIFFFFFFFFF",
    )  # Expected line symbol matrix from the input


def test_generate_line_indent_matrix(sample_template):
    parser = TemplateParser(sample_template)
    assert parser.line_indent_matrix == ("IIII", "IIIIIIII", "IIIIIIII", "IIIIIIIIIIII")


def test_indent_size_error():
    with pytest.raises(Exception, match="Indent Size Error"):
        TemplateParser("dir1/\nfile1.txt")  # No indentation present
