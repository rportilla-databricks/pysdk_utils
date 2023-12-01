# test_my_class.py

import unittest
from dip_connect.dip_conn import DIPConnect

class TestMyClass(unittest.TestCase):

    def setUp(self):
        self.my_class_instance = DIPConnect(workspace_url="<your workspace URL starting with https://>")

    def test_my_function(self):
        self.my_class_instance.connect()

        from databricks.sdk import WorkspaceClient
        w = WorkspaceClient()
        for j in w.jobs.list():
            print(j)


if __name__ == '__main__':
    unittest.main()
