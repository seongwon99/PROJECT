from flask import Flask, render_template,Blueprint, request


bp = Blueprint("db",__name__,url_prefix="/db")



# DB에 데이터 추가
@bp.route('/user_insert', methods=['POST'])
def user_insert():
    name=request.form['name']
    one=request.form['water']
    two=request.form['prot']
    three=request.form['fat']
    four=request.form['carb']

    from main.db_model import User
    user1=User(Food=name, Water=one, Protein=two, Fat=three, Carbohydrate=four)
    db.session.add(user1)
    db.session.commit()

    # return 쓴다 안쓴다


# DB에서 사용자 목록 요청
@bp.route('/user_list')
def user_list():
    from db_model import User


    datas=User.query.order_by(User.created_at.desc())
    return render_template('check.html', user_list=datas)