function load(doc) {
    if (doc && doc.token && doc.country && doc.age && doc.e_mail && doc.password && doc.gender && doc._rev ){
      emit(doc.token, {e_mail: doc.e_mail, age: doc.age, country: doc.country, password: doc.password,gender: doc.gender, rev: doc._rev});
    }
  }