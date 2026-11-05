import os
import platform
from pathlib import Path
from typing import Union, List, Tuple
import ctypes

PathString = Union[str, Path]


def is_windows_os() -> bool:
    """Проверка что программа запущена на Windows"""
    pass


def validate_windows_path(path: PathString) -> Tuple[bool, str]:
    """Проверка корректности Windows пути"""
    pass

def format_size(size_bytes: int) -> str:
    """Форматирование размера файла в читаемом виде для Windows"""
    pass


def get_parent_path(path: PathString) -> str:
    """Получение родительского каталога с учетом Windows путей"""
    pass

def safe_windows_listdir(path: PathString) -> List[str]:
    """Безопасное получение содержимого каталога в Windows"""
    pass


def is_hidden_windows_file(path: PathString) -> bool:
    """Проверка является ли файл скрытым в Windows"""
    pass