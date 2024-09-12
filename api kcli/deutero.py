import requests

# Ορίστε το URL του API
url = 'http://127.0.0.1:5000/kcliinstall'

# Εάν χρειάζεται να στείλεις δεδομένα με το POST αίτημα, χρησιμοποίησε το 'data' ή 'json'
# Σε αυτό το παράδειγμα δεν στέλνουμε δεδομένα, απλά στέλνουμε το αίτημα
response = requests.post(url)
print (response)
# Έλεγχος της απάντησης
if response.status_code == 200:
    print('Απάντηση από το API:', response.text)
else:
    print('Σφάλμα:', response.status_code)
