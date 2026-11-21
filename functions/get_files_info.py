import os
import os.path as path

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:

        working_dir_path = path.abspath(working_directory)
        target_dir = path.normpath(path.join(working_dir_path, directory))

        valid_target_dir = path.commonpath([working_dir_path, target_dir]) == working_dir_path

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside  the permitted working directory'
        elif not path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            result = "Result for current directory:"
            for file in os.listdir(target_dir):
                result += f"\n  - {file}: file_size={path.getsize(path.join(target_dir, file))} bytes, is_dir={path.isdir(path.join(target_dir, file))}"

            return result

    except Exception as e:
          return f'Error: "{e}"'
