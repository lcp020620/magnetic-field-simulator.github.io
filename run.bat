@echo off
:: 'venv' 폴더가 없으면 새로 만듭니다.
if not exist "venv" (
    echo Generating Vircual environment...
    python -m venv venv
)

:: 가상환경 활성화 후 라이브러리 설치
call venv\Scripts\activate
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [error] There was an issue during library installation. 
    echo Check your python version or internet connection.
    pause
)

:: 프로그램 실행
python app.py

exit