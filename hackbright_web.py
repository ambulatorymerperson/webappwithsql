"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, flash, redirect

import hackbright

app = Flask(__name__)

# secret_key = "SECRETSECRET"

@app.route("/student")
def get_student():
    """Show information about a student."""

    # github = "jhacks" -- this is the hardcoded way
    github = request.args.get('github') 
    # above variable github is using the get method to request a key,value pair from args.

    first, last, github = hackbright.get_student_by_github(github)

    row = hackbright.get_grades_by_github(github)


    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github, 
                           row=row)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html") 

@app.route("/add_student_form")
def take_new_student_info():

    	return render_template("add_student.html")

@app.route("/adding_student", methods=['POST'])
def student_add():


	first_name = request.form.get('first_name')
	last_name = request.form.get('last_name')
	github_username = request.form.get('github_username')


	hackbright.make_new_student(first_name, last_name, github_username)

	# flash("successfully added!")

	# return render_template("add_student.html",
	# 							first_name=first_name,
	# 						last_name=last_name,
	# 						github_username=github_username)

	return redirect("/add_student_form")

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
