import subprocess
import sys
import os

def install_package():
    # Path to your package (setup.py directory)
    package_path = '.'

    # Change the current working directory to the package path
    os.chdir(package_path)

    # Run pip install in editable mode
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-e', '../../.'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'databricks-sdk'])


def run_example():
    from dip_connect.dip_conn import DIPConnect

    profile = "my_new_profile"
    dipc = DIPConnect(workspace_url="https://reglh-cyber.cloud.databricks.com/", setup_fl=False,profile=profile)
    dipc.connect()

    from databricks.sdk import WorkspaceClient
    w = WorkspaceClient(profile=profile)
    for j in w.jobs.list():
        print(j)

install_package()
run_example()