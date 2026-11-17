import os
import subprocess
import os.path as path

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:

        working_dir_path = path.abspath(working_directory)
        target_file = path.normpath(path.join(working_dir_path, file_path))

        valid_target = path.commonpath([working_dir_path, target_file]) == working_dir_path

        if valid_target == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", target_file]
            if args != None:
                command.extend(args)
            result = subprocess.run(
                command,
                cwd = working_dir_path,
                capture_output = True,
                text = True,
                timeout = 30)
            result_string = ""
            if result.returncode != 0:
                result_string += f"Process exited with code {result.returncode}"
            if result.stdout == None and result.stderr == None:
                result_string += "No output produced"
            else:
                if result.stdout != None:
                    result_string += f"STDOUT: {result.stdout}"
                if result.stderr != None:
                    result_string += f"STDERR: {result.stderr}"
            return result_string
    
    except Exception as e:
        return f'Error: "{e}"'
