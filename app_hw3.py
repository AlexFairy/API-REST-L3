#resort to method 1-6 in baby steps
#use template for anything

#MUST BE RUN IN A VIRTUAL ENVIRONMENT
#Step 1: import flask & flask sql alchemy
#Step 2: connect to MYSQL project
#Step 3: create the ORM model
#Step 4: initialize database
#Step 5: make the routes
#Step 6: run app

#format
#the actual file name (app_hw3.pay) is used to set route
    #@filename.route('/MYSQLtable/<int:primary_key value>, methods=['CRUD]')
        #function

#Extra notes
#Must use parameter when ['GET'] is retrieving single data

#1
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#2
app_hw3 = Flask(__name__)
app_hw3.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Bebop1216!@localhost/gym_db'
db = SQLAlchemy(app_hw3)  # This will be used for the ORM model

#3
# note: on MYSQL, integer is int while in ORM it's written out!
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

class WorkoutSessions(db.Model):
    session_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    session_time = db.Column(db.String(50), nullable=False)
    activity = db.Column(db.String(255), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)

#4
with app_hw3.app_context():
    db.create_all()

#5: Make the routes
#GET individual for MEMBER
@app_hw3.route('/members/<int:id>', methods=['GET'])
def memberGet(id):
    member = Member.query.get(id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    return jsonify({'id': member.id, 
                    'name': member.name, 
                    'age': member.age})

#GET individual for WORKOUTSESSION
@app_hw3.route('/workoutsessions/<int:session_id>', methods=['GET'])
def workoutsessionGet(session_id):
    workoutsession = WorkoutSessions.query.get(session_id)
    if not workoutsession:
        return jsonify({'error': 'Workout session not found'}), 404
    return jsonify({
        'session_id': workoutsession.session_id,
        'member_id': workoutsession.member_id,
        'session_date': str(workoutsession.session_date),
        'session_time': workoutsession.session_time,
        'activity': workoutsession.activity,
        'duration_minutes': workoutsession.duration_minutes,
        'calories_burned': workoutsession.calories_burned})

#GET all for MEMBER
@app_hw3.route('/members', methods=['GET'])
def membersGet():
    members = Member.query.all() #.all() gets everything from mysql data
    return jsonify([{'id': x.id, 
                     'name': x.name, 
                     'age': x.age} for x in members])

#GET all for WORKOUT SESSIONS
@app_hw3.route('/workoutsessions', methods=['GET'])
def workoutsessionsGet():
    workoutsessions = WorkoutSessions.query.all() #.all() gets everything from mysql data
    return jsonify([{
        'session_id': x.session_id,
        'member_id': x.member_id,
        'session_date': str(x.session_date), 
        'session_time': x.session_time,
        'activity': x.activity,
        'duration_minutes': x.duration_minutes,
        'calories_burned': x.calories_burned} for x in workoutsessions])

#POST for MEMBER
@app_hw3.route('/members', methods=['POST'])
def memberPOST():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'age' not in data:
        return jsonify({'error': 'Invalid'}), 400
    try:
        new_member = Member(id=data['id'], name=data['name'], age=data['age'])
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Member added successfully!', 'id': new_member.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# POST for WORKOUT SESSIONS
@app_hw3.route('/workoutsessions', methods=['POST'])
def workoutsessionPOST():
    data = request.get_json()
    if not data or 'session_id' not in data or 'member_id' not in data or 'session_date' not in data or 'session_time' not in data or 'activity' not in data:
        return jsonify({'error': 'Invalid'}), 400
    try:
        session_date = datetime.strptime(data['session_date'], "%Y-%m-%d").date()
        new_workoutsession = WorkoutSessions(
            session_id=data['session_id'],
            member_id=data['member_id'],
            session_date=session_date,
            session_time=data['session_time'],
            activity=data['activity'],
            duration_minutes=data['duration_minutes'],
            calories_burned=data['calories_burned']
        )
        db.session.add(new_workoutsession)
        db.session.commit()
        return jsonify({'message': 'Workout session added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# PUT for MEMBERS
@app_hw3.route('/members/<int:id>', methods=['PUT'])
def memberPUT(id):
    member = Member.query.get(id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    data = request.get_json()
    try:
        member.name = data.get('name', member.name)
        member.age = data.get('age', member.age)
        db.session.commit()
        return jsonify({'message': 'Updated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# PUT for WORKOUT SESSIONS
@app_hw3.route('/workoutsessions/<int:session_id>', methods=['PUT'])
def workoutsessionPUT(session_id):
    workoutsession = WorkoutSessions.query.get(session_id)
    if not workoutsession:
        return jsonify({'error': 'Workout session not found'}), 404
    data = request.get_json()
    try:
        workoutsession.member_id = data.get('member_id', workoutsession.member_id)
        workoutsession.session_date = datetime.strptime(data.get('session_date', str(workoutsession.session_date)), "%Y-%m-%d").date()
        workoutsession.session_time = data.get('session_time', workoutsession.session_time)
        workoutsession.activity = data.get('activity', workoutsession.activity)
        workoutsession.duration_minutes = data.get('duration_minutes', workoutsession.duration_minutes)
        workoutsession.calories_burned = data.get('calories_burned', workoutsession.calories_burned)
        db.session.commit()
        return jsonify({'message': 'Updated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

#DELETE for MEMBERS
@app_hw3.route('/members/<int:id>', methods=['DELETE'])
def memberDELETE(id):
    member = Member.query.get(id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    try:
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Deleted successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

#DELETE for WORKOUT SESSIONS
@app_hw3.route('/workoutsessions/<int:session_id>', methods=['DELETE'])
def workoutsessionDELETE(session_id):
    workoutsession = WorkoutSessions.query.get(session_id)
    if not workoutsession:
        return jsonify({'error': 'Workout session not found'}), 404
    try:
        db.session.delete(workoutsession)
        db.session.commit()
        return jsonify({'message': 'Deleted successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

#6
if __name__ == '__main__':
    app_hw3.run(debug=True)