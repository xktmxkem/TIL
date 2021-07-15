# Git 이란?

### 형상 관리 도구(Configuration Management Tool)

![Git을 사용한 버전 관리 소개 (2018 업데이트)](data:image/png;base64,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)

Open Source 기반의 **버전 관리 툴**

쉽게 말해 스크린 샷을 찍듯이 개발해 나가는 과정을 기록해 나가는 일기장 이라 생각하면 된다.

SVN과 다르게 소스 코드를 여러 개발 PC와 저장소에 분산해서 저장하며, 로컬 혹은 중앙 저장소에 장애가 생기더라도 복원이 가능하다.

Git과 연계된 서비스로는 Git Hub, Git Lab, Bit Bucket 등이 있는데 단순히 로컬,원격 저장소의 차이 정도로 생각하는게 편하다

--------



> # Git 명령어 
>
> 
>
> > ### 1. git init
> >
> > * 로컬 저장소에 사용할 폴더 내에서 git bash를 실행 후 명령어를 입력한다
> >
> > * .git 라는 숨겨진 파일이 생성되며 git 저장소로 사용되게 된다. 
> >
> > * .git 디렉토리에는 저장소에 필요한 뼈대 파일(Skeleton)이 들어있다.
> >
> > * 사용법
> >
> >   ```python
> >   git init
> >   ```
> >
> > ### 2. git status
> >
> > * 파일 상태 확인 명령어이다.
> >
> > * 각 논리적 스테이지 Working Directory, Staging Area, Commit에 있는 파일들을 
> >
> >   보여주며 새롭게 추가, 수정, 명령어 수행 상태 등을 볼 수 있다.
> >
> > >#### **※** 파일상태 2가지
> > >
> > >1. **Untracked** 상태
> > >
> > >   - Staging Area에 올라오지 않은 상태의 파일으로 원하는 파일을 add하면 
> > >
> > >     디렉토리에 올릴 수 있다.
> > >
> > >2. **Tracked** 상태
> > >
> > >   - 파일이 git에 의해 변동사항이 추적되는 상태이다. 이 상태에는 각 논리적 스테이지에 따라 나뉜다.
> > >
> > >   2.1 **Staged** 상태 : 파일 수정 후 staging area에 올라가 있는 상태(commit 후 상태)
> > >
> > >   2.2 **Unmodified** 상태 : 현재 파일이 최신 커밋 파일과 비교해 다른게 없는 상태
> > >
> > >   2.3 **Modified** 상태 : 현재 파일이 최신 커밋 파일과 비교해 다른 상태
> >
> > * 사용법
> >
> > ```python
> > git status
> > ```
> >
> > ### 3. git add
> >
> > * Working Directory 내에는 있지만 Staging Area에 올라오지 않은 상태의 파일을 Staging Area에 올리는 명령어이다.
> >
> > * 이때 .gitignore.txt 파일을 같은 디렉토리 내에 생성하여 내부에 올리지 않을 파일 명들을 입력하면 git add . 명령어를 사용하더라도 파일 내에 적힌 자료들을 올리지 않을 수 있다.
> >
> > * .gitignore의 경우  <https://www.toptal.com/developers/gitignore> 에 접속하여 본인이 사용하는 OS, 편집 툴, 언어를 입력하면 별도의 추가 없이 복사 붙여넣기로 편리하게 완성할 수 있다.
> >
> > * 사용법
> >
> >   ```phthon
> >   git add [파일명]
> >   ```
> >
> >   ```python
> >   git add .
> >   ```
> >
> >   ```python
> >   git add --all
> >   ```
> >
> >   ```python
> >   git add -A
> >   ```
> >
> > ### 4. git rm
> >
> > * git으로 관리(Tracked) 즉, 추적되는 파일 혹은 폴더를 제거하고자 할 때 사용되는 명령어 이다.
> > * 명령어의 옵션에 따라 삭제할 수 있는 파일의 위치가 달라진다
> >
> > > ##### 1. 로컬과 원격 저장소 모두에서 파일을 삭제하기를 원한다면
> > >
> > > * 순서대로 실행시키면 로컬(git)과 원격(git hub 등)에서 모두 삭제된다.
> > >
> > > ```python
> > > git rm [파일명]
> > > ```
> > >
> > > ```python
> > > git commit -m "커밋내용"
> > > ```
> > >
> > > ##### 2. 원격 저장소에서만 삭제할 경우
> > >
> > > * 순서대로 실행시키면 원격 저장소에서 삭제된다.
> > >
> > > ```python
> > > git rm --cached [파일명]
> > > ```
> > >
> > > ```python
> > > git commit -m "커밋내용"
> > > ```
> > >
> > > ##### 3. 강제삭제
> > >
> > > * 삭제하려는 파일 내용이 브랜치 끝 부분에서의 내용과 다를 경우 강제 삭제
> > >
> > > ```python
> > > git rm -f
> > > ```
> > >
> > > ```python
> > > git rm --force
> > > ```
> >
> > ### 5. git commit
> >
> > * 변경사항 확정에 사용하는 명령어이다.
> > * Staging Area에 올라와 있는 파일들을 Commit 저장소로 보내는 명령어이다.
> > * 커밋 메세지는 다중으로 처리 가능하며 여러개의 -m을 사용한다.
> >
> > > ###### 1. add와 commit을 동시에
> > >
> > > * 한 번도 add 되지 않은 파일의 경우, 따로 add 작업을 해줘야 한다.
> > >
> > > ```python
> > > git commit -a
> > > ```
> > >
> > > ##### 2. 커밋 메세지에 diff의 내용 포함
> > >
> > > ```python
> > > git commit -v
> > > ```
> > >
> > > ##### 3. 최신 커밋 메세지 수정하여 커밋
> > >
> > > * 신규 커밋 메세지를 추가 않고 제일 최근에 커밋한 메세지를 수정하여 올릴 수 있다.
> > >
> > > ```python
> > > git comomit --amend
> > > ```
> > >
> > > ##### 4. a, m 옵션을 합친 형태
> > >
> > > ```python
> > > git commit -am
> > > ```
> >
> > ### 6. git diff
> >
> > * 마지막 커밋과 staging area의 차이 확인
> >
> > ```python
> > git diff --staged
> > ```
> >
> > * 두 커밋 ID간의 차이 확인
> >
> > ```python
> > git diff [커밋 id] [커밋 id]
> > ```
> >
> > ### 7. git remote
> >
> > * 로컬 저장소와 원격 저장소를 연결하기 위해 사용하는 명령어이다
> > * 주로 github에서 repository를 생성한 후 .git 파일이 있는 로컬 저장소와 연결을 할 때 사용한다.
> > * 여기서 origin은 긴 repository 주소를 별칭으로 지정해 앞으로 사용할 명령어에서 단순하게 호출하기 위해 사용한다. 
> >
> > ```python
> > git remote add origin [repository 주소]
> > ```
> >
> > * 추가한 원격 저장소의 목록 확인
> >
> > ```python
> > git remote 
> > ```
> >
> > ```python
> > git remote -v
> > ```
> >
> > * 특정 원격 저장소의 정보 확인
> >
> > ```python
> > git remote show [이름]
> > ```
> >
> > * 원격 저장소 제거
> >
> > ```python
> > git remote rm [이름]
> > ```
> >
> > ### 8. git push
> >
> > * 로컬 저장소(Commit Area)에 있는 파일들을 원격 저장소(git hub)에 추가 하는 명령어.
> > * 파라미터(별칭)가 따로 없으면 origin 저장소에 푸시한다.
> >
> > ```python
> > git push [원격 저장소 이름(별칭)][브랜치명]
> > ```
> >
> > ### 9. git clone
> >
> > * 초기에 로컬 저장소에 아무런 파일이 없을때 원격 저장소에서 가져오는 명령어이다. 
> >
> > ```python
> > git clone [remote repo 주소]
> > ```
> >
> > ### 10. git pull
> >
> > * git fetch에서 하는 원격저장소의 변경사항을 가져와서 지역브랜치에 합치는 작업
> > * 쉽게 얘기해서 다른 사람들의 작업 변경 사항을 내 로컬 저장소로 가져온다.
> > * clone과 달리 원격 저장소의 파일이 어느정도 있을 때 변경사항 관리용으로 사용

---

###### 이 외에도 여러 명령어가 있지만 차차 업데이트 하도록 하겠다.



