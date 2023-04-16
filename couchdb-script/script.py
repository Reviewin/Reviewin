from couchdb import Server, design

# Connect to CouchDB server
couch = Server('http://admin:kolea21342@127.0.0.1:5984/')

# Create databases
if 'reviewinn_users' not in couch:
    reviewinn_users_db = couch.create('reviewinn_users')
else:
    reviewinn_users_db = couch['reviewinn_users']

if 'captchaa' not in couch:
    captchaa_db = couch.create('captchaa')
else:
    captchaa_db = couch['captchaa']

if 'productss' not in couch:
    productss_db = couch.create('productss')
else:
    productss_db = couch['productss']

# Create views

# View for "reviewinn_users" with email filter
loginn_map_func = '''function (doc) {
  if (doc && doc.email && doc.password && doc.age && doc.country && doc.gender){
    emit(doc.email, {password: doc.password, age: doc.age, country: doc.country, gender: doc.gender});
  }
}'''

loginn_view = design.ViewDefinition('users', 'loginn', loginn_map_func)
loginn_view.sync(reviewinn_users_db)

# View for "captchaa" with captcha filter
recaptchaa_map_func = '''function (doc) {
  if (doc && doc.captcha_value){
    emit(doc.captcha_value, doc.captcha_value)
  }
}'''

recaptchaa_view = design.ViewDefinition('captcha_design', 'recaptchaa', recaptchaa_map_func)
recaptchaa_view.sync(captchaa_db)

# View for "productss" with product_id filter
productt_view_map_func = '''function (doc) {
  if (doc && doc._id && doc.product_id && doc.type_of_products){
    emit(doc.product_id, doc.type_of_products)
  }
}'''

productt_view = design.ViewDefinition('products_design', 'productt_view', productt_view_map_func)
productt_view.sync(productss_db)
