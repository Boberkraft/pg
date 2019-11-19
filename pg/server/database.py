
from pg.server import db
from flask import Flask




class UnprocessedScrapedPage(db.Model):
    __tablename__ = 'unprocessed_scraped_page'
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.String(100000), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<UnprocessedScrapedPage id: {self.id}, size: {len(self.html)}>"


class ScrapedPage(db.Model):
    __tablename__ = 'scraped_page'
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.Integer, nullable=True)
    generation = db.Column(db.Integer, nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    quiz = db.relationship("Quiz")
    html = db.Column(db.String(10000), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<ScrapedPage id: {self.id}, size: {len(self.html)}>"


class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.Integer, nullable=True)
    questions = db.relationship('Question')

    def __repr__(self):
        return f"<Quiz id: {self.id} >"


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.Integer, nullable=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    generation = db.Column(db.Integer, nullable=False, default=1)
    type = db.Column(db.String(1000), nullable=False)
    html = db.Column(db.String(10000), nullable=False)
    answer = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f"<Question id: {self.id}, quiz_id: {self.quiz_id}>"

def show():
    pages = UnprocessedScrapedPage.query.all()
    for page in pages:
        pass

if __name__ == '__main__':

    DATABASE_PATH = 'test.db'

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"
    db.init_app(app)
    # db.create_all()


