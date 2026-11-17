import os
import os.path as path

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:

        working_dir_path = path.abspath(working_directory)
        target_file = path.normpath(path.join(working_dir_path, file_path))

        valid_target = path.commonpath([working_dir_path, target_file]) == working_dir_path

        if valid_target == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            os.makedirs(path.split(target_file)[0], exist_ok = True)
            with open(target_file, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: "{e}"'
