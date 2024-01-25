from dip_connect.dip_conn import DIPConnect
import logging
from databricks.sdk import WorkspaceClient

logging.basicConfig(level="DEBUG")

WORKSPACE_URL = ""
dipc = DIPConnect(workspace_url=WORKSPACE_URL, profile="test")
dipc.connect()
w = WorkspaceClient(host=WORKSPACE_URL, profile="test")
for j in w.jobs.list():
    print(j)