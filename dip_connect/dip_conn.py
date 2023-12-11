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
        auth_command = "{} auth login --host {}".format(binary_path, self.workspace_url)

        try:
            # Choose the right module based on the OS
            if platform.system() == 'Windows':
                import wexpect as expect
            else:
                import pexpect as expect

            # Start the command with pexpect
            child = expect.spawn(auth_command)

            # Wait for the prompt where the profile needs to be entered
            # Note: Replace 'Prompt text' with the actual text that the command
            # prompts you with before you need to enter the profile name
            # Send the profile name
            prefix = self.__get_prefix()
            if len(self.profile) > 0:
                for l in prefix:
                    child.send('\b')
                child.sendline(self.profile)

            else:
                self.profile = prefix
                print(f"Profile set in authenticate: {self.profile}")  # Debug print
                child.sendline('\n')

            # Optional: Wait for any follow-up prompts and send responses in a similar way
            # child.expect('Next prompt text')
            # child.sendline('response to next prompt')

            # Wait for the command to complete
            child.expect(expect.EOF)

            platform_name = platform.system()
            print('platform is' + platform_name)
 
            if platform_name == "Windows":
              stdout = child.before
            else:
              # linux
              stdout = child.before.decode()

            if stdout:
                print("Authentication successful.")
            else:
                print("Authentication unsuccessful or no output.")

        except expect.ExceptionPexpect as e:
            # Handle errors in the authentication process
            print(f"An error occurred during authentication: {e}")

    def setup_profile(self):
        import os
        os.environ['DATABRICKS_CONFIG_PROFILE'] = self.profile
        print("Set up profile with name " + self.profile)

    def connect(self):
        self.authenticate()
        print(f"Profile before setup_profile: {self.profile}")  # Debug print
        self.setup_profile()
