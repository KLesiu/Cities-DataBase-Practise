import csv
import mysql.connector

def get_pass():
    with open("pass.csv") as passw:
        read = csv.reader(passw)
        for ele in read:
            return ele[0]

with mysql.connector.connect(user='sql7618788',password=get_pass(),host='sql7.freemysqlhosting.net',database='sql7618788') as connection:
    cursor = connection.cursor()

    with open("cities.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                prev_position = int(row['2021'])
            except:
                prev_position = 0


            sql = f"""INSERT INTO
            city(name, country, position, prev_position)
            VALUES('{row['City']}', '{row['Country']}', {int(row['2022'])}, {prev_position})
            """
            cursor.execute(sql)
        connection.commit()





