function comments(doc) {
    if (doc && doc.age && doc._id && doc.comments && doc.product_id){
      emit(doc.product_id,doc.comments);
    }
  }