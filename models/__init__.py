class Temp(db.Model):
	id = self.db.Column(self.db.Integer, primary_key=True)
	username = self.db.Column(self.db.String(80), unique=True)