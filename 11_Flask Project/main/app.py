from flask import Flask, render_template, request, url_for, redirect
from joblib import dump,load
from sklearn.preprocessing import StandardScaler
from db_create import bp

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 인스턴스 생성
test_model = load(r'C:\Users\KDP-48\Desktop\flask 프로젝트\model\classifier_model.joblib')
test_scaler=load(r'C:\Users\KDP-48\Desktop\flask 프로젝트\model\classifier_scaler.joblib')

db=SQLAlchemy()
migrate=Migrate()


def create_app():
    app=Flask(__name__)
    app.register_blueprint(bp)

    app.config.from_pyfile('config.py')
    print(f'app.config["DEBUG"] => {app.config["DEBUG"]}')

    # ORN 연동
    import db_model

    
    db.init_app(app)
    migrate.init_app(app,db)

    

    # http://127.0.0.1:5010/
    @app.route('/')
    def home(): return render_template('main.html')

    @app.route('/submitpage')
    def sub(): return render_template('submit.html')

    @app.route('/checkpage')
    def check():
       # DB에 등록된 회원조회 데이터 전달
        from db_model import User
        users=User.query.order_by(User.id)
        
        return render_template('check.html', user_list =users)

    @app.route('/find',methods=["POST"])
    def search_result():
        name=request.form['name']
        one=request.form['water']
        two=request.form['prot']
        three=request.form['fat']
        four=request.form['carb']

        input_=[[one,two,three,four]]
        input_scaled=test_scaler.transform(input_)
        result_=test_model.predict(input_scaled)

        result_2=None

        print(result_)
        if result_==[0]: result_2= "곡류군"
        elif result_==[1]: result_2= "과일군"
        elif result_==[2]: result_2= "어육류군"
        elif result_==[3]: result_2= "우유군"
        elif result_==[4]: result_2= "지방군"
        else: result_2= "채소군"

        list1 =[]
        list1.append(name)
        list1.append(result_2)



        #디비 등록
        from db_model import User
        user1=User(Food=name, Water=one, Protein=two, Fat=three, Carbohydrate=four, Result=result_2)
        db.session.add(user1)
        db.session.commit()



        return render_template('submit.html',group=list1)


    return app



if __name__=='__main__':
    create_app().run(debug=True)
