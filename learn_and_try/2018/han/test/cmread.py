from utils.client import HTTPClient
from utils.log import logger

url = 'http://wap.cmread.com/r/l/ballot.jsp?operateDataId=125840893&itemid=20884&ln=42886_619143_97699197_9_1_L1&purl=%2Fr%2Fp%2Fspds.jsp&operateFregmentId=619143&vt=2&ballotid=8780'
client = HTTPClient(url=url, method='GET')
res = client.send()
logger.debug(res.text)

