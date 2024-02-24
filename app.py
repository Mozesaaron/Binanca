from flask import Flask , request , render_template , jsonify
import socket

app = Flask(__name__)

@app.route('/')
def displaydashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)        

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)


























