import pytest
from assignment import (
    append_hello_world,
    is_file_nonempty,
    count_lines,
    count_characters_excluding_spaces
)

@pytest.mark.parametrize("filename, content, expected_content", [
    ("test_append.txt", "example text ", "example text Hello, world!"),
    ("test_append2.txt", "", "Hello, world!")
])
def test1(filename, content, expected_content):
    with open(filename, "w") as f:
        f.write(content)
    
    append_hello_world(filename)
    
    with open(filename, "r") as f:
        result = f.read().strip()
    
    assert result == expected_content

@pytest.mark.parametrize("filename, content, expected_result", [
    ("test_nonempty1.txt", "this file is not empty", True),
    ("test_nonempty2.txt", "", False)
])
def test2(filename, content, expected_result):
    with open(filename, "w") as f:
        f.write(content)
    
    assert is_file_nonempty(filename) == expected_result

@pytest.mark.parametrize("filename, content, expected_count", [
    ("test_lines1.txt", "1st line\n2nd line\n3rd line\n4th line", 4),
    ("test_lines2.txt", "Single line", 1),
    ("test_lines3.txt", "", 0)
])
def test3(filename, content, expected_count):
    with open(filename, "w") as f:
        f.write(content)
    
    assert count_lines(filename) == expected_count

@pytest.mark.parametrize("filename, content, expected_count", [
    ("test_chars1.txt", "How many characters in here?", 24),
    ("test_chars2.txt", "Python 3.9!", 10),
    ("test_chars3.txt", "", 0)
])
def test4(filename, content, expected_count):
    with open(filename, "w") as f:
        f.write(content)
    
    assert count_characters_excluding_spaces(filename) == expected_count
