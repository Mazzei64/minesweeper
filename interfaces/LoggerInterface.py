class LoggerInterface:

    '''
        Method responsible for logging an event action.
    '''
    def LogAction(self, event, log):
        pass   
    
    '''
        Method responsible for logging when application initializes.
    '''
    def LogGameStart(self):
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

    '''
        Method responsible for handling closing of current file descriptor object
        and logging when application closes.
    '''
    def close(self):
        pass  