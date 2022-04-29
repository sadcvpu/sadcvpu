import joblib

tr = joblib.load('text_classif/tfidf.pkl')
clf = joblib.load('text_classif/SVM.pkl')

def predict_activity(activity_text):
  return clf.predict(tr.transform([activity_text]))[0]