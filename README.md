# fast-api

1.환경

    Python3.9
    Fast-Api

2.SETUP

    //가상화 설치 
    python -m venv .venv

    . .venv/bin/activate

    pip install --upgrade pip

    //패키지 설치
    pip install -r requirements.txt

    //패키지 export
    pip freeze > requirements.txt

    uvicorn app.main:app --reload
    
3.docs

    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
    

4.sqlacodegen

    # Make DB ddl to sqlalchemy models
    sqlacodegen "drive://username:password@host:port/dbname" > models.py

    # example
    sqlacodegen "mysql+pymysql://root:@localhost:3306/ktown4u-api" > models.py