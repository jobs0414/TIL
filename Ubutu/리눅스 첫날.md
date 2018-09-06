### 리눅스 

- 유미 강사님 takytaky@empas.com

- https://www.kernel.org/

The Linux Kernel Archives

Protocol Location HTTP https://www.kernel.org/pub/ GIT https://git.kernel.org/ RSYNC rsync://rsync.kernel.org/pub/ Latest ...

www.kernel.org

![img](https://ssl.pstatic.net/static/blank.gif)

-  **리눅스의 계보** 

---

1. 슬랙웨어 계열의 SUSE.

2. 데비안 (dpkg의 시초) 계열의 Ubuntu

3. 레드햇 계열의 페도라 & CentOs (기업의 70%는 현재 레드햇을 사용중)



우분투 LTS = Long Term Support 장기 지원 버전





-  **리눅스의 명령어**  

---

1. 리눅스의 명령어는 명령/옵션/인자 로 구성됨.

2. 옵션은 숏 옵션(ex. -a)과 롱 옵션(ex. --help)으로 나뉜다.

3. ls (list) : 디렉터리에 있는 내용을 보는 명령.

ls -F

-> 이름만 보고도 파일과 폴더 구분하고 싶을 때 사용.

ls -a

-> 숨겨진 파일 보이기

ls -aF

-> 숨겨진 파일도 보이고, 파일과 폴더 구분가능.

ls -r

-> 순서를 뒤집어서 정렬

ls -ld

-> 디렉토리 자체의 정보



![img](https://blogfiles.pstatic.net/MjAxODA5MDRfMjE0/MDAxNTM2MDI4MzM0ODY3.XTBBeft_tFUq0Jyo3Or2PIrSdxdzt3KlppWFbN8zHU0g.kMxB5qbAhY5912rgzpamgbIDqwmA_uVddXMVBfxIki8g.PNG.berote/capture-20180904-113131.png)



whereis 명령어

-> 명령어의 위치

tty

-> 현재의 터미널을 제어하는 폴더의 위치



echo 메세지 > 출력 터미널 위치

![img](https://blogfiles.pstatic.net/MjAxODA5MDRfMTA0/MDAxNTM2MDI5NzkwNjA3.VfNZ1kv9LhZvDiguNldfTu_ujIDGHLrAthhbYnUE1e8g.90Ff4f0wU2GsYe_nQIiB8sO2ue6BYUswfaCOmreeEcUg.PNG.berote/capture-20180904-115610.png)



mkdir

-> 디렉토리 생성



echo hello world > hello

-> hello world라는 내용을 가진 hello 파일 생성



mkdir -p

-> 중간 디렉토리 자동생성



ex) mkdir -p a/b/c



rmdir

-> 디렉토리 삭제



rm -r

-> 디렉토리, 파일 하위에 내용이 있어도 해당 디렉이나 파일 삭제



cat

-> 파일 내용 출력



more

-> 파일 내용을 화면 단위로 출력



less

-> more을 개선한 명령. 파일 내용 앞뒤로 스크롤 가능.

-> less상태에서 / 누르고 검색가능



tail

-> 파일 뒷부분의 행을 출력



head

-> 파일 앞 부분 출력



cp

-> cp file1 file2

-> cp -r dir1 dir2

-i 옵션: 파일2가 이미 존재할 시 덮어쓸 것인지 물어본다.

-r 옵션: 디렉터리 복사 할때



mv 파일명 파일명2

-> 파일명을 파일명2로 바꾼다.



touch

-> 빈 파일 생성

touch 기존파일명

-> 데이터 변경없이 파일 최종수정시간만 최신으로 업데이트 된다

touch -mt 09011200 파일명

-> 파일의 modify time 직접 수정



grep(=global regular expression print)

->지정한 패턴이 포함된 행을 찾는다.

-> -i 대문자,소문자 모두 검색 / -n 행번호 출력/ -c 행의 개수만 출력

-> -v 해당 패턴이 제외된 결과만 출력 / -e 패턴의 중복허용 (ex. grep -e tel -e ftp /etc/services)



- **리눅스 파일 종류**
---


1.일반 파일

2.디렉터리 - 디렉터리도 파일 취급

3.심벌릭 링크 - 원본 파일 대신하도록 원본 파일을 다른 파일명으로 지정한 것. (바로가기와 비슷)

4.장치 파일 - 리눅스, 하드디스크나 키보드 같은 각종 장치도 파일로 취급.







- **주요 디렉토리 기능**
---


1./dev : 장치 파일

2./home: 각 계정 홈디렉토리(로그인시 처음 위치하는 경로)

ex) /home/user1

3./opt : third party 프로그램 설치 경로

4./root: root(관리자)홈 티렉토리

5./usr (Unix System Resource): 명령어/공용 라이브러리/메뉴얼 페이지\

6./boot : 운영체제 실행파일(=kernel, vmlinuz...)

7./etc: 시스템 설정 파일

8./tmp (temporary): 임시파일

9./var (variable): 로그 등 자주 바뀌는 파일이 주로 저장







- **절대 경로명과 상대 경로명**
---


1.절대경로 : 반드시 /로 시작한다. 특정 위치를 가리키는 절대 경로명은 항상 동일하다.



ex) /home/user1



2.상대경로 : /이외의 문자로 시작한다. 현재 디렉토리 기준 서브 디렉토리로 내려가면 . 하나를 추가.

현재 디렉토리 기준 상위 디렉토리로 올라가면 ..추가한다.

상대경로명은 현재 디렉터리가 어디냐에 따라 달라진다.



ex) 현재 위치 /home 에서 cd .. 할 경우 / 로 옮겨진다.



\1. pwd(Present Working Directory) : 현재 위치 확인 

\2. cd(Change Directory) : 디렉토리 바꾸기 (그냥 cd만 입력할 경우 혹은 ~을 입력할 경우, 계정인 /home/user1 위치로 이동)

![img](https://blogfiles.pstatic.net/MjAxODA5MDRfMTY3/MDAxNTM2MDQwNTEzMzE4.HYgcWxjqPb4Rws64Y7nEiwg8-jnqh5zH2EVS6_SPiAog.PlsgA6hSjQrARWjeDfciqjyBb1fj9oRF_akOTa6t6fkg.PNG.berote/capture-20180904-145440.png)



d 파일 종류

rwxr-xr-x 권한

2 하드 링크 개수

user1 파일 소유자

user1 파일이 속한 그룹

4096 파일 용량

9월 3 21:43 파일 최종 수정시간

템플릿 파일명



- **파일시스템 구조**

---

1.슈퍼블록(superblock): 파일시스템 일반 속성 (리눅스 ext4 / xfs == 윈도우 ntfs), 크기, used/free...

2.아이노드 테이블(inode table) : 각 파일 속성

-> 디렉토리는 아이노드 번호를 갖고있다



**링크의 종류**
---

1.하드링크(Hardlink)

-같은 파티션에만 구현

-파일만 링크 구현 (디렉은 x)



2.심볼릭링크(Symbolic link)

-다른 파티션에도 구현가능

-파일/디렉토리 링크 구현



**하드링크 만들어보기**
---
link.org의 내용과 하드링크인 link.h의 내용이 같다.

![img](https://blogfiles.pstatic.net/MjAxODA5MDRfMTA5/MDAxNTM2MDQ4MzIwODMz.1yaSs5KzCFSCpnKUbTRVDDvK11Ns9s9HEr0aZFzjSsIg.zBpKDaRCZXrUZ_D5LPc8lGRR4iroHJ4xbHHR12sbUbMg.PNG.berote/1.png) 

![img](https://blogfiles.pstatic.net/MjAxODA5MDRfMjQ1/MDAxNTM2MDQ4NTMzMjMw.21ZW952oGyLQ1J8vDWHFyzYRKlZJLyVHAeCxbN6m7SAg.wjgE24XQpTuGh52PrvcjpnZkEKmz8okWwyTNq2EuzRQg.PNG.berote/2.png) 



**심볼릭 링크 만들어보기**
---
link.org가 8글자이므로 심볼릭 링크의 크기는 8바이트다

**![img](https://blogfiles.pstatic.net/MjAxODA5MDRfNSAg/MDAxNTM2MDQ4Nzg4MjA5.OdRvZ6cc8VYADKToqgwbCX6sMrihU6pvA8Au7nbndKAg.TpaUE0Gn_nqB295q2BZ_C762jqW6trpmaB3zot3HcqMg.PNG.berote/3.png)**



**![img](https://blogfiles.pstatic.net/MjAxODA5MDRfMjI4/MDAxNTM2MDUwMzcxNjM4.G9gHQWffbpH-_26db3Jypazx5vqXh0vYagEY8DpBIOog.bHbkuuhcnGn7-YEMHyAoJMk1Muj5HHbVOq3HdxAYSbEg.PNG.berote/4.png)**




