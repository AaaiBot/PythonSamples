class SqlCommandRunner:

    def __init__(self):
        self.SqlCommand = "Not defined"
        self.Location = "c:\\abc.xyz.db"
        pass

    def run(self):
        self.__getDataseConnection()
        self.__runSqlCommand()

    def __location(self):
        return "c:\\Abc.xyz.db"

    def __runSqlCommand(self):
        print("Running this SQL Script: " + self.SqlCommand)

    def __getDataseConnection(self):
        print("Getting database connection from: " + self.__location())
