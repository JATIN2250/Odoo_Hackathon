from db_models import create_app, db, UserInfo

app = create_app()

with app.app_context():
    users = [
        UserInfo(user_name="Troy", user_mail="amandacalhoun@yahoo.com", password="pass123",
                 location="Port Christopher", availability="Wednesday", skills_have="ML, C++", skills_want="C++"),
        UserInfo(user_name="Veronica", user_mail="jenniferbrown@hotmail.com", password="pass123",
                 location="West Olivia", availability="Monday", skills_have="Guitar, Excel, C++,", skills_want="UI Design"),
        UserInfo(user_name="Danielle", user_mail="kimerin@warren.com", password="pass123",
                 location="Justinton", availability="Sunday, Wednesday", skills_have="Figma, ML, Node.js", skills_want="Excel, React"),
        UserInfo(user_name="William", user_mail="kevin39@holt-harmon.net", password="pass123",
                 location="Lake Kathyshire", availability="Monday, Tuesday, Friday", skills_have="ML", skills_want="Figma, Excel"),
        UserInfo(user_name="Heather", user_mail="juliefields@baldwin.com", password="pass123",
                 location="Williamsfurt", availability="Monday, Sunday, Tuesday", skills_have="React, C++", skills_want="React, UI Design"),
        UserInfo(user_name="Christopher", user_mail="anthonyshannon@gmail.com", password="pass123",
                 location="Shirleyville", availability="Saturday", skills_have="Node.js, Python, C++", skills_want="Python"),
        UserInfo(user_name="Benjamin", user_mail="rlove@gmail.com", password="pass123",
                 location="Cynthiaburgh", availability="Thursday, Friday", skills_have="C++, Java, Node.js", skills_want="C++"),
        UserInfo(user_name="John", user_mail="david16@smith.com", password="pass123",
                 location="Rodgersmouth", availability="Thursday, Saturday, Monday", skills_have="Guitar, React, Excel", skills_want="Excel"),
        UserInfo(user_name="Marc", user_mail="laurenquinn@hotmail.com", password="pass123",
                 location="North Shannon", availability="Tuesday", skills_have="Java, C++", skills_want="Python"),
        UserInfo(user_name="Heather", user_mail="andrea41@gmail.com", password="pass123",
                 location="North Juliemouth", availability="Monday, Friday", skills_have="Excel, Guitar, Figma", skills_want="React, Node.js")
        ]

    db.session.bulk_save_objects(users)
    db.session.commit()
    print("✅ Dummy users added.")
