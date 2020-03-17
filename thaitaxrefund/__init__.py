import os
import re
import requests


def check(thai_id, thai_name, thai_surname, thai_year=2562):

    URL = 'https://refundedcheque.rd.go.th/itp_x_tw/pages/n/result.jsp'
    headers = {
        'Referer': 'https://refundedcheque.rd.go.th/itp_x_tw/pages/n/inquire.jsp'
    }

    data = {
        'TAX_YR': thai_year,
        'PIN': thai_name,
        'NAME': thai_name,
        'SNAME': thai_surname
    }

    r = requests.post(URL, data=data, headers=headers)

    print(r.status_code)
    print(r.content)


if __name__ == "__main__":
    thai_id = ''
    thai_name = ''
    thai_surname = ''

    check(thai_id, thai_name, thai_surname)
