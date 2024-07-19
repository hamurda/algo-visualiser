from fastapi import APIRouter
import copy
from ...models.arrays.arrays_models import ArrayResponse, Step, ArrayRequest

router = APIRouter(
    prefix="/arrays",
    tags=["arrays"]
)


# Two Sum problem, give indices of 2 numbers that add up to target value
# Time complexity: O(n^2), Space complexity: O(1)
@router.post("/twosum", response_model=ArrayResponse)
def get_two_sum_problem_brute_force(params: ArrayRequest) -> ArrayResponse:
	resp = ArrayResponse(
		time_complexity="O(n^2)",
		space_complexity="O(1)",
		question_link="https://leetcode.com/problems/two-sum/description/",
		difficulty="easy",
		optimized= False,
		steps=[],
    )
	numbers=params.array1
	target=params.target
	
	for (idx1, num1) in enumerate(numbers):
		for (idx2, num2) in enumerate(numbers[idx1+1:], idx1+1):
			step = Step(
				left_pointer = idx1,
				left_pointer_value = num1,
				right_pointer = idx2,
				right_pointer_value = num2,
				found = False,
            )
			
			if num1+num2 == target:
				step.found = True
				resp.steps.append(step)
				return (resp)
			resp.steps.append(step)
	
	return resp

# Time complexity: O(n), Space complexity: O(n)
@router.post("/twosumopt", response_model= ArrayResponse)
def get_two_sum_optimized(params: ArrayRequest) -> ArrayResponse:
	resp = ArrayResponse(
		time_complexity="O(n)",
		space_complexity="O(n)",
		question_link="https://leetcode.com/problems/two-sum/description/",
		difficulty="easy",
		optimized= True,
		steps=[],
    )
	numbers=params.array1
	target=params.target
	
	nums_map = {}
	for (idx, num) in enumerate(numbers):
		number_to_find = target-num
		step = Step(
				found = False,
				index = idx,
				value = num,
				number_to_find = number_to_find,
				num_dict = copy.deepcopy(nums_map)
        )
		
		if number_to_find in nums_map:
			step.found = True
			resp.steps.append(step)
			# return (nums_map[number_to_find], idx)
			return (resp)
		else:
			nums_map[num] = idx
			step.num_dict[num] = idx
			
		resp.steps.append(step)

	return resp


@router.get("/")
def read_root():
    return {"Hello": "World"}