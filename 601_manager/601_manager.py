# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
from unidecode import unidecode

class manager(osv.Model):
	_name = '601_manager.manager'
	_columns = {
		'date': fields.datetime(u'消费时间', required=True),
		'amount': fields.float(u'消费额', required=True),
		'description': fields.text(u'描述'),
		'project': fields.many2one('601_manager.project', u'项目', required=True),
		'user_ids': fields.one2many('601_manager.user', 'manager_id', u'参与者',
				 required=True),
		''
	}

class project(osv.Model):
	"""docstring for project"""
	_name = '601_manager.project'
	_columns = {
		'name': fields.char(u'名称', required=True),
		'description': fields.text(u'描述'),
	}

class user(osv.Model):
	_name = '601_manager.user'
	_columns = {
		'name': fields.char(u'姓名'),
		'is_boss': fields.boolean(u'是老板'),
	}

	_defaults = {
        'is_boss' : False;
    }