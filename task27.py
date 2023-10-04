
# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from pathlib import Path

__all__ = ['group_rename_files']

def group_rename_files(new_name: str, ext_renamed: str, /, count_dig: int = 3, ext_new: str = None,
                       saved_range: range = (3, 6), path: str = None) -> int:
    
    if ext_new is None:  
        ext_new = ext_renamed
    work_path = Path.cwd() if path is None else Path(path)
    count_renamed = 0
    for p in work_path.iterdir():
        if p.is_file() and p.suffix == ext_renamed:
            file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{count_renamed:03}{ext_new}"
            p.rename(Path(p.parent,  file_name))
            count_renamed += 1

    return count_renamed

if __name__ == '__main__':
    group_rename_files("nnt", ".txt")