# Introduction
여행 상품 판매 서비스를 제공하는 [마이리얼트립](https://www.myrealtrip.com/) 클론 프로젝트
By 6 developers (4 Front-End, 2 Back-End)

# 개발 인원 및 기간
- 개발기간 : 2020.02.23 ~ 2020.03.06
- 개발인원 : 4 Front-End, 2 Back-End

# 데모 영상 (이미지 클릭)
[![마이리얼트립](https://k.kakaocdn.net/dn/t8jNH/btqCyndYMRG/kG3rxJjM6kM8wrwLzu8ZL0/img.png)](https://youtu.be/DQS73OiWkKM)

# 적용 기술
- Python
- Django Web Framework
- Bcrypt
- JWT
- MySQL
- AWS EC2, RDS
- CORS header

# 구현 기능
## 공통
- Beautifulsoup, Selenium을 이용한 실제 데이터 수집
- Bcrypt를 사용하여 패스워드 해싱
- JWT를 사용하여 로그인 시 토큰 발행 
- 회원 가입 및 로그인
- 이메일 

## 상품
- 메인페이지
  - 메인카테고리 / 서브카테고리 상품 분류 구현 
- 상세페이지
- 상품 검색 기능

## 리뷰
- 상품 별로 리뷰 리스트 반환
- 로그인한 사용자만 작성
- 수정 및 삭제 기능 지원
- 평균 평점 및 리뷰 수 데이터 반환

# 데이터 모델링 ERD
https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FJa9fx%2FbtqCuY0wO3B%2FzqGkRs2RKOdr2KH5SHvkx1%2Fimg.png

