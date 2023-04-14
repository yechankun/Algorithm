# algorithm

알고리즘 풀이를 진행하는 리포지토리입니다.

## 🏷️ 목차

- [algorithm](#algorithm)
  - [🏷️ 목차](#️-목차)
  - [📘 진행 방법](#-진행-방법)
  - [🧐 COC(Code of Conduct, 행동 규칙)](#-coccode-of-conduct-행동-규칙)
  - [💻 풀이 Commit 규칙](#-풀이-commit-규칙)
  - [🍴 PR 규칙](#-pr-규칙)
  - [💻 디렉토리 및 파일 구조](#-디렉토리-및-파일-구조)
  - [💦 참고](#-참고)

## 📘 진행 방법

1. 알고리즘을 풀이한다.
2. 풀이한 내용을 형식에 맞춰 커밋한다.

## 🧐 COC(Code of Conduct, 행동 규칙)

- 자신을 비하하지 않고 자신감을 가진다.
- 남들이 얻을 수 있는 것을 내가 노력해서 얻지 못하는 것은 없다고 믿는다.
- 알고리즘 풀이는 삶을 좀 더 풍요롭게 좀 더 지혜롭게 만들 것을 믿는다.

## 💻 풀이 Commit 규칙

- 풀이 Commit에만 해당하는 규칙입니다.
- 문제 풀이시
  - solve(문제종류) : 6자날짜표기 파일명
- 풀이 변경시
  - fix : 6자수정날짜표기 파일명
- 파일명, 폴더 변경시
  - move : 6자수정날짜표기 파일명

| 플랫폼 이름   | 예시                                              |
| ------------- | ------------------------------------------------- |
| 백준          | solve(simulation) : 221227_bj_s2\_오목.py         |
| 프로그래머스  | solve(search) : 221227_pg_lv1\_컨트롤 제트.py     |
| 리트코드 예시 | solve(math) : 221227_lt_e_Two Sum.py              |
| 코드트리 예시 | solve(simulation) : 221227_ct_g2\_정육면체 굴리기 |

## 📁 파일명 규칙

- 풀이날짜\_플랫폼\_난이도\_문제명.확장자

- 풀이날짜: 6자날짜표기법

- 플랫폼: 백준/프로그래머스/리트코드/코드트리 = bj/pg/lt/ct
- 난이도: 레벨표기일 경우 = lv, 광물표기일 경우 = 첫글자영어소문자, 리트코드의 경우 = Difficulty의 첫글자
  - e.g. 220411_pg_lv2\_숫자 더하기.py, 220411_bj_b1\_덧셈나눗셈.py, 221227_lt_e_Two Sum.py
- 폴더명은 문제종류(영어)로 한다.

## 그 외 규칙

- docs : 문서 수정
- comment : 필요한 주석 추가 및 변경
- rename : 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우
- remove : 파일을 삭제하는 작업만 수행한 경우

## 💦 참고

문제 종류: two pointer>dp>simulation>search>greedy>sort>string>math

> 문제 풀이가 복합적인 알고리즘이 요구될 경우 왼쪽이 우선순위를 가짐
