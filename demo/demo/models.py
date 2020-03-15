from demo import db


class Model(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


user_course = db.Table(
    "user_course",
    db.Column("id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"))
)


class User(Model):
    name = db.Column(db.String(32))
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    course = db.relationship("Course", secondary=user_course, backref="user")


class Role(Model):
    r_name = db.Column(db.String(32))
    description = db.Column(db.String(32))
    user = db.relationship("User", backref="role_set")


class Course(Model):
    name = db.Column(db.String(32))
    description = db.Column(db.String(32))


db.create_all()
