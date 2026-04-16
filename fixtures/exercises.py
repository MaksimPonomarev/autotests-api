import pytest
from pydantic import BaseModel
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(function_user: UserFixture, function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    course_id = function_course.response.course.id
    request = CreateExerciseRequestSchema(course_id=course_id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)


