## 소프트웨어 tool 

#### chocolatey 

윈도우즈에서 소프트웨어 설치를 쉽게 할 수 있는 툴 

#### typora

1. 제목태그 

   ```python
   #제목1
   ##제목2
   ###제목3
   ####제목4
   #####제목5
   ```

#### typora 툴 메뉴 

툴 메뉴 사용하기 



#### 테이블(표) 만들기

```python
|제목 1 | 제목 2 | 제목 3 | 
```

> 인용구를 사용한 markdown 
>
> 수평선 --- 



#### git bash 

1. 효율성 측면과  command에서만 제공하는 기능들이 더 있기 떄문! 

   깃 page를 통해서 나만의 페이지 만들기 

   ```python
   git bash >> code .   
   mkdir / ls-al  /cd  / cd.. 
   git add index.html 
   git status   #git 상태를 묻는 것 
   git commit -m #"first commit" #git의 스냅샷을 찍어야 관리를 한것. 
   git log #지금까지 한 모든 log를 볼 수 있음 
   
   git remote add origin https://github.com/qejrpqjkl0204/qejrpqjkl.github.io.git 
   
   git push -u origin master #원격저장에 밀어넣기 
   git diff #내가 무엇을 수정했는지 볼 수 있음 
   q하면 나갈 수 있음 
   
   결론 
   git add 
   git commit -m ""
   git push -u orgin master
   ```

   git init 은 무얼 하는 것인가?  git 관리자 (master)를 부여함. 기능 

   ### git add 와 commit 의 차이

   ```python
   git add와 git commit 
   git add에는 2가지 기능 
   1. 잠깐 멈춰!
   2. 사진 찍듯이 저장 stage에 위에 올려놓는 것 
   git add를 계속 하면 저장이 계속 됨. 
   git commit 무대위에 올린 친구들 완전히 저장! 
   
   
   깃과 깃허브는 다르다.   비트버켓 
         남의 컴퓨터에 공간이 만들어져있음. 
       
       
       config 는 설정 
       cat config 
    git remote는 연동 
   git push -u origin master 한번만 하면 되. 
   ```

간편하게 

git add 

git commit -m ""

git push 

### git 중급으로 넘어가기

빈파일 touch logfile 

touch .gitignore

logfile 

gitignore 파일 





git branch about-page

branch의 역할 



두개 합치기 git merge about-page 

master에서 합치는 명령어 실행해야 한다. 

master에서는 합병을 주로 한다. 

git branch -d about-page  깃 브랜치 지우기 



 git checkout -b help-page 한방에 생성하기 

rm *.html 



### git 협업

```python
github에 new 레지토리 생성 
상대방 초대 

git init 
git config --global user.name ""
git config --global user.email ""

vim ~/.gitconfig
a 쓰고  core를 vim으로 바꾸기 
wq 저장 
git add .
git commit -m ""
git push 

git clone 누구나 가능 "" 주소복사 


b인 사람 



동시에 작업하는 경우 
git pull 합의를 해서 꼭 하나의 상황을 만든다. 

```

### git 

- repo는 해당 폴더에 있는 모든 파일과 하위 디렉토리 변화를 추적하는 directory봐도 무방
- init 명령어 사용 Git이 우리의 프로젝트 변경

