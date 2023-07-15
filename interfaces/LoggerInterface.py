class LoggerInterface:

    '''
        Method responsible for logging an event action.
    '''
    def LogAction(self, event, log):
        pass   
    
    '''
        Method responsible for logging entry.
    '''
    def LogWrite(self, log):
        pass

    '''
        Method responsible for creating the logging main file.
    '''
    def CreateLoggingFile(self, filename, filePath):
        pass