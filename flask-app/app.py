from flask import Flask
from flask_restful import Api, Resource

from celery import Celery
from celery.result import AsyncResult
import celery.states as states
import celeryconfig

celery = Celery('tasks')

celery.config_from_object('celeryconfig')

celery.conf.update({
    'task_routes': {
        'mytasks.add': {'queue': 'queue1'},
        'mytasks.sub': {'queue': 'queue2'}
    }
})

app = Flask(__name__)
api = Api(app)

class add_zahl(Resource):
    def post(self, zahl):
        task = celery.send_task('mytasks.add', args=[zahl]) #,queue='queue_name'
        return {'message': f"Prozess {task.id} gestartet, input {zahl}"}, 200

class sub_zahl(Resource):
    def post(self, zahl):
        task = celery.send_task('mytasks.sub', args=[zahl]) #, queue='queue2'
        return {'message': f"Prozess {task.id} gestartet, input {zahl}"}, 200

class ergebnis(Resource):
    def get(self, task_id):
        res = celery.AsyncResult(task_id)
        return res.state if res.state==states.PENDING else str(res.result)


api.add_resource(add_zahl, "/add/<int:zahl>")
api.add_resource(sub_zahl, "/sub/<int:zahl>")
api.add_resource(ergebnis, "/ergebnis/<task_id>")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
