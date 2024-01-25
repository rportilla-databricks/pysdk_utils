import subprocess
import sys
import platform
import re

class DIPConnect:
    def __init__(self, workspace_url, profile : str = ""):
        # Initialize any required variables
        self.workspace_url = workspace_url
        self.profile = profile

    def __get_prefix(self):

        # Regex pattern
        pattern = r'https://([^\.]+)'

        # Search for the pattern
        match = re.search(pattern, self.workspace_url)

        # Extract the matched part
        if match:
            result = match.group(1)
            return(result)
        else:
            print("Workspace URL pattern not found")

    def authenticate(self):
	
        if platform.system() == "Windows":
          try:
            # Use 'where' command to find the binary path on Windows
            result = subprocess.run(['where', 'databricks.exe'], stdout=subprocess.PIPE, text=True, check=True)
            binary_path = result.stdout.strip()
          except subprocess.CalledProcessError:
            raise Exception("databricks.exe not found on Windows.")
        else:
          try:
            # Use 'which' command to find the binary path on Linux
            result = subprocess.run(['which', 'databricks'], stdout=subprocess.PIPE, text=True, check=True)
            binary_path = result.stdout.strip()
          except subprocess.CalledProcessError:
            raise Exception("databricks not found on Linux.")
    
        # Shell command for Databricks authentication
        result = subprocess.run([binary_path, "auth", "login", "--host", self.workspace_url, "--profile", self.profile], capture_output=True)
        if result.returncode != 0:
            raise Exception("Unable to login. " + result.stderr)

    def setup_profile(self):
        import os
        os.environ['DATABRICKS_CONFIG_PROFILE'] = self.profile
        print("Set up profile with name " + self.profile)

    def connect(self):
        self.authenticate()
        print(f"Profile before setup_profile: {self.profile}")  # Debug print
        self.setup_profile()
