# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields

class manager(osv.Model):
	_name = 'manager_601.manager'
	_columns = {
		'date': fields.datetime(string=u'消费时间', required=True),
		'amount': fields.float(string=u'消费额', required=True),
		'description': fields.text(string=u'描述'),
		'project': fields.many2one('manager_601.project', string=u'项目', required=True),
		'user_ids': fields.one2many('manager_601.user', 'manager_id', string=u'参与者',
				 required=True),
	}

	_defaults = {
		'date': fields.datetime.now(),
	}

class project(osv.Model):
	"""docstring for project"""
	_name = 'manager_601.project'
	_columns = {
		'name': fields.char(string=u'名称', required=True),
		'description': fields.text(string=u'描述'),
	}

class user(osv.Model):
	_name = 'manager_601.user'
	_columns = {
		'manager_id': fields.many2one('manager_601.manager', string=u'管理'),
		'name': fields.char(string=u'姓名'),
		'is_boss': fields.boolean(string=u'是老大'),
		'cost': fields.float(string=u'月花费'),
	}

	_defaults = {
        'is_boss' : False,
    }