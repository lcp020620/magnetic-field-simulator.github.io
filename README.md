# 🧲 자기장 시뮬레이터 (FEM Based Magnetic Field Simulator)
# [Click here for English!](https://lcp020620.github.io/ENGLISH-magnetic-field-simulator/)

## **[이걸 눌러 다운로드하세요!](https://github.com/lcp020620/magnetic-field-simulator.github.io/archive/refs/heads/main.zip)**

## **🛠️ 이 프로젝트에 사용된 언어와 라이브러리**

본 프로젝트는 고성능 GPU 연산과 인터랙티브한 3D 시각화를 위해 아래 라이브러리들을 활용합니다.

| 언어 | 라이브러리 | 용도 | 공식 문서 url |
| :--- | :--- | :--- | :---: |
| **Python** | **CuPy** | GPU 기반 병렬 컴퓨팅 구현 | [CuPy](https://cupy.dev) |
| | **NumPy** | GPU 연산 결과 후처리 | [Numpy](https://numpy.org/) |
| | **Flask** | 로컬 웹 서버 구축 및 자기장 데이터 상호작용  | [Flask](https://flask.palletsprojects.com) |
| **JavaScript** | **Three.js** | 웹 브라우저 기반 실시간 자기장 시각화 | [Three.js](https://threejs.org) |

**"눈에 보이지 않는 자기장, 이제 직접 설계하고 3D로 확인하세요!"**  
본 프로젝트는 [**유한요소법(FEM)**](https://en.wikipedia.org/wiki/Finite_element_method) 을 활용하여 임의의 전류 배치에 따른 자기장의 세기와 방향을 계산하고 시각화하는 시뮬레이터입니다.

연구 또는 교육 목적이라면 마음껏 사용하세요.(코드 변형 가능, 2차 배포 불가) 공유하시려면 이 페이지의 url을 공유하세요~!

**[COMSOL](https://www.comsol.com/)이 너무 비싸서 부담되는 학생들을 위해 만들었습니다!** 무료로 자기장 시뮬레이터를 사용해보세요.

**그래픽 카드 없어도 Google Colab에서 실행 가능해요!**

---

## **프로젝트 소개 및 튜토리얼 Youtube 영상**
시뮬레이터의 작동 모습과 사용법을 영상으로 확인해 보세요!

| 🎥 컴퓨터로 직접 실행하는 방법 | 💻 Google Colab에서 실행하는 방법 |
| :---: | :---: |
| [![Intro](https://img.youtube.com/vi/XghdGBYB3hE/0.jpg)](https://youtu.be/XghdGBYB3hE) | [![Colab](https://img.youtube.com/vi/CR1B1KkAaRE/0.jpg)](https://youtu.be/CR1B1KkAaRE) |
| *자기장 시뮬레이션의 핵심 기능 소개* | *GPU가 없어도 웹에서 바로 실행하는 방법* |

---

## ** ✨ 핵심 기능**
- **3D 벡터 시각화**: 각 지점의 자기장 방향과 세기를 3D 화살표로 즉시 확인 (6개 열로 구성된 `.csv` 파일이면 다 시각화돼요!)
- **다양한 전류 설정**: 전류의 형태(원 또는 선분), 세기(Ampere), 위치(3D Vector)를 자유롭게 배치
- **정밀도 조절**: Mesh Dense와 Vector Dense 변수를 통해 시뮬레이션 해상도 조절
- **데이터 내보내기**: 결과값을 [Microsoft Excel](https://www.microsoft.com/ko-kr/microsoft-365/excel) 등에서 분석 가능한 `.csv` 파일로 저장

---

## **🛠 컴퓨터에서 직접 돌리시려면 NVIDIA 그래픽카드가 필요해요! 없으시다면 [Google Colab](https://youtu.be/CR1B1KkAaRE)에서 실행하세요~**
이 프로그램은 고성능 연산을 위해 **NVIDIA GPU(CUDA)**를 사용합니다.
- **그래픽카드**: NVIDIA 그래픽카드 필수 (CUDA 연산 지원)
- **run.bat 파일을 실행해 자동 설치**: `run.bat` 파일 실행 시 가상 환경과 필수 라이브러리가 자동으로 설치됩니다.
- **제 컴퓨터 환경**: CUDA 13.1, CuPy 13.6.0, NumPy 2.4.0 (라이브러리 관련 문제가 생겼다면, 이것과 비슷한 버전들을 설치해보세요.)


---

## **🚀 GPU가 있는 경우 사용 방법(축하드려요! 부자시네요!)**

### 0. 프로그램 다운로드
 - [여기](https://github.com/lcp020620/magnetic-field-simulator.github.io/archive/refs/heads/main.zip)를 눌러 ZIP 압축 파일을 다운로드하세요.
 - 압축 해제하시고 폴더에 들어가세요.

### 1. 프로그램 실행
 - `run.bat` 파일을 실행하면 필수 라이브러리를 설치하고 로컬 서버가 구동됩니다. "알 수 없는 게시자" 경고는 제가 돈이 없어서 전자서명 배포를 못 해서 그런거에요. 악성 바이러스는 없습니다. (처음 가동에는 시간이 걸려요.)
 - 자동으로 인터페이스가 켜지지 않는다면 웹 브라우저에 [127.0.0.1:5000](http://127.0.0.1:5000)을 입력하세요.

### 2. 시뮬레이션 설정
- **Step 0**: 시뮬레이션 공간 크기와 **Mesh Dense**(격자 밀도)를 설정합니다.
- **Step 1**: 전류 정보를 입력(형태, 세기, 좌표)하고 **Request** 버튼을 눌러 목록에 추가합니다.
- **Step 2**: 모든 설정이 완료되면 **Start Simulation**을 클릭합니다. [CuPy Library](https://cupy.dev)를 이용해 GPU 계산이 시작됩니다.

### 3. 결과 확인 및 종료
- 계산이 끝나면 [Three.js](https://threejs.org)로 렌더링된 3D 자기장 벡터가 표시됩니다.
- **Download as .csv** 버튼을 눌러 데이터를 `.csv` 파일로 저장할 수 있습니다.
- **Simulation Turn Off** 버튼을 눌러 프로그램 종료하세요. 이 버튼을 눌러 백그라운드 프로세스를 완전히 종료할 수 있습니다.
- **Go back to Simulation settings** 버튼을 눌러 시뮬레이션 설정 화면으로 돌아가세요. 시뮬레이션 공간 정의와 전류 정보 입력을 처음부터 하실 수 있습니다.

---

## **🤝 도움이 필요해요!**
본 프로젝트는 학생들이 무료로 자기장을 연구할 학문적 도구를 제공하기 위해 개발된 1인 프로젝트입니다.

아래 이슈들에 대한 피드백과 도움을 환영합니다!

1. **자기력선 시각화**: 지저분한 화살표 대신 자기력선을 매끄러운 선(Streamlines)으로 연결하는 기능.
2. **배포 최적화**: [PyInstaller](https://pyinstaller.org) 사용 시 CUDA DLL 인식 오류 해결 및 단일 `.exe` 패키징.
3. **시각화 성능**: 특정 영역만 선택적으로 렌더링하여 벡터 겹침 현상 해소.
4. **웹 서버화**: 저사양 기기에서도 접속 가능한 GPU 클라우드 서버 구축. (현재 Google Colab으로 일부 해결됨)
5. **UI/UX 개선**: 시뮬레이션 시각화 페이지의 창 닫기(`window.close()`)가 안되는 버그. (Chrome의 보안 방침 변경으로 새로운 방법 필요)
6. **동적 메시 할당**: 사용자가 관심 있는 특정 영역을 더 세밀하게 시뮬레이션하는 기능.

---

## **📝 라이선스 (License)**
본 프로그램은 **교육 및 연구 목적으로 누구나 자유롭게 사용**할 수 있습니다. 별도의 허가 없이 수업이나 개인 공부에 활용해 보세요! 🎓

2차 배포는 금지됩니다.

---
*개발자에게 피드백을 주고 싶거나 문의가 있다면 github 문의나 이메일(lcp020620@kaist.ac.kr)을 남겨주세요.*
