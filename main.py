from flask import Flask, render_template
import json

app = Flask(__name__)

status_to_color = {
    "online": "is-success",
    "offline": "is-danger",
    "error": "is-danger",
    "limited": "is-warning",
    "overloaded": "is-warning",
    "unknown": "is-warning",
    "maintenance": "is-warning",
    "degraded": "is-warning",
    "updating": "is-warning",
    "testing": "is-warning",
}

@app.route('/')
def dashboard():
    with open('data.json') as json_file:
        services = json.load(json_file)
    
    updated_services = []
    for service in services:
        new_service = service.copy()  # Create a copy of the service
        new_service['status'] = status_to_color.get(service['status'].lower(), "is-warning")
        updated_services.append(new_service)
    
    return render_template('index.html', services=services, updated_services=updated_services)

if __name__ == '__main__':
    app.run(debug=True)