from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    @classmethod
    def create_table(cls):
        """Create a new table to pesrist the attibutes of the department instance"""
        sql = """CREATE TABLE IF NOT EXISTS Ddepartments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        ) """
        CURSOR.execute(sql)
        CONN.commit()
        print("Department table created successfully.")
    @classmethod
    def drop_table(cls):
        """Drop the table that persists Department instances"""
        sql = """DROP TABLE IF EXISTS departments"""
        CURSOR.execute(sql)
        CONN.commit()
        print("Department table dropped successfully.")
    
    def save(self):
        """"Insert a new row with the name and location values of the current Department.
        Update object id attributes using the primary key of the new row"""
        sql = """INSERT INTO departments (name, location) VALUES (?, ?)"""
        CURSOR.execute(sql, (self.name, self.location))
        self.id = CURSOR.lastrowid
        CONN.commit()
        print(f"Department {self.id} saved successfully.")
       