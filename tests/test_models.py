"""Test the models."""

from dataclasses import dataclass
from enum import StrEnum

from tomtom_apis.api import BaseParams


class Choice(StrEnum):
    """Test enum."""

    NO = "No"
    YES = "Yes"


@dataclass(kw_only=True)
class ParamsTest(BaseParams):
    """Test params."""

    field1: int | None = None
    field2: str | None = None
    field3: bool | None = None
    field4: float | None = None
    field5: list[str] | None = None  # Adding a list of strings
    field6: list[int] | None = None  # Adding a list of integers
    field7: Choice | None = None


def test_to_dict_all_fields_set() -> None:
    """Test to_dict method when all fields are set."""
    params = ParamsTest(field1=123, field2="test", field3=True, field4=45.67, field5=["a", "b", "c"], field6=[1, 2, 3], field7=Choice.YES)
    expected = {
        "field1": "123",
        "field2": "test",
        "field3": "true",
        "field4": "45.67",
        "field5": "a,b,c",  # List of strings converted to comma-separated string
        "field6": "1,2,3",  # List of integers converted to comma-separated string
        "field7": "Yes",
    }
    assert params.to_dict() == expected


def test_to_dict_some_fields_none() -> None:
    """Test to_dict method when some fields are None."""
    params = ParamsTest(field1=123, field2=None, field3=False, field4=None, field5=["x", "y"], field6=None, field7=None)
    expected = {"field1": "123", "field3": "false", "field5": "x,y"}
    assert params.to_dict() == expected


def test_to_dict_all_fields_none() -> None:
    """Test to_dict method when all fields are None."""
    params = ParamsTest(field1=None, field2=None, field3=None, field4=None, field5=None, field6=None, field7=None)
    expected: dict = {}
    assert params.to_dict() == expected


def test_to_dict_mixed_types_with_none() -> None:
    """Test to_dict method when some fields are None and others have different types."""
    params = ParamsTest(field1=None, field2="example", field3=None, field4=99.99, field5=["item1"], field6=[10, 20], field7=Choice.NO)
    expected = {"field2": "example", "field4": "99.99", "field5": "item1", "field6": "10,20", "field7": "No"}
    assert params.to_dict() == expected


def test_to_dict_empty_list() -> None:
    """Test to_dict method when a field is an empty list."""
    params = ParamsTest(field1=456, field2="test2", field3=False, field4=12.34, field5=[], field6=[], field7=Choice.NO)
    expected = {"field1": "456", "field2": "test2", "field3": "false", "field4": "12.34", "field7": "No"}
    assert params.to_dict() == expected


def test_to_dict_single_item_list() -> None:
    """Test to_dict method when a field is a list with one item."""
    params = ParamsTest(field1=789, field2="test3", field3=True, field4=56.78, field5=["single"], field6=[42])
    expected = {"field1": "789", "field2": "test3", "field3": "true", "field4": "56.78", "field5": "single", "field6": "42"}
    assert params.to_dict() == expected
