from flask import Flask, jsonify, request
import paramiko

app = Flask(__name__)

# Στοιχεία για τον απομακρυσμένο server
REMOTE_SERVER_IP = 'xxxx'
REMOTE_SERVER_USERNAME = 'xxxx'
REMOTE_SERVER_PORT = xxxx
REMOTE_SERVER_PASSWORD = 'xxxx'  # Προσοχή: Χρησιμοποίησε κλειδιά SSH για καλύτερη ασφάλεια

# Οι εντολές που θέλεις να εκτελέσεις
x = "ip a"
y = ""




def execute_remote_command(command):
    """Συνάρτηση για εκτέλεση εντολής σε απομακρυσμένο server μέσω SSH."""
    try:
        # Σύνδεση μέσω SSH στον απομακρυσμένο server
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(REMOTE_SERVER_IP, username=REMOTE_SERVER_USERNAME,port=REMOTE_SERVER_PORT, password=REMOTE_SERVER_PASSWORD)

        # Εκτέλεση εντολής
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Κλείσιμο της σύνδεσης
        ssh_client.close()

        return output, error
    except Exception as e:
        return None, str(e)

@app.route('/kcliinstall', methods=['POST'])
def add_kcli():
    # Εκτέλεση της πρώτης εντολής
    output_x, error_x = execute_remote_command(x)
    # Εκτέλεση της δεύτερης εντολής
    output_y, error_y = execute_remote_command(y)

    # Επιστροφή των αποτελεσμάτων
    return jsonify({
        'x_output': output_x,
        'x_error': error_x,
        'y_output': output_y,
        'y_error': error_y
    })

if __name__ == '__main__':
    app.run(debug=True)