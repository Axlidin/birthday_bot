# import sqlite3
#
# class Database:
#     def __init__(self, path_to_db="main.db"):
#         self.path_to_db = path_to_db
#
#     @property
#     def connection(self):
#         return sqlite3.connect(self.path_to_db)
#
#     def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
#         if not parameters:
#             parameters = ()
#         connection = self.connection
#         connection.set_trace_callback(logger)
#         cursor = connection.cursor()
#         data = None
#         cursor.execute(sql, parameters)
#
#         if commit:
#             connection.commit()
#         if fetchall:
#             data = cursor.fetchall()
#         if fetchone:
#             data = cursor.fetchone()
#         connection.close()
#         return data
#
#     def create_table_birthday(self):
#         sql = """
#         CREATE TABLE birthday (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         full_name VARCHAR(255) NOT NULL,
#         Year INTEGER NOT NULL,
#         Month INTEGER NOT NULL,
#         Day INTEGER NOT NULL,
#         telegram_id BIGINT NOT NULL
#         );
#         """
#         self.execute(sql, commit=True)
#
#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join([
#             f"{item} = ?" for item in parameters
#         ])
#         return sql, tuple(parameters.values())
#
#     def add_birthday(self,
#                      full_name: str,
#                      Year: int,
#                      Month: int,
#                      Day: int,
#                      telegram_id: int,
#                      ):
#
#         sql = """
#         INSERT INTO birthday(full_name,
#                             Year,
#                             Month,
#                             Day,
#                             telegram_id) VALUES(?, ?, ?, ?, ?)
#         """
#         self.execute(sql, parameters=(full_name,
#                                     Year,
#                                     Month,
#                                     Day,
#                                     telegram_id), commit=True)
#
#     def select_all_birthday(self):
#         sql = "SELECT * FROM birthday"
#         return self.execute(sql, fetchall=True)
#
#     def select_birthday(self, **kwargs):
#         sql = "SELECT * FROM birthday WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=(parameters, ), fetchone=True)
#
#     def count_birthday(self):
#         return self.execute("SELECT COUNT(*) FROM birthday;", fetchone=True)
#
#     def update_birthday_Year(self, Year, telegram_id):
#         sql = "UPDATE birthday SET Year=? WHERE telegram_id=?"
#         return self.execute(sql, parameters=(Year, telegram_id, ), commit=True)
#
#     def delete_birthday(self):
#         self.execute("DELETE FROM birthday WHERE TRUE", commit=True)
#
#     def drop_birthday(self):
#         self.execute("DROP TABLE birthday", commit=True)
#
#     def my_birthday(self, tg_id):
#         sql = "SELECT * FROM birthday WHERE telegram_id=? "
#         return self.execute(sql, parameters=(tg_id, ), fetchall=True)
#
#     def happy_Month_Day(self, Month, Day):
#         sql = f"SELECT * FROM birthday WHERE Month = ? AND Day = ?"
#         return self.execute(sql, parameters=(Month, Day, ), fetchall=True)
#
#     def delete_db_name(self, del_name):
#         sql = "DELETE FROM birthday WHERE full_name=?"
#         return self.execute(sql, parameters=(del_name, ), commit=True)
#
#     def happy_day(self, t_month, t_day):
#         sql = "SELECT * FROM birthday WHERE Month = ? AND Day = ?"
#         return self.execute(sql, parameters=(t_month, t_day, ), fetchall=True)
# ##########users
#     def create_table_Users(self):
#         sql = """
#         CREATE TABLE Users (
#             id int NOT NULL,
#             fullname varchar(255) NOT NULL,
#             PRIMARY KEY (id)
#             );
#             """
#         self.execute(sql, commit=True)
#
#     def add_Users(self, id: int, fullname: str):
#         sql = """
#         INSERT INTO Users(id, fullname) VALUES(?, ?)
#         """
#         self.execute(sql, parameters=(id, fullname), commit=True)
#
#     def select_all_Users(self):
#         sql = """
#         SELECT * FROM Users
#         """
#         return self.execute(sql, fetchall=True)
#
#     def select_Users(self, **kwargs):
#         # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
#         sql = "SELECT * FROM Users WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#
#         return self.execute(sql, parameters=parameters, fetchone=True)
#
#     def count_Users(self):
#         return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
#
#     def update_user_Users_username(self, fullname, id):
#         # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
#
#         sql = f"""
#         UPDATE Users SET fullname=? WHERE id=?
#         """
#         return self.execute(sql, parameters=(fullname, id, ), commit=True)
#
#     def delete_Users(self):
#         self.execute(f"""DELETE FROM Users WHERE TRUE""", commit=True)
#
#     def drop_Users(self):
#         self.execute(f"""DROP TABLE Users""", commit=True)
#
#     def my_user_see(self, tg_id):
#         sql = f"""SELECT * FROM Users WHERE id=?"""
#         return self.execute(sql, parameters=(tg_id, ), fetchall=True)
#
#     def is_registered(self, user_id):
#         sql = (f"""SELECT * FROM Users WHERE id = ? """)
#         rows = self.execute(sql, parameters=(user_id,), fetchall=True)
#         return rows
#
#         ##########gr birhday
#     def create_table_Gr_birthyday(self):
#         sql = """
#                     CREATE TABLE Gr_birthyday (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     full_name VARCHAR(255) NOT NULL,
#                     Year INTEGER NOT NULL,
#                     Month INTEGER NOT NULL,
#                     Day INTEGER NOT NULL,
#                     guruh_name VARCHAR(255) NOT NULL,
#                     guruh_id INTEGER
#                     );
#                     """
#         self.execute(sql, commit=True)
#
#     def add_Gr_birthyday(self,
#                          full_name: str,
#                          Year: int,
#                          Month: int,
#                          Day: int,
#                          guruh_id: int,
#                          guruh_name: str):
#         sql = """
#            INSERT INTO Gr_birthyday (guruh_name,
#                             full_name,
#                             Year,
#                             Month,
#                             Day,
#                              guruh_id) VALUES (?, ?, ?, ?, ?, ?)
#            """
#         self.execute(sql, parameters=(guruh_name,
#                                       full_name,
#                                       Year,
#                                       Month,
#                                       Day,
#                                       guruh_id), commit=True)
#
#     def select_all_Gr_birthyday(self):
#         sql = """
#            SELECT * FROM Gr_birthyday
#            """
#         return self.execute(sql, fetchall=True)
#
#     def select_Gr_birthyday(self, **kwargs):
#         sql = "SELECT * FROM Gr_birthyday WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#
#         return self.execute(sql, parameters=parameters, fetchone=True)
#
#     def count_Gr_birthyday(self):
#         return self.execute("SELECT COUNT(*) FROM Gr_birthyday;", fetchone=True)
#
#     def update_user_Gr_birthyday_username(self, Gr_birthydayName, id):
#         sql = f"""
#            UPDATE Gr_birthyday SET Gr_birthydayName=? WHERE id=?
#            """
#         return self.execute(sql, parameters=(Gr_birthydayName, id,), commit=True)
#
#     def delete_Gr_birthyday(self):
#         self.execute(f"""DELETE FROM Gr_birthyday WHERE TRUE""", commit=True)
#
#     def drop_Gr_birthyday(self):
#         self.execute(f"""DROP TABLE Gr_birthyday""", commit=True)
#
#     def my_user_seeGR_user(self, tg_id):
#         sql = f"""SELECT * FROM Gr_birthyday WHERE user_id=?"""
#         return self.execute(sql, parameters=(tg_id,), fetchall=True)
#
#     def my_user_seeGR_gr(self, guruh_id):
#         sql = f"""SELECT * FROM Gr_birthyday WHERE guruh_id=?"""
#         return self.execute(sql, parameters=(guruh_id,), fetchall=True)
#
#     def see_mont_day(self, month, day):
#         sql = f"""SELECT * FROM Gr_birthyday WHERE Month=? AND Day=?"""
#         return self.execute(sql, parameters=(month, day,), fetchall=True)
#
#     def delete_birhdaygr(self, del_name):
#         sql = "DELETE FROM Gr_birthyday WHERE full_name=?"
#         return self.execute(sql, parameters=(del_name, ), commit=True)
#
#     ##########Guruhlar
#     def create_table_Guruhlar(self):
#         sql = """
#               CREATE TABLE Guruhlar  (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     chat_id INTEGER,
#                     GroupName varchar(255) NOT NULL);
#                                       """
#         self.execute(sql, commit=True)
#
#     def add_Guruhlar(self, chat_id: int, GroupName: str):
#         sql = """
#               INSERT INTO Guruhlar  (chat_id, GroupName) VALUES (?, ?)
#               """
#         self.execute(sql, parameters=(chat_id, GroupName), commit=True)
#
#     def select_all_Guruhlar(self):
#         sql = """
#               SELECT * FROM Guruhlar
#               """
#         return self.execute(sql, fetchall=True)
#
#     def select_Guruhlar(self, **kwargs):
#         sql = "SELECT * FROM Guruhlar  WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#
#         return self.execute(sql, parameters=parameters, fetchone=True)
#
#     def count_Guruhlar(self):
#         return self.execute("SELECT COUNT(*) FROM Guruhlar ;", fetchone=True)
#
#     def update_user_Guruhlar_username(self, GroupName, id):
#         sql = f"""
#               UPDATE Guruhlar  SET Guruhlar GroupName=? WHERE id=?
#               """
#         return self.execute(sql, parameters=(GroupName, id,), commit=True)
#
#
#     def delete_Guruhlar(self):
#         self.execute(f"""DELETE FROM Guruhlar  WHERE TRUE""", commit=True)
#
#
#     def drop_Guruhlar(self):
#         self.execute(f"""DROP TABLE Guruhlar """, commit=True)
#
#
#     def my_user_seeGuruhlar_user(self, chat_id):
#         sql = f"""SELECT * FROM Guruhlar  WHERE chat_id=?"""
#         return self.execute(sql, parameters=(chat_id,), fetchall=True)
#
# ###################auotinfo########
#     def auto_info_user(self, month, day):
#         sql = """SELECT * FROM birthday WHERE Month = ? AND Day = ?"""
#         return self.execute(sql, parameters=(month, day, ), fetchall=True)
#
#     def auto_info_gr(self, month, day):
#         sql = """SELECT * FROM Gr_birthyday WHERE Month = ? AND Day = ?"""
#         return self.execute(sql, parameters=(month, day, ), fetchall=True)
#
# def logger(statement):
#     print(f"""
# _____________________________________________________
# Executing:
# {statement}
# _____________________________________________________
# """)