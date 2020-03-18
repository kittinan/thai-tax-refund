# thai-tax-refund
check status for thai tax refund

https://www.rd.go.th/publish/27942.0.html


## Installation

available on pip https://pypi.org/project/thaitaxrefund/

```bash
pip install thaitaxrefund
```

## Usage

Command line usage

```
thaitaxrefund THAI_ID THAI_FIRSTNAME THAI_LASTNAME [--year=<THAI_YEAR> --json]
```

command line example

```bash
thaitaxrefund 1111111111111 บิ๊ก ตู่
```

```python
import thaitaxrefund

thai_id = '1111111111111'
thai_name = 'บิ๊ก'
thai_surname = 'ตู่'
result = thaitaxrefund.check(thai_id, thai_name, thai_surname, thai_year=2562)
```

### Example result
```json
{
    "process_text": "พิจารณาคืนภาษี",
    "code": "MSG107",
    "countByName": -1,
    "countByNameNid": 1,
    "countByNid": -1,
    "criteria": {
        "dln": "",
        "fName": "บิ๊ก",
        "formCode": "",
        "lName": "ตู่",
        "nid": "1111111111111",
        "taxYear": "2562",
        "tin": "",
        "txpTtlText": ""
    },
    "formData": {
        "dln": "ภงด91000000000000000000000",
        "fName": "บิ๊ก",
        "formCode": "ภงด91",
        "lName": "ตู่",
        "nid": "1111111111111",
        "taxYear": "2562",
        "tin": "1111111111",
        "txpTtlText": "นาย"
    },
    "formDetailList": [
        {
            "effDate": "12/03/2563",
            "ofcName": "กองบริหารการเสียภาษีทางอิเล็กทรอนิกส์",
            "pndType": "ภ.ง.ด.91",
            "seq": 1
        }
    ],
    "formSendDocDetail": null,
    "ipAddress": "xxx.xxx.xxx.xxx",
    "message": "อยู่ระหว่างดำเนินการ หากมีข้อสงสัย โปรดติดต่อ<br>สำนักงานสรรพากรพื้นที่กรุงเทพมหานคร 26<br>หมายเลขโทรศัพท์ 0-2454-8475,0-2454-8618-20 ต่อ 125-127,0-2454-8623-24 ต่อ 125-127",
    "messageEN": "In process. Please contact Revenue Branch Office<br>Bangkok Area Revenue Office 26<br>Tel. 0-2454-8475,0-2454-8618-20 ต่อ 125-127,0-2454-8623-24 ต่อ 125-127",
    "processPicName": "process_3",
    "reqDoc": false,
    "reqNewK39": false,
    "searchPromptPay": false,
    "uploadConsiderDoc": true,
    "uploadDoc": false,
    "urlReqNewK39": "",
    "urlSearchPromptPay": "",
    "urlUploadDocument": "",
}
```
