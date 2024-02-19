import pytest
from main import StudentsInMLOps

@pytest.fixture
def ml_ops_class():
    return StudentsInMLOps()

def test_initial_total_strength(ml_ops_class):
    assert ml_ops_class.getTotalStrength() == 0

def test_enroll_students(ml_ops_class):
    ml_ops_class.enrollStudents(5)
    assert ml_ops_class.getTotalStrength() == 5

def test_drop_students(ml_ops_class):
    ml_ops_class.enrollStudents(10)
    ml_ops_class.dropStudents(3)
    assert ml_ops_class.getTotalStrength() == 7

def test_invalid_enrollment(ml_ops_class, capsys):
    ml_ops_class.enrollStudents(-5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid number of students to enroll."

def test_invalid_drop(ml_ops_class, capsys):
    ml_ops_class.enrollStudents(5)
    ml_ops_class.dropStudents(8)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid number of students to drop."

def test_get_class_name(ml_ops_class):
    assert ml_ops_class.getClassName() == "MLOps"
