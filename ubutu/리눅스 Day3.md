### 리눅스 3일차 

- **history** 
- `프롬프트` 설정하기 



**bash 환경설정**

1./bin/bash 

	/etc/profile (by root) : system-wide ( /etc/profile.d/*.sh)

2.~/.bash_profile 



3. vi  .`bashrc``



##### 기호를 이용한 파일 접근 권한 변경 

---

- 연산자 기호 

  > +권한부여    -권한제거     =접근 권한 설정 
  >
  > r 읽기 권한  w 쓰기 권한   x 실행 권한 

- sudo / root 의 차이점 

  > sudo는 ㅣ -일회성 / root는 관리자 계정으로 들어가는 것  
  >
  > su는 계정을 바꾸어서 들어가는 것 



- sudo chgrp sang testfile  소유그룹을 바꾼다. 

  chmod 권한을 바꾸는 것 . 

  ln 링크를 바꾸는 것.   

  chown 소유자를 바꾸는 것 

  chown or  chgrp  소유의  그룹을 바꾸는 것 

  touch : 시간만 바꿔주새요 

  mv : 이름 바꾸는 것  

  #### 6장 

**특수권한** 

- SUID :  실행 중에 파일 소유자의 권한 허용 

- SGID : 실행 중에 파일 소유 그룹의 권한 허용

  `Sticky Bits` 

**작업예약**

- at : 일회용  cron : 반복작업 

/etc/passwd : 사용자 계정 정보 

계정명:암호:uid:gid:추가설명(옵션):홈디렉토리 :로그인쉘 



/etc/shadow 

/etc/group 



- read(읽기) : 내용 볼 수 있는 권한 
- write(쓰기,편집,수정)  
- excute(실행)

chmod g+w, 0-r 

chmod 640 



unmask 033    dir 744 / 633 

sudo (su + do)

su (switch user)  su - 



chown 

chgrpvi /et 



ps-ef 

ps aux 

top 



app/user 프로세스에게 전달하는 메세지 = 시그널 

HUP = Hang up 

---

#### 사용자 계정 관리 명령 

- who 명령 

  - 현재 시스템을 사용하는 사용자의 정보를 출력한다. 

- /etc/shadow : 암호 + 암호 에이징 

- lastb 

- 









