import docker
from flask import Flask, request, jsonify


app = Flask('score')


docker_client = docker.from_env()


def validate_attendee_code(task_id, code):
    container = docker_client.containers.run(
        'cpp-builder:latest',
        detach=True,
        environment={'TASK_ID': task_id, 'CODE': code}
    )
    result = container.wait(timeout=5)
    assert result['StatusCode'] == 0
    outcome = container.logs()
    result = []
    for line in outcome.splitlines():
        compilation_code, diff_code = line.split(b' ')
        result.append({
            'exit_code': int(compilation_code),
            'result': int(diff_code)
        })
    return result


@app.route('/tasks/<string:task_id>/score', methods=['POST'])
def run_attendee_program(task_id: str):
    assert request.content_type == 'text/plain'
    code = request.data
    return jsonify(validate_attendee_code(task_id, code))


@app.route('/healthcheck')
def healthcheck():
    return {'status': 'ok'}


if __name__ == '__main__':
    app.run(debug=False)
