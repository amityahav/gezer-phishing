from flask import Blueprint, render_template, request, redirect, url_for
from libs.logic import Logic


login = Blueprint('login', __name__)
logic = Logic()


@login.route('/login.php', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('./login.html')

    if request.method == 'POST':
        username, password, identity = request.form.get('username'), request.form.get('pass'), request.form.get('id')

        html_file_name = logic.render_courses(username, password, identity)
        if html_file_name == "login_fail.html":
            return render_template(f"./{html_file_name}")

        return redirect(url_for('courses_list.crs_list', username=html_file_name))
