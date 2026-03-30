from pydantic import BaseModel, ConfigDict, Field

from lesson6.tools.fakers import fake


class Exercise(BaseModel):
    """
    Описание структуры задания
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий
    """
    exercises: list[Exercise]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение задания
    """
    exercise: Exercise

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str  = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4, alias="courseId")
    max_score: int = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int = Field(default_factory=fake.min_score, alias="minScore")
    order_index: int = Field(default_factory=fake.integer, alias="orderIndex")
    description: str  = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time, alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание задания
    """
    exercise: Exercise


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str  = Field(default_factory=fake.sentence)
    max_score: int = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int = Field(default_factory=fake.min_score, alias="minScore")
    order_index: int = Field(default_factory=fake.integer, alias="orderIndex")
    description: str  = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time, alias="estimatedTime")

