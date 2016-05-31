from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests,json


def API_Request(url,method,token,payload):
    requests.packages.urllib3.disable_warnings()
    headers = {"Authorization": token,"Content-Type":"application/json"}
    if method in ['post','POST']:
        r = requests.post(url, headers=headers,data=json.dumps(payload),verify=False)
    elif method in ['delete','DELETE']:
        r = requests.delete(url, headers=headers,data=json.dumps(payload),verify=False)
    else:
        r = requests.get(url, headers=headers,data=json.dumps(payload),verify=False)
    return r.text



def stream(request):
    user = 'xx'
    content = {
        'user': user
    }
       
    return render(request, 'stream.html', content)



def api(request):

    url = 'https://10.75.6.130:9443/csa/query/table/apfloor'
    method = 'get'
    token = 'eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.m_DcR_YaUv7LruAGrL1YaPoIlfKEStMNNjulHBboteTS4eiYrzPqvA.0Md5GeZdckS1iO3akYCLHw.vCK8PJ8I6A40eyILwgqtZYxCDhNvRE09MZ73zQ0gST9QKGJF9Tt7cLDkdGbybmKPmLZk6JI2DXys2CwYw5EWNTRDbVchdS2s_1hJ61VRADbaH0iVIzRhr1d1XHk0mAeMKjWIfUz2EVKqG-sdiQawlrgSvjhMkOBX_srcVTH9rW090C-4Oco2NW3e2HAfIckk_s9GrO5GDaSbKxt0nxlmF8wpTw8CRmrueYOmVqzU6VQgsgyrj8YBAUoT1mUSCqXo1BNfpEzhRzHCFkojLdk_lMVNUapiTKYmTIbS-1wZ_lH3nW-MjNHKF-RrxmihATWfgTJLLiwCMiggJJWu9hqqQACu275omJfiDqz3fBAvdydx7rYtKTXw9Hgag-673Dm5tJeVBjqUBq1MfYRBvRrkG3ZjJEx7Fpr_IbGtAfOlDBO70s3lmF9M4ZuSvcLh39wRzmIShaoSiJwZqx2-v4wYlmSSOd3KW-eq3R0QR1slYreeIr23TQKPnxU81T001YGq2bQOgfnCsUZnJ1BECt3u0Xrh5pI6ekhl_8b6g461lSc8EemaFbrnryERZrJ-71ZTTl0pSCggI8d8pUQLZmMSjILbMYBR89Q8mbjh-S6pQWFQaF_js0sSU4uOWfWdh7sHCDJwL_REaRv5sE960ff6ZAKgcwdArL75RTCtP7ca-cYGfM_W0VZw_HBjYGsbfatqvZK0FAK6UmFq9qQjqBwpVPqz3vOo-sq7Bv7KTIl853lD200G2AmysV3u91-h32zlJ15l3cDqqC9GFZlVdCJJYBGnx1yx-9dSklRCYinLZQwlQ-5thC-Q4y4kG3yR_t_hnrbtOdrtBc1jBjL2RdpPff-WzClfVMWanoYIuH5E707vHJg_wD28Zm7ErYTmp1kTofeCHODtunJJ2OqbAjkvVfBPmcDYDNYS4ROBU0scx4xBzjYzcLyso8sneuqOebn-cPExwSD45bIZLZIitX_Dn-1WktoeJcZ6Oxzv4KzKxD2x1Ljj0oPKX-nCq5u71Ier92VdfDUZZmvD0uWU7pVZmktyHGjjXa-_I8l_oDQj_Fvu1d6f592I2B7GAZvScmNTN2lA5YPmSuPIlmHHoSbVTxYDlohVlvn944SuMHI9pwIMFcqSHiOmTjJXOPl4_kBXbYWVtgcrzNak0Vz1UoG7BJgqGHpV0Qcp9gKkfwASy3aG1wLqFYRdTRZ4eZZhtPRGHMu0jS7OBzqaGl7mu7_o2kWPYc3NZyngyprTx-xx2gMi78YmoXE4NXniZtFftwxv.R7Rf6XxvLTsvB0Jd1et84g'
    payload = ''
    api_result = API_Request(url,method,token,payload)
    content = {
        'api_result': json.loads(api_result)
    }

    return render(request, 'api.html', content)