import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    Exercise, GetExerciseResponseSchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(
        actual: CreateExerciseResponseSchema,
        expected: CreateExerciseRequestSchema
):
    """
    Функция проверяет соответствие полей в запросе и ответе при создании задания
    :param actual: CreateExerciseResponseSchema
    :param expected: CreateExerciseRequestSchema
    """
    logger.info("Check create exercise response")
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")


@allure.step("Check exercise")
def assert_exercise(actual: Exercise, expected: Exercise):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.
    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение задания соответствует ответам на их создание.
    :param get_exercise_response: GetExerciseResponseSchema
    :param create_exercise_response: CreateExerciseResponseSchema
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get exercise response")
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


@allure.step("Check update exercise response")
def assert_update_exercise_response(
        actual: GetExerciseResponseSchema,
        expected: UpdateExerciseRequestSchema
):
    """
    Функция для проверки данных задания в запросе на обновление и ответе на него
    :param actual: GetExerciseResponseSchema
    :param expected: UpdateExerciseRequestSchema
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info("Check update exercise response")
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.
    :param actual: Фактический ответ API с внутренней ошибкой.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    logger.info("Check exercise not found response")
    assert_internal_error_response(actual, expected)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет, что тело ответа на запрос содержит список ранее созданных заданий
    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercise_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    logger.info("Check get exercises response")
    assert_length(create_exercise_responses, get_exercises_response.exercises, "exercises")
    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)







