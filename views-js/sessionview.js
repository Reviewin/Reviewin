function sessionview (doc) {
    if (doc && doc.token && doc.age && doc.e_mail && doc._id ){
      emit(doc.e_mail, doc._id)
    }
  }