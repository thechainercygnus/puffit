import pytest

from src.puffit.generator import ProjectGenerator


@pytest.fixture
def sample_structure():
    return {"dir1": {"file1.txt": None, "dir2": {"file2.txt": None}}, "file3.txt": None}


def test_projectgenerator_initialization(sample_structure):
    generator = ProjectGenerator(sample_structure)
    assert generator.directory_structure == sample_structure


def test_create_scaffold_creates_structure(tmp_path, sample_structure):
    generator = ProjectGenerator(sample_structure)

    # Call the method to create the structure in the tmp_path
    generator.create_scaffold(tmp_path)

    # Assert the directories and files exist
    assert (tmp_path / "dir1").is_dir()
    assert (tmp_path / "dir1" / "file1.txt").is_file()
    assert (tmp_path / "dir1" / "dir2").is_dir()
    assert (tmp_path / "dir1" / "dir2" / "file2.txt").is_file()
    assert (tmp_path / "file3.txt").is_file()


def test_create_scaffold_handles_empty_structure(tmp_path):
    generator = ProjectGenerator({})

    # Call the method to create the structure in the tmp_path
    generator.create_scaffold(tmp_path)

    # Since the structure is empty, no directories or files should be created
    assert len(list(tmp_path.iterdir())) == 0


def test_create_scaffold_with_custom_structure(tmp_path):
    custom_structure = {"custom_dir": {"custom_file.txt": None}}

    generator = ProjectGenerator(custom_structure)

    # Call the method with custom structure
    generator.create_scaffold(tmp_path)

    assert (tmp_path / "custom_dir").is_dir()
    assert (tmp_path / "custom_dir" / "custom_file.txt").is_file()
