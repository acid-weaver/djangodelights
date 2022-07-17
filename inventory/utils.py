navigation = [
				{'title':'Menu', 'url_name':'menu'},
				{'title':'Inventory', 'url_name':'inventory'},
				{'title':'Purchases', 'url_name':'purchase'},
				{'title':'Bookkeeping', 'url_name':'bookkeeping'},
				# {'title':'Registration', 'url_name':'registration'}
			]

class DataMixin:
	def get_user_context(self, **kwargs):
		context = kwargs
		if 'select' in context:
			context['select'] = navigation[context['select']]
		context['nav_menu'] = navigation
		return context