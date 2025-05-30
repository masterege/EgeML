import sys
import logging

def errorMessageDetail(error, errorDetail:sys):
    _, _, excTb = errorDetail.exc_info()
    fileName = excTb.tb_frame.f_code.co_filename
    errorMessage = f"Error occured in Python Script -> \nName: [{fileName}] \nLine: [{excTb.tb_lineno}] \nError Message: [{str(error)}]."
    return errorMessage

class CustomException(Exception):
    def __init__(self, errorMessage, errorDetail:sys):
        super().__init__(errorMessage)
        self.errorMessage = errorMessageDetail(errorMessage, errorDetail = errorDetail)

    def __str__(self):
        return self.errorMessage
