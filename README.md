# 운동 기록 편의 웹앱.

## 목표
- 사용자에게 운동 기록 시 있을 수 있는 불편함을 해결하여 좋은 UX를 제공.
- **세트 기록**: 세트 세팅을 간단하게 그 세트 데이터를 기반으로 요일별 세트를 설정할 수 있음.
- **세트 수**: 세트당 수행 횟수를 편하게 편집할 수 있음.
- **시간**: 세트 수행 시간과 세트당 휴식 시간을 편하게 기록할 수 있도록 함.

----------------------------------------------------

## 요구사항 정의서

- 

----------------------------------------------------

## ERD

### user: 유저 정보
<details> 
<summary>컬럼 </summary>

- id[사용자_아이디] (PK)
- name[이름]
- email[이메일]
- password[비밀번호]
- age[나이]
- weight[무게]
- height[키]
- muscle_mass[골격근량]
- fat_mass[체지방량]
- created_at[생성_날짜]
- updated_at[수정_날짜]
</details>

### workout: 운동 날짜 및 시간

<details> 
<summary>컬럼 </summary>

- id (PK)
- user_id (FK)
- start_date_time[운동_시작_시간]
- end_date_time[운동_끝_시간]
- total_time[총_운동_시간]
- created_at[생성_날짜]
- week_day [요일]
</details>

### workout_set: 세트 기록
<details> 
<summary>컬럼 </summary>

- id (PK)
- workout_id (FK)
- exercise_id (FK)
- set_order[수행_순서]
- weight[무게]
- reps[수행_횟수]
- duration[수행_시간]
- rest_time[휴식_시간]
- memo[특이사항] (nullable)
- created_at[생성_날짜]
</details>

### exercise: 웨이트 종목
<details> 
<summary>컬럼 </summary>

- id (PK)
- name[이름]
- target_area[부위]
- category[구분]: enum(하체, 등, 어깨, 가슴)
- description[설명]
- created_at[생성_날짜]
- updated_at[수정_날짜]
</details>

----------------------------------------------------

## API명세서

