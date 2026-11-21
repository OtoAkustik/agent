from config import MAX_CHARS
import os.path as path

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Gets the content of a specified file and returns it as text", 
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of file to return content from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:

        working_dir_path = path.abspath(working_directory)
        target_file = path.normpath(path.join(working_dir_path, file_path))

        valid_target = path.commonpath([working_dir_path, target_file]) == working_dir_path

        if valid_target == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            content = ""
            with open(target_file, "r") as f:
                content += f.read(MAX_CHARS)
                print(content)
                if f.read(1):
                    content += f'...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content

    except Exception as e:
          return f'Error: "{e}"'
