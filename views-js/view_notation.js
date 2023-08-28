function view_notation(doc) {
    if (doc && doc._id && doc.token) {
      emit(doc.product_id, {token: doc.token});
    }
  }