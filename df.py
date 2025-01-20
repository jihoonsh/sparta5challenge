import pandas as pd
import requests
import xml.etree.ElementTree as ET
from google.colab import userdata

keyID = userdata.get('keyID')
url = f'http://openapi.foodsafetykorea.go.kr/api/{keyID}/I0490/xml/1/100'

response = requests.get(url)

root = ET.fromstring(response.text)
row_dict = {
    'PRDTNM': [], 'RTRVLPRVNS': [], 'BSSHNM': [], 'ADDR': [], 'TELNO': [],
    'BRCDNO': [], 'FRMLCUNIT': [], 'MNFDT': [], 'RTRVLPLANDOC_RTRVLMTHD': [],
    'DISTBTMLMT': [], 'PRDLST_TYPE': [], 'IMG_FILE_PATH': [], 'PRDLST_CD': [], 'CRET_DTM': [],
    'RTRVLDSUSE_SEQ': [], 'PRDLST_REPORT_NO': [], 'RTRVL_GRDCD_NM': [], 'PRDLST_CD_NM': [], 'LCNS_NO': []
}

for i in root.findall('./row'):
    for j in i:
        row_dict[j.tag].append(j.text)
df = pd.DataFrame(row_dict)
