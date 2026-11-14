import os.path as path

def get_files_info(working_directory: str, directory, str = ".") -> str:
    try:

        working_dir_path = path.abspath(working_directory)
        target_dir = path.normpath(path.join(working_dir_path, directory))

        valid_target_dir = path.commonpath([working_dir_path, target_dir]) == working_dir_path

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside  the permitted working directory'
        elif not path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        else:
            return f'Success: "{directory}" is within the working directory'

    except Execption as e:
          return f'Error: "{e}"'
