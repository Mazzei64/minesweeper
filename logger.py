from interfaces.LoggerInterface import LoggerInterface
from datetime import date, datetime
import os


class Logger(LoggerInterface):

    def __init__(self):
        self.__log_file = None
        self.__CreateLoggingFile()

    def LogAction(self, log):
        self.__log_file.write(f"{self.__time_stamp_format()} {log}\n")  
    
    def close(self):
        self.__LogGameOver()
        if not self.__log_file.closed:
            self.__log_file.close()

    def __LogGameStart(self):
        self.__log_file.write('*--------------------------------------------------------------------------*\n')
        self.__log_file.write(f"{self.__full_time_stamp_format()} -- Game started\n")
        self.__log_file.write('*--------------------------------------------------------------------------*\n\n')
        

    def __LogGameOver(self):
        self.__log_file.write('\n*--------------------------------------------------------------------------*\n')
        self.__log_file.write(f"{self.__full_time_stamp_format()} -- Game Over\n")
        self.__log_file.write('*--------------------------------------------------------------------------*\n\n')

    def __current_time__(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    def __current_date__(self):
        return date.today()
    
    def __full_time_stamp_format(self):
        return f"[{self.__current_date__()} - {self.__current_time__()}]"
    
    def __time_stamp_format(self):
        return f"[{self.__current_time__()}]"
   
    def __CreateLoggingFile(self):
        if not os.path.exists('minesweeper-log-file.txt'):
            self.__log_file = open('minesweeper-log-file.txt', 'w')
            self.__LogGameStart()
        else:
            self.__log_file = open('minesweeper-log-file.txt', 'a')
            self.__log_file.write('|**************************************************************************|\n\n')
            self.__LogGameStart()