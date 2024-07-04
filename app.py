from flask import Flask, render_template, jsonify

app = Flask(__name__)

COURSE = [{
    'id': 1,
    'title': 'Python',
}, {
    'id': 2,
    'title': 'Flask',
}, {
    'id': 3,
    'title': 'FastAPi',
}]


@app.route("/")
def home_api():
  return render_template('home.html',
                         course=COURSE,
                         company_name='InfinityCode')


@app.route("/api/jobs")
def list_course():
  return jsonify(COURSE)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
