import requests

requests.packages.urllib3.disable_warnings()

VERSION = "0.4.5"


def check(thai_id, thai_name, thai_surname, thai_year=2562):

    URL = "https://refundedcheque.rd.go.th/itp_x_tw/pages/n/result.jsp"
    URL_API = "https://refundedcheque.rd.go.th/itp_x_tw/SearchTaxpayerServlet"

    headers = {"Referer": "https://refundedcheque.rd.go.th/itp_x_tw/pages/n/inquire.jsp"}

    s = requests.Session()
    r = s.get(URL, headers=headers, verify=False)

    data = {
        "taxYear": thai_year,
        "fName": thai_name,
        "lName": thai_surname,
        "nid": thai_id,
        "searchType": None,
        "effDate": None,
    }

    headers = {"Referer": URL}

    r = s.post(URL_API, data=data, headers=headers, verify=False)

    if r.status_code != 200:
        return None

    raw_data = r.json()

    process_dict = {
        "process_1": "ยื่นแบบฯ",
        "process_2": "ดำเนินการ",
        "process_3": "พิจารณาคืนภาษี",
        "process_4": "ส่งคืนภาษี",
        "process_5": "ได้คืนภาษี",
    }

    raw_data["process_text"] = process_dict.get(raw_data["processPicName"], "")

    # Rquire document
    if (
        raw_data["processPicName"] == "process_3"
        and raw_data.get("reqDoc")
        and raw_data.get("uploadDoc")
    ):
        raw_data["process_text"] = "ได้รับเอกสารของท่านแล้ว อยู่ระหว่างการตรวจสอบความถูกต้อง"

    elif raw_data["processPicName"] == "process_3" and raw_data.get("reqDoc"):
        raw_data["process_text"] = "ขอให้ท่านส่งเอกสาร"

    return raw_data
