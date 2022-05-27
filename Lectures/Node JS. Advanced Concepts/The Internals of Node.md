강의 4 ~
# [[NodeJS]] 구조

![[Screen Shot 2022-03-20 at 12.43.45 PM.png]]

- 가장 상단에 js 파일에 있는 Javascript 코드가 있음
- `node index.js` 명령어로 파일 내 코드를 실행시킴

[[NodeJS]]
- JS 코드를 실행시키기 위한 여러가지 dependencies 콜렉션이 있음, 이 중 가장 중요한 두 가지
	- [[V8]]
	- [[libuv]]
- [[NodeJS]] 목적
	1. Node는 [[Javascript]] [[애플리케이션]]을 [[C++]] 로 코드로 연결하는 [[인터페이스]] 제공
		- [[V8]] 과 [[libuv]] 를 직접 사용하지 않고, NodeJS 를 거치는 이유는 무엇일까?
		- 해당 라이브러리가 JS 코드로만 구성되어있지 않기 때문
		- [[NodeJS]] 는 이 [[C++]] 언어로 구성된 라이브러리 연결
	2. wrapper 와 프로젝트에서 사용할 수 있는 일관된 API  제공 (http, fs, crypto, path 등)
		- 이러한 라이브러리들은 대부분 [[libuv]]에 내장됨
		- [[C++]] 코드에 대한 접근 없이도 편리하게 [[Javascript|JS]] 코드에서 위 기능을 이용할 수 있음
- **실제 [[NodeJS]]를 통해 돌아가는 [[Javascript|JS]] 코드들은 [[C++]] 에 의존**

[[V8]]
- Open Source Javascript Engine
- 구글
- Javascript 코드를 웹 브라우저 외부에서 실행될 수 있도록 함
- [[Javascript]] 로 작성된 코드의 내용을 [[C++]] 코드로 동일하게 번역함
- [[C++]] 70%, [[Javascript]] 30% 

[[libuv]]
- [[C++]] 오픈소스 프로젝트
- Node 가 [[파일 시스템]], [[네트워크]] 등 [[운영체제]]에 접근할 수 있도록 함
- [[병행성]] 을 관리
- [[C++]] 100%

---
**[Node.JS github](https://github.com/nodejs/node/tree/master) 구조**
- `libs`: 프로젝트에서 사용하는 함수 및 모듈들에 대한 [[Javascript|JS]] 정의가 들어있음
	- [[NodeJS]]의 Javascript Side 라고 보면 됨
- `src`: 프로젝트에서 사용하는 함수 및 모듈들에 대한 [[C++]] 구현이 들어있음
	- fs, http 모듈 등
---
[[NodeJS]] 톺아보기
1. Node Standard Library 중 기능 하나를 고름
	- `pbkdf2` ('crypto' 라이브러리 내)
2. Node Source Code 중 어디에 해당 기능이 구현되어있는지 찾아봄
	-  [`libs/internal/crypto/pbkdf2.js`](https://github.com/nodejs/node/blob/master/lib/internal/crypto/pbkdf2.js)
	- `pbkdf2()` [[Javascript|JS]] 코드가 작성되어 있으며, 내부에서는 다시 [[C++]] 코드를 호출 (`PBKDF2Job`)
	- `PBKDF2Job` 는 `internalBinding('crypto')` 를 통해 가져오고 있음
3. 해당 기능에서 [[V8]]과 [[libuv]] 가 어떻게 사용되는지 알아보기
	- 실제 `PBKDF2Job` 구현은 [`src/node_crypto.cc`](https://github.com/nodejs/node/blob/master/src/node_crypto.cc) 에 구현
	- 과거에는 5000줄이 넘는 대형 파일이었는데, 현재는 `crypto` 폴더 내에 쪼개져 있음
	- `PBKDF2Job` 은 [`src/crypto/crypto_pbkdf2.cc`](https://github.com/nodejs/node/blob/master/src/crypto/crypto_pbkdf2.cc) 에 구현
	- **[[V8]] 의 활용**
		- `using v8::` 형태로 [[V8]] 을 통해 각 [[Javascript|JS]] 코드에 대한 [[C++]] 정의를 가져오고 있음
	- **[[libuv]]의 활용**
		- `uv_` 형태로 붙어서 정의되어있음
		- [[C++]] 사이드에서 각종 [[병행성]] 및 [[프로세스]] 처리를 수행

![[Screen Shot 2022-03-20 at 3.10.10 PM.png]]
`process.binding()` 은 Node 11.x 버전부터 `internalBinding()` 으로 바뀜
`internalBinding()` 은 [[Javascript|JS]]와 [[C++]] 를 연결해주는 역할!

---
강의 7 ~
# [[Event Loop]]

## [[프로세스]]
- [[컴퓨터]]에서 [[프로그램]]을 실행하면, [[프로세스]] 형태로 인스턴스가 구성
- 하나의 [[프로세스]]는 여러개의 [[스레드]]를 가질 수 있음
- [[스레드]]는 [[CPU]]에 의해 처리되어야 할 일련의 작업들이라고 생각하면 됨
- 아래 그림을 보면 759개의 [[프로세스]]와 3,937개의 [[스레드]]가 실행 중인 것을 알 수 있음
![[Screen Shot 2022-03-20 at 4.07.55 PM.png]]
## [[스케줄링]]
**[[스케줄링]]은 [[스레드]]를 이해하는데 중요한 요소**
- [[운영체제]]에서 특정 시점에 어떤 [[스레드]]를 먼저 처리할 것인지를 결정하는 능력
- [[컴퓨터]]에는 제한된 자원만 잇고, [[CPU]]가 한 번에 처리할 수 있는 능력에는 제한이 있음
- [[운영체제]]의 [[스케줄러]]는 처리 요청이 들어온 모든 [[스레드]]를 분석한 후, 중요한 작업을 먼저 처리하는 등의 작업을 수행
- 예를 들어 [[마우스]] 움직임에 따라 커서를 움직이는 작업을 담은 [[스레드]]가 늦게 처리된다면, 커서 움직임에 지연이 생겨 불편함을 느낄 것

## [[스레드]] 처리
**[[스레드]] 처리 작업을 빠르게 개선하는 방법**
1. [[CPU]] 코어 갯수를 늘림으로써 여러 개의 [[스레드]]를 한 번에 처리.
	![[Screen Shot 2022-03-20 at 4.15.55 PM.png]]
	각 코어는 [[멀티 스레딩]]을 통해서 한 번에 하나 이상의 [[스레드]]를 처리할 수 있음
2. [[스레드]]의 필요 작업([[I/O]], [[CPU]] 활용 등) 을 평가하여 작업을 효율적으로 배분
	![[Screen Shot 2022-03-20 at 4.18.09 PM.png]]
	각 스레드 작업에 필요한 자원들을 평가하고, [[I/O]] 작업등이 수행되어서 [[CPU]] 자원이 잠시 필요하지 않는 순간에, 해당 [[스레드]] 작업을 잠시 멈추고, 다른 [[스레드]] 작업을  수행할 수 있음

## [[NodeJS]]: 싱글 [[스레드]]
- [[NodeJS]]는 하나의 [[스레드]]만을 활용함
	![[Screen Shot 2022-03-20 at 4.23.25 PM.png]]
- 해당 싱글 [[스레드]] 내부에 [[이벤트 루프]]가 존재함

## 이벤트 루프
- [[NodeJS]]에 존재하는 싱글 [[스레드]]에서 특정 시점에 어떤 작업을 수행해야하는지 제어하는 구조
- [[NodeJS|Node]] 프로그램의 핵심이며, 모든 [[NodeJS|Node]]프로그램은 하나의 [[이벤트 루프]]만 가지고 있음
- [[NodeJS|Node]]의 퍼포먼스 이슈 대부분은 [[이벤트 루프]]의 동작과 관련되어 있기 때문에, [[이벤트 루프]]를 이해하는 것이 중요하다.

### 동작 과정의 이해
- [[이벤트 루프]] 동작 과정을 이해하는 것은 꽤 어려운데, 여기에서는 fake Code 를 작성해서, [[NodeJS|Node]] [[애플리케이션]]이 시작하고 종료되는 과정을 작성해보면서 이해

```js
// node myFile.js

myFile.runContents();

// exit back to terminal
```

- `node` 명령어를 통해 파일이 실행되더라도 [[이벤트 루프]]는 바로 실행되지 않는다.
- [[NodeJS]]는 실행 파일의 내용을 먼저 실행한 이후, [[이벤트 루프]]로 들어감
- 