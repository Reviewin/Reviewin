function login(doc) {
    emit(doc.email,{"age": doc.age,"country":doc.country, "points":doc.points, "gender":doc.gender});
  }