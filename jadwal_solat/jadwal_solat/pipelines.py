# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from jadwal_solat.models import db_connect, create_jadwal_solat_table, JadwalSolat

class JadwalSolatPipeline(object):
	def __init__(self):
		engine = db_connect()
		create_jadwal_solat_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		session = self.Session()
		jadwalSolat = JadwalSolat(**item)

		try:
			session.add(jadwalSolat)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item
