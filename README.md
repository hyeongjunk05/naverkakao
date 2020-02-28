# Introduction

website clone project (https://www.myrealtrip.com/)
By 6 developers (4 Front-End, 2 Back-End)

# DB modeling

&nbsp;
&nbsp;
&nbsp;
## 회원 관련 테이블
&nbsp;
### accounts
- 가입 회원의 데이터를 저장
&nbsp;
### reviewes
- 상품 후기에 대한 데이터를 저장
&nbsp;
&nbsp;
&nbsp;
## 상품 관련 테이블
&nbsp;
### main_themes
- 상품 메인 카테고리 리스트 저장
&nbsp;
### sub_theme
- 서브 카테고리 리스트 저장  
&nbsp;
### tour_products
- 투어&티켓 상품에 대한 데이터를 저장
- 상품 명, 타입, 교통 수단, 위도(경도) 등
&nbsp;
### images
- 이미지에 대한 데이터 저장
- 상품 이미지, 썸네일
&nbsp;
### prices
- 상품 가격에 대한 정보 저장
- 상품 정가, 할인률, 기격 등
&nbsp;
### coures
- 상품이 제공하는 코스 데이터 저장
- 이미지, 상세 내용
&nbsp;
### guides
- 여행 가이드에 대한 데이터 저장
&nbsp;
### cities
- 도시 이름 리스트 저장
&nbsp;
### countries
- 국가 이름 리스트 저장
&nbsp;
&nbsp;
&nbsp;
## 결제 관련 테이블
&nbsp;
### orders
- 결제 관련 데이터 저장
- 결제정보, 연령, 여행목적 등의 데이터 참조
&nbsp;
### payments
- 결제 방식 저장 
- 신용카드 결제, 실시간 계좌 이체 등 결제 수단에 대한 리스트 저장
&nbsp;
### age
- 결제자에 대한 연령 정보 저장
- 10대, 20대, 30대 등등 연령대 리스트 저장
&nbsp;
### travel_objects
- 여행 목적에 대한 데이터 저장
- 결제창에서 제공하는 리스트 저장(혼자 떠나는 여행, 친구들과 떠나는 여행 등)



