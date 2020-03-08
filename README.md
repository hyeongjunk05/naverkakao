# Introduction
여행 상품 판매 서비스를 제공하는 [마이리얼트립](https://www.myrealtrip.com/) 클론 프로젝트

# 개발 인원 및 기간
- 개발기간 : 2020.02.23 ~ 2020.03.06
- 개발인원 : 3 Front-End, 2 Back-End

# 데모 영상 (이미지 클릭)
[![마이리얼트립](https://k.kakaocdn.net/dn/t8jNH/btqCyndYMRG/kG3rxJjM6kM8wrwLzu8ZL0/img.png)](https://youtu.be/DQS73OiWkKM)

# 적용 기술
- Python
- Django Web Framework
- Bcrypt
- JWT
- MySQL
- AWS EC2, RDS
- Gunicorn
- CORS header
- Beautifulsoup, Selenium

# 구현 기능
## 계정
- Bcrypt를 사용하여 패스워드 해싱
- JWT를 사용하여 로그인 시 토큰 발행 
- 회원 가입 및 로그인
- 이메일 유효성 검사
- 마이 페이지

## 상품
- 메인페이지
- 상세페이지
- 상품 검색 기능

## 리뷰
- 상품 별로 리뷰 리스트 반환
- 로그인한 사용자만 작성
- 수정 및 삭제 기능 지원
- 평균 평점 및 리뷰 수 데이터 반환

# 데이터 모델링 ERD
![데이터모델링](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fl3Dw8%2FbtqCuYzsUvM%2FqnzHvTa8MpM2UcBNmPiITK%2Fimg.png)

