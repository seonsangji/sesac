import imaplib
import email
from email.header import decode_header

from dotenv import load_dotenv
import os

load_dotenv()

IMAP_SERVER = 'imap.naver.com'
IMAP_PORT = 993

NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(NAVER_EMAIL, NAVER_PASSWORD)

# 메일함 선택 ( 기본 INBOX )
mail.select("INBOX")
status, messages = mail.search(None, "ALL")

# print(status, messages)

mail_ids = messages[0].split()
latest_mail_id = mail_ids[-1] # 가장 최신 id 가져오기

# 최신 메일 가져오기
status, msg_data = mail.fetch(latest_mail_id, "(RFC822)")
# print(status, msg_data)

# 메일의 본문 데이터 파싱하기 
for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")
        print(f"제목: {subject}")

        from_ = msg.get('From')
        print(f"발신자: {from_}")

        if msg.is_multipart():
            for part in msg.walk(): 
                # 메일 본문, 멀티파트로 인코딩 된 걸 하나하나 읽어가기
                content_type = part.get_content_type()
                content_disposition = str(part.get('Content-Disposition'))
                body = part.get_payload(decode=True).decode('utf-8')
                print(f"본문: {body}")
        else:
            #메일이 단일파트라면
            body = msg.get_payload(decode=True).decode('utf-8')
            print(f"본문: {body}")
            break

    mail.logout()