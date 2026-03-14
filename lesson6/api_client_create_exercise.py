from lesson6.clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from lesson6.clients.exercises.exercises_client import ExercisesClient, CreateExerciseRequestDict, get_exercises_client
from lesson6.clients.files.files_client import get_files_client, CreateFileRequestDict
from lesson6.clients.private_http_builder import AuthenticationUserDict
from lesson6.clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from lesson6.tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

#Создаем задание для курса
create_exercise_client = get_exercises_client(authentication_user)
create_exercise_request = CreateExerciseRequestDict(
    title = "Lesson5",
    courseId = create_course_response["course"]["id"],
    maxScore = 0,
    minScore = 0,
    orderIndex = 0,
    description = "string",
    estimatedTime = "string"
)

create_exercise_response = create_exercise_client.create_exercise(create_exercise_request)
print("Create exercise data: ", create_exercise_response)