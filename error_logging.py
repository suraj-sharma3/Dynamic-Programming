import logging

logging.basicConfig(level = logging.DEBUG, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s") # This is for providing the level at which we want to log the error, the levels could be debug, info, warning, error, critical. We can provide the file name in which we want to log the errors and the file mode that we want to use. This line of code / command can only run once in a program so just put this once at the start of your program. format attribute is used to provide the format in which we want to log the error. here error would be logged in this format : human readable time - error level name - error message

# format attribute's string formats for logging errors : https://docs.python.org/3/library/logging.html#logrecord-attributes

# 5 Steps of error logging in order of increasing importance
# warning, error & critical would be logged into the console & not debug & info
logging.debug("debug") # "debug" - error message that we want to log into the console
logging.info("info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")

# logging variable values

x = 5
logging.debug("The value of the variable is 5") # as the level of logging in basicConfig is debug

# logging errors

try:
    1/0
except Exception as e:
    logging.error(e, exc_info=True)

# another way : 
    
try:
    1/0
except Exception as e:
    logging.exception(e, exc_info=True)

# Custom Loggers
    
# Video Link (resume from custom loggers part) : https://youtu.be/urrfJgHwIJA?si=J2N6UvhG80yZRjnn//