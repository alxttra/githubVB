import xrequests, concurrent.futures
executor = concurrent.futures.ThreadPoolExecutor(20000)
url = "https://camo.githubusercontent.com/4c3e5a1660b7c3980298561ba7b6456d0150a52b11b0e0e6d47b76d29fe4c91a/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d616c7874747261267374796c653d666c61742d73717561726526636f6c6f723d666638636563"
session = xrequests.Session()
def send():
    session.get(url)

while True:
    executor.submit(send) 
