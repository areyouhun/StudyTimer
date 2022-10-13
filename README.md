# StudyTimer
시간을 재주고 엑셀에 자동으로 저장해주는 프로그램
<aside>
💡 **서비스 소개**
스톱워치 기능 및 기록된 시간을 엑셀 파일에 
자동으로 저장해주는 프로그램입니다.

**개발 기간** 2022.08 ~ 2022.09 (1개월)

**개발 인원** 1명 (개인 프로젝트)

**프로그래밍 언어** Python

**라이브러리** JSON, Tkinter, Openpyxl

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51b058f6-b4cc-4aa6-9e0b-a8eab8099131/Untitled.png)

## 주요 기능

**1)** **스톱워치**: 시간을 기록하고 리셋합니다. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ae411cc-164f-4965-aab0-4acc0598a702/Untitled.png)

**2)** **시간 데이터 관리 및** **엑셀 파일 연동**: 시간을 재고 저장하면 Study Timer 및 연동된 엑셀 파일이 업데이트됩니다. 

**this month**에 적힌 시간은 한 달 동안 기록한 시간을 나타내며, **until now**에 적힌 시간은 지금까지 기록한 시간을 나타냅니다.

![시간을 재기 전과 후의 StudyTimer **(25초 증가)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/abdee5b7-6f41-4046-a1df-09cf01f50c8a/Untitled.png)

시간을 재기 전과 후의 StudyTimer **(25초 증가)**

![시간을 재기 전 엑셀 파일의 **10월 코딩공부 시간**, **누적 코딩공부 시간**, **10월 13일 코딩공부 시간**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/26395c73-f763-4e58-8710-9faad97ed4d0/Untitled.png)

시간을 재기 전 엑셀 파일의 **10월 코딩공부 시간**, **누적 코딩공부 시간**, **10월 13일 코딩공부 시간**

![시간을 잰 후 엑셀 파일의  **10월 코딩공부 시간**, **누적 코딩공부 시간**, **10월 13일 코딩공부 시간 (25초 증가)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5af34d55-b4fa-4001-bfdf-007d8badde03/Untitled.png)

시간을 잰 후 엑셀 파일의  **10월 코딩공부 시간**, **누적 코딩공부 시간**, **10월 13일 코딩공부 시간 (25초 증가)**

시간 데이터는 JSON 파일로 관리되며 연동된 엑셀 파일에도 반영됩니다. **JSON파일에선 초 단위로 나타나며, 엑셀 파일은 시:분:초 단위로 나타납니다.** 

**3)** **다양한 컬러 옵션:** 프로그램을 실행할 때마다 Study Timer의 컬러가 랜덤으로 바뀝니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/354f2687-f4a3-4761-961a-07180e76049a/Untitled.png)