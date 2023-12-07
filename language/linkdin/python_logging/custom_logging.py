# Customized logging

# basicConfig() # basicConfig() is a function that configures the logging system.
# basicConfig(
# format=formatstr, # formatstr is a string that specifies the format of the log message.
# datefmt=datestr, # datestr is a string that specifies the format of the date/time portion of the log message.
# level=levelstr, # levelstr is a string that specifies the lowest-severity log message that will be written to the log file.
# filename=filenamestr, # filenamestr is a string that specifies the name of the log file.
# filemode=filemodestr # filemodestr is a string that specifies the mode to open the log file with.
# # )

# %(asctime)s -> Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).
# %(filename)s -> Filename portion of pathname.
# %(funcName)s -> Name of function containing the logging call.
# %(levelname)s -> Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
# %(lineno)d -> Source line number where the logging call was issued (if available).
# %(message)s -> The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
# %(module)s -> Module (name portion of filename).
# %(name)s -> Name of the logger used to log the call.
# %(pathname)s -> Full pathname of the source file where the logging call was issued (if available).
# %(process)d -> Process ID (if available).
# %(processName)s -> Process name (if available).
# %(thread)d -> Thread ID (if available).
# %(threadName)s -> Thread name (if available).

# Path: language/linkdin/python_logging/custom_logging.py

# Demonstrate how to customize logging output
import logging

ext_data = {'user': 'gk'}


# TODO: add another function to log from
def another_function():
    logging.debug("This is a debug-level log message", stack_info=True)


def main():
    # set the output file and debug level, and

    # TODO: use a custom formatting specification
    frt_str = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    date_frt_str = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(
        datefmt=date_frt_str,
        format=frt_str,
        level=logging.DEBUG,
        filemode="w",
        filename="output.log")

    logging.info("This is an info-level log message", extra=ext_data)
    another_function()


if __name__ == '__main__':
    main()
