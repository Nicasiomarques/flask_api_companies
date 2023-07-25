from ...infra.db.sqlalchemy import db

class Company(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cnpj = db.Column(db.String(25))
  reasonName = db.Column(db.String(100))
  fantasyName = db.Column(db.String(100))
  cnae = db.Column(db.String(150))
