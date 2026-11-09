import os
import platform
from pathlib import Path
from typing import Union, List, Tuple
import ctypes

PathString = Union[str, Path]


def is_windows_os() -> bool:
    """Проверка что программа запущена на Windows"""

    os_name = platform.system()
    if os_name == 'Windows':
        return True
    else:
        return False


def validate_windows_path(path: PathString) -> Tuple[bool, str]:
    """Проверка корректности Windows пути"""

    list_error = []
    error = ""
    not_prohibited_characters = True
    exists = True
    length_path = True
    prohibited_characters = ["/", ":", "*", "?", '"', "<", ">", "|"]

    if not isinstance(path, (Path, str)):
        return False, "некорректный тип пути"

    path_string = str(path)

    drive, tail = os.path.splitdrive(path_string)

    if len(path_string) > 260:
        length_path = False
        error = "слишком длинный путь"
        list_error.append(error)

    for ch in prohibited_characters:
        if ch in tail:
            not_prohibited_characters = False

    if not not_prohibited_characters:
        error = "путь с файлом содержит недопустимые символы"
        list_error.append(error)

    if drive:
        if len(drive) != 2 or not drive[0].isalpha() or drive[1] != ":":
                error = "путь с файлом содержит недопустимые символы"
                not_prohibited_characters = False
                list_error.append(error)

    if not os.path.exists(path):
        exists = False
        error = "путь не найден"
        list_error.append(error)

    valid = not_prohibited_characters and length_path and exists

    return valid, "; ".join(list_error)


def format_size(size_bytes: int) -> str:
    """Форматирование размера файла в читаемом виде для Windows"""

    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes >= 1024:
        size = round((size_bytes / 1024), 1)

        if size < 1024:
            return f"{size} KB"
        else:
            size = round((size / 1024), 1)

            if size < 1024:
                return f"{size} MB"
            else:
                return f"{round((size / 1024), 1)} GB"


def get_parent_path(path: PathString) -> str:
    """Получение родительского каталога с учетом Windows путей"""

    drive, tail = os.path.splitdrive(path)

    if path == drive:
        return path
    else:
        return os.path.dirname(path)

def safe_windows_listdir(path: PathString) -> List[str]:
    """Безопасное получение содержимого каталога в Windows"""

    try:
        return os.listdir(path)
    except FileNotFoundError:
        return []
    except PermissionError:
        return []
    except OSError:
        return []


def is_hidden_windows_file(path: PathString) -> bool:
    """Проверка является ли файл скрытым в Windows"""

    kernel32 = ctypes.windll.kernel32
    get_file_attributes = kernel32.GetFileAttributesW

    path = str(path)

    attributes = get_file_attributes(path)

    if attributes == 0xFFFFFFFF or attributes == -1:
        return False

    if attributes & 2 == 0:
        return False
    else:
        return True