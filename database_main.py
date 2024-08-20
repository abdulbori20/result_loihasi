import mysql.connector

DATABASE_NAME = 'result_loihasi1'


##Shularni o'ziznikiga o'zgartiring
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Abdulboriy'
def init_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        create_database_script = f"""
            create database IF NOT EXISTS {DATABASE_NAME};
        """

        use_database_script = f"""
            use {DATABASE_NAME};
        """

        create_student_table_script = """
        create table IF NOT EXISTS student(
                id bigint AUTO_INCREMENT PRIMARY KEY,
                username varchar(250) not null UNIQUE,
                password varchar(250) not null,
                created_date timestamp default CURRENT_TIMESTAMP
            );
        """

        create_courses_table_script = """
        create table IF NOT EXISTS courses(
                id bigint AUTO_INCREMENT PRIMARY KEY,
                nomi varchar(250) not null,
                narxi decimal(10, 2) not null,
                davomiyligi varchar(250),
                created_date timestamp default CURRENT_TIMESTAMP
            );
        """

        create_student_cources_table_script = """
        create table IF NOT EXISTS students_cources(
                id bigint AUTO_INCREMENT PRIMARY KEY,
                student_id bigint,
                course_id bigint,
                foreign key(student_id) REFERENCES student(id),
                foreign key(course_id) REFERENCES courses(id)
            );
        """

        insert_student_script = """
            insert ignore into student(username, password) values("admin", "admin");
        """

        cursor = connection.cursor()

        cursor.execute(create_database_script)
        connection.commit()

        cursor.execute(use_database_script)
        connection.commit()

        cursor.execute(create_student_table_script)
        connection.commit()

        cursor.execute(create_courses_table_script)
        connection.commit()

        cursor.execute(create_student_cources_table_script)
        connection.commit()

        cursor.execute(insert_student_script)
        connection.commit()

        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print("Xatolik sodir boldi", e)
