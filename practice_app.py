from flask import render_template, request, redirect
from db_models import create_app, db, UserInfo

app = create_app()

@app.route('/')
def home():
    return render_template('my.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = UserInfo(
            user_name=request.form['user_name'],
            user_mail=request.form['user_mail'],
            password=request.form['password'],
            location=request.form.get('location', ''),
            availability=request.form.get('availability', ''),
            skills_have=request.form.get('skills_have', ''),
            skills_want=request.form.get('skills_want', '')
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
