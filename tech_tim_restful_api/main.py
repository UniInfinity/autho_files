from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video", required=True)
video_put_args.add_argument("views", type=int, help="views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="likes of the video", required=True)


video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="name of the video")
video_update_args.add_argument("views", type=int, help="views of the video")
video_update_args.add_argument("likes", type=int, help="likes of the video")



resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="could not find video with that id")

        return result


    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="video id taken....")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201


    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video doesnt exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        
        return result        



    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video doesnt exist, cannot delete")
        
        del result[video_id]
        
        # db.session.delete(result)
        db.session.commit()
        
        return result



api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)


































    '''--------------------'''
    # 1
    # class HelloWorld(Resource):
    # def get(self):
    #     return {'Data':'Hello World'}

    # def post(self):
    #     return {'POST':'Posted'}
    '''-------------------'''
# 2
#videos = {}

# def abort_if_video_id_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, message="video id is not valid")

# def abort_if_video_id_exist(video_id):
#     if video_id in videos:
#         abort(409, message="video already exist with this ID.....")
'''----------------------------------------------------------------------'''


