import requests

# TOKEN = "485131186e3ba40f39bdc56b5b48a7d6b1c77d1a"
JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNjE2MTg0MjU2LCJlbWFpbCI6IiJ9.u8sqWyYSQKaDrS4RW5LisTulwiSPbcHZth-QTNo_S3k"
)

# "eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNjE2MTg0MjU2LCJlbWFpbCI6IiJ9"

headers = {
    # 'Authorization': f'Token {TOKEN}',  # Token 인증
    'Authorization': f'JWT {JWT_TOKEN}',  # JWT 인증
}

res = requests.get("http://127.0.0.1:8000/post/1/", headers=headers)
print(res.json())