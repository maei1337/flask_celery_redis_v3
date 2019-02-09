from flask import Flask
from flask_restful import Api, Resource

from celery import Celery

celery = Celery(
                'tasks',
                broker='redis://redis:6379',
                backend='redis://redis:6379'
)

app = Flask(__name__)
api = Api(app)

class add_zahl(Resource):
    def post(self, zahl):
        task = celery.send_task('mytasks.add', args=[zahl])
        return {'message': 'Prozess {} gestartet'.format(task.id)}, 200

api.add_resource(add_zahl, "/add/<int:zahl>")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
