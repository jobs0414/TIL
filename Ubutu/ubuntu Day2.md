### 리눅스 4장 -2일차 

---



1. find /home -name .bashrc -exec ls -l {}

-  ".bash*"   꼭 넣어주어야 한다. 

- find /home 



- ctrl+alt + f3   문서편집기 들어감? 

- ctrl + alt + f1  다시 돌아옴 



**리눅스 편집기** 

---

- nano examples.desktop 

- head -10 examples.desktop 

- vi 시작 >>>명령 모드 >>> i,l,a,A,o,O 입력모드 (입력한 키를 내용으로 처리)



**vi 종료방법** 

---

-  저장 >> 종료 

> esc  : wq  (write quit)

-  저장 없이 종료 

> esc : q!  (quit ! 강제 )

> esc : w  저장 



#### 입력모드 전환하기 (i,l,a,A,o,O)

---

1) i (insert) : 입력모드 전환 후 커서 앞에 글자 입력  (커서 앞에 들어간다)

2) a (append) :  커서 뒤에 글자가 들어간다.

     A : 라인 끝 입력 

3) o  :  커서 아래 빈 줄 추가 후 입력 

4) O : 커서 위 빈 줄 추가 후 입력



r : 한글자 교환 

cw : change word 단어 교환 

cc : 라인 교환 

c : 현재 커서부터 라인끝까지 교환 



x : delete (커서 뒤 )

X : backspace (커서 앞)

dw : delete word 

dd : 라인 삭제 

D : 현재 커서부터 라인끝까지 삭제 



yw (yank word) : 단어 복사 

yy : 라인 복사 



p : 붙여넣기 



Substitute 

바꾸기 

: %s ubuntu UBUNTU  하면 일괄적으로 대문자로 바뀐다. 

한 라인만 바꾼다. 



#### shell 

---

-user와 os 를 연결해주는 번역기. 

shell이라는 것이 실행이 안되면 운영체제에 명령어를 전달할 수 없다. 



리눅스 

alias a=date 

date별명을 a로 준다. 

터미널 끄고 나면 다시 원래대로 돌아온다. 



셀의 기능과 종류 

~  : 홈디렉터리 이동 



$  shell에 의해 값으로 바꾸어주세요 그런 의미이다. 

```python
a=`pwd`  pwd의 경로를 집어넣는다. 
b=$(pwd) 
pwd의 결과를 b에 넣는다. 

```



출력 리다이렉션 

cat f1 f5 > f.good 2 > f.bad 



```python 
grep // pipe  를 쓴다. 

```

`PATH` : 명령어의 실행 파일을 검색할  디렉토리 목록 

`env` : 나 환경변수만 볼꺼야 

name 

변수는 위에서 아래로만 흐를 수가 있다. 

echod



####  shell 

- 셸이 사용하는 변수에는 셸 변수와 환경변수가 있다. 

- 전체 변수 출력 : set , env 명령어 

- 주요 셸 환경 변수 

- PATH : 명령을 탐색할 경로 
- PWD :  작업 디렉터리의 절대 경로 

환경 변수 설정하기 : `export` 명령어 사용 

some를 환경변수로 바꿔보자 



환경변수를 다시 셀 변수로 바꾸기 : `export -n` 명령 

변수 해제하기 : `unset`













