from firebase import firebase
firebase = firebase.FirebaseApplication("https://digital-equator-258017.firebaseio.com/", None)
data =  { 'Name': 'John Doe',
          'RollNo': 3,
          'Percentage': 70.02
          }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
result = firebase.post('/digital-equator-258017/Costumer',data)
print(result)

