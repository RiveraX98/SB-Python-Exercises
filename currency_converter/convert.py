from flask import Flask, request
import requests


base_URL = "https://api.exchangerate.host"


def check_info(convert_from, into, amount):
    res = requests.get(f"{base_URL}/symbols")
    data = res.json()
    code_list = data["symbols"]

    if convert_from not in code_list or into not in code_list:
        msg = "Invalid currency code"
        return (msg)

    elif amount.isdigit() == False:
        msg = "Invalid Amount"
        return (msg)

    else:
        return ("ok")


def convert_currency(convert_from, into, amount):

    res = requests.get(
        f"{base_URL}//convert?from={convert_from}&to={into}&amount={amount}")
    data = res.json()
    converted_amount = round(data["result"], 2)

    return (converted_amount)
