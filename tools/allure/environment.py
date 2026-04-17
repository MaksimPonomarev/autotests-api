from config import settings
import sys
import platform

def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Собираем все элементы в единую строку с переносами
    items.extend([
        f'python_version={sys.version}',
        f'os_info={platform.system()}, {platform.release()}',
    ])
    properties = '\n'.join(items)



    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w', encoding='utf-8') as file:
        file.write(properties)  # Записываем переменные в файл
