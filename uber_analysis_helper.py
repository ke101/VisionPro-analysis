import pandas as pd
import pytz


# function to convert UTC time to Eastern time

# ref: https://www.askpython.com/python/examples/utc-to-est-conversion#:~:text=Converting%20UTC%20to%20EST%20in%20Python%20can%20be%20done%20using,time%2C%20making%20the%20conversion%20accurate.
def convert_utc_to_est(utc_time):
    utc_time = utc_time.tz_localize(tz='UTC')
    # fetch the timezone information
    est = pytz.timezone('US/Eastern')

    # convert utc to est
    est_time = utc_time.astimezone(est)

    # return the converted value
    return est_time

# get new time after add or minus
def time_shift(current,operation,amount):
    if operation=="+":
        return pd.Timestamp(current)+ pd.Timedelta(minutes=amount)
    elif operation =="-":
        return pd.Timestamp(current)- pd.Timedelta(minutes=amount)
    else:
        return "invalid operation"

