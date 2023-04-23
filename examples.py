# from db import session

# import tables

# from sqlalchemy.sql.expression import desc

# # result = session.query(
# #     tables.Films.id, tables.Films.name_film
# # ).filter(
# #     tables.Films.id > 1,
# #     tables.Films.id < 3,
# # ).all()

# # film_ids = session.query(tables.Films.id).filter(tables.Films.id > 1).subquery()

# # if result:
# #     print("All is good")
# # else:
# #     print("Not good")

# # print(result)
# # print(film_ids)

# # result = session.query(tables.Films.name_film).filter(tables.Films.id.in_(film_ids)).all()
# # print(result)

# film_ids = session.query(tables.Films.id, tables.Films.name_film).order_by(desc(tables.Films.id)).limit(1).offset(1).all()
# print(film_ids)


computer = {
    "id": 21,
    "status": "ACTIVE",
    "activated_at": "2013-06-01",
    "expiration_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": 'green',
            "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
        },
        "owners": [{
            "name": "Stephan Nollan",
            "card_number": "4000000000000002",
            "email": "shtephan.nollan@gmail.com",
        }]
    }
}