from firebase import firebase
N = str(input("Name\n"))
E = str(input("EMail\n"))
P = str(input("Pokemon\n"))
firebase = firebase.FirebaseApplication("https://dcmondb-default-rtdb.firebaseio.com/", None)
data = {'Name':N,'Email':E,'Pokemon':P}

result = firebase.post(f'https://dcmondb-default-rtdb.firebaseio.com/Profiles/{N}',data)
print(result)
try:
    result1 = firebase.get(f'https://dcmondb-default-rtdb.firebaseio.com/Profiles/{N}',data)
    print(result1)

Exception:
    except Exception as e:
    print(e)
