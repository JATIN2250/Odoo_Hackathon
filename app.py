from flask import Flask, render_template, request, redirect, url_for
from db_models import create_app, db, UserInfo

app = create_app()

# Dummy data for demonstration. In a real app, you'd query a database.
# I've created 17 sample users to demonstrate pagination.
all_users = [
    {"initials": "JD", "name": "John Doe", "skill": "Machine Learning", "offering": "Python, ML", "wants": "Excel", "availability": "Evenings", "location": "Jaipur, India", "color": "purple"},
    {"initials": "AB", "name": "Alice Brown", "skill": "UI Design", "offering": "Figma", "wants": "Python", "availability": "Mornings", "location": "Mumbai, India", "color": "red"},
    {"initials": "SP", "name": "Sam Patel", "skill": "Data Science", "offering": "Python, SQL", "wants": "React", "availability": "Weekends", "location": "Delhi, India", "color": "green"},
    {"initials": "MJ", "name": "Mary Jane", "skill": "Excel", "offering": "Excel, Word", "wants": "ML", "availability": "Weekends", "location": "Bangalore, India", "color": "blue"},
    {"initials": "KT", "name": "Kevin Tran", "skill": "Web Dev", "offering": "HTML/CSS", "wants": "React", "availability": "Evenings", "location": "Pune, India", "color": "green"},
    {"initials": "RS", "name": "Ravi Singh", "skill": "Guitar", "offering": "Acoustic", "wants": "Video Editing", "availability": "Anytime", "location": "Jaipur, India", "color": "yellow"},
    {"initials": "AD", "name": "Anjali Das", "skill": "Video Editing", "offering": "Premiere Pro", "wants": "Music Theory", "availability": "Afternoons", "location": "Kolkata, India", "color": "indigo"},
    {"initials": "BV", "name": "Ben Verma", "skill": "React", "offering": "React, JS", "wants": "Python", "availability": "Weekends", "location": "Hyderabad, India", "color": "pink"},
    {"initials": "CK", "name": "Chloe Kim", "skill": "Photography", "offering": "Lightroom", "wants": "Web Dev", "availability": "Mornings", "location": "Chennai, India", "color": "teal"},
    {"initials": "DL", "name": "David Lee", "skill": "Python", "offering": "Flask, Django", "wants": "UI Design", "availability": "Evenings", "location": "Jaipur, India", "color": "gray"},
    {"initials": "EM", "name": "Emily Mae", "skill": "Content Writing", "offering": "SEO, Blogs", "wants": "Graphic Design", "availability": "Anytime", "location": "Mumbai, India", "color": "red"},
    {"initials": "FG", "name": "Frank Green", "skill": "Graphic Design", "offering": "Illustrator", "wants": "Photography", "availability": "Afternoons", "location": "Bangalore, India", "color": "blue"},
    {"initials": "GH", "name": "Grace Hall", "skill": "Music Theory", "offering": "Piano, Theory", "wants": "Guitar", "availability": "Weekends", "location": "Delhi, India", "color": "purple"},
    {"initials": "IJ", "name": "Ian Johnson", "skill": "SQL", "offering": "Database Mgmt", "wants": "Data Science", "availability": "Mornings", "location": "Pune, India", "color": "green"},
    {"initials": "JK", "name": "Jake Kumar", "skill": "Java", "offering": "Spring Boot", "wants": "ML", "availability": "Evenings", "location": "Hyderabad, India", "color": "yellow"},
    {"initials": "LM", "name": "Lily Moon", "skill": "Digital Art", "offering": "Procreate", "wants": "Python", "availability": "Anytime", "location": "Jaipur, India", "color": "indigo"},
    {"initials": "NO", "name": "Nate Olsen", "skill": "Project Mgmt", "offering": "Agile, Scrum", "wants": "SQL", "availability": "Weekends", "location": "Mumbai, India", "color": "pink"},
]

@app.route('/')
def home():
    # Pass the first 6 users as "recommendations" to the home page
    recommended_users = all_users[:6]
    return render_template('my.html', users=recommended_users)
'''
@app.route('/search', methods=['GET', 'POST'])
def search():
    # Get the search query from URL parameters for GET requests
    query = request.args.get('q', '').strip() # Default to empty string, remove leading/trailing whitespace
    page = request.args.get('page', 1, type=int)

    if request.method == 'POST':
        # Get the search query from the form data (from the input with name="search_skill")
        post_query = request.form.get('search_skill', '').strip()
        # Redirect to the GET version of the search route with the query
        # This is the "Post/Redirect/Get" pattern, good for search forms
        return redirect(url_for('search', q=post_query))

    # Perform the search filtering based on the 'query' variable
    # This 'query' comes from either the GET parameter or the redirect after a POST
    if query:
        # Filter logic: case-insensitive search across skill, offering, and wants
        # A user matches if the query is found in their skill, offering, or wants
        results = [
            user for user in all_users
            if query.lower() in user['skill'].lower() or
               query.lower() in user['offering'].lower() or
               query.lower() in user['wants'].lower()
        ]
    else:
        # If no query is provided (e.g., initial visit to /search without a 'q' parameter),
        # display all users. You could also choose to display an empty set or a default.
        results = all_users

    return render_template('search-results.html', query=query, users=results)
'''
@app.route('/profile')
def profile():
    # In a real app, you'd fetch a specific user by their ID
    # e.g. @app.route('/profile/<int:user_id>')
    # For this demo, we'll just show the profile of the first user.
    user_data = all_users[0]
    return render_template('user-profile.html', user=user_data)

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Get all selected checkboxes and join into comma-separated strings
        skills_have = ", ".join(request.form.getlist('your_skills'))
        skills_want = ", ".join(request.form.getlist('want_skills'))
        availability = ", ".join(request.form.getlist('availability'))

        new_user = UserInfo(
            user_name=request.form['username'],
            user_mail=request.form['email'],
            password=request.form['pass'],
            location=request.form.get('location'),
            skills_have=skills_have,
            skills_want=skills_want,
            availability=availability
        )

        db.session.add(new_user)
        db.session.commit()

        # Redirect back to login box or homepage
        return redirect('/')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('search_skill', '').strip().lower()

    if not query:
        return render_template('search-results.html', users=[], query="")

    # Search in skills_have field (case-insensitive, partial match)
    results = UserInfo.query.filter(UserInfo.skills_have.ilike(f"%{query}%")).all()

    # Format results to fit your HTML template
    users = []
    colors = ['red', 'blue', 'green', 'purple', 'pink', 'orange']
    for i, user in enumerate(results):
        color = colors[i % len(colors)]
        initials = user.user_name[0].upper()
        users.append({
            'name': user.user_name,
            'email': user.user_mail,
            'skill': query.capitalize(),
            'offering': user.skills_have,
            'wants': user.skills_want,
            'availability': user.availability,
            'location': user.location,
            'initials': initials,
            'color': color
        })

    return render_template('search-results.html', users=users, query=query)
if __name__ == '__main__':
    app.run(debug=True)