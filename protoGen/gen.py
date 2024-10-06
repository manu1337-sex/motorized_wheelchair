import os
import subprocess

def protocify(directory, extension):
    current_working_dir = os.getcwd()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, current_working_dir)
                command = f'python -m grpc_tools.protoc -I=./api --python_out=./out --grpc_python_out=./out .\\{relative_path}'
                subprocess.run(command, shell=True)

directory = r".\api"
extension = ".proto"
protocify(directory, extension)

def fixer(directory, extension):
    current_working_dir = os.getcwd()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # :sob:
                updated_content = content.replace("import common_entities_pb2", "import prot.common_entities_pb2")
                updated_content = updated_content.replace("from game import ", "import prot.game.")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f'Replaced in: {file_path}')


directory = r".\out"
extension = ".py"
fixer(directory, extension)