from typing import Any, Dict, List
from pydantic import BaseModel

class Step(BaseModel):
    index: int = None
    value: int = None
    number_to_find: int = None
    found: bool
    left_pointer: int = None
    left_pointer_value: int = None
    right_pointer: int = None
    right_pointer_value: int = None
    num_dict: Dict[Any, Any] = None

class ArrayResponse(BaseModel):
    time_complexity: str
    space_complexity: str
    section: str = "arrays"
    question_link: str
    difficulty: str
    optimized: bool
    steps: List[Step]

class ArrayRequest(BaseModel):
    array1: List[int]
    array2: List[int] = None
    target: int = None

