from app import db

class Code(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	code = db.Column(db.String(1000))



	def __init__(self,code):
		self.code = code