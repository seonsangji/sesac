import smtplib
from email.mime.text import MIMEText # 메일의 컨텐츠 인코딩 포맷
import os

from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
NAVER_EMAIL = os.getenv("NAVER_EMAIL")
NAVER_PASSWORD = os.getenv("NAVER_PASSWORD")

RECIPIENT_MAIL = NAVER_EMAIL

subject = "커피가 왤케 맛이없지 이건 꿈이야"
body = "컴포즈 먹고싶두"


message = MIMEText(body, _charset='utf-8')
message['subject'] = subject
message['from'] = NAVER_EMAIL
message['to'] = RECIPIENT_MAIL

try: 
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls() #TLS 보안 연결 시작
    smtp.login(NAVER_EMAIL, NAVER_PASSWORD)
    smtp.sendmail(NAVER_EMAIL, RECIPIENT_MAIL, message.as_string())
    print("메일이 성공적으로 발송되었습니다.")
except Exception as e:
    print(f"메일 전송 중 오류 발생: {e}")
finally:
    smtp.quit()