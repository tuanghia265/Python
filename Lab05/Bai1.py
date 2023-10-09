import pyodbc

connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=QLSinhVien; UID=sa;PWD=123;Encrypt=no'

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        
def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"Danh sách các lớp là: ")
        for row in records:
            print("*"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
            
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)


def insert_class(id,class_name):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        select_querry=f"insert Lop (ID, TenLop) values ('{id}','{class_name}')"
        cursor.execute(select_querry)
        connection.commit()

        print("Đã thêm thành công!!!")
        close_connection(connection)
    except(Exception,pyodbc.Error) as error:
        print("Đã có lỗi xảy ra vui lòng thử lại.Thông tin lỗi:",error)


def insert_student(id,stu_name,stu_class):
    try:
        conect=get_connection()
        cursor=conect.cursor()
        select_querry=f"insert SinhVien (ID,HoTen,Lop) values ('{id}','{stu_name}','{stu_class}')"
        cursor.execute(select_querry)
        conect.commit()

        print("Đã thêm thành công")
    except(Exception,pyodbc.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
def del_student(id):
    try:
        conect=get_connection()
        cursor=conect.cursor()
        select_querry=f"delete SinhVien where ID = ('{id}')"
        cursor.execute(select_querry)
        conect.commit()
        print(f"Đã xóa sinh viên có mã {id} thành công")
    except (Exception,pyodbc.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)

def upd_student(id,name,id_class):
    try:
        conect=get_connection()
        cursor=conect.cursor()
        select_querry=f"update SinhVien set HoTen=N'{name}', MaLop='{id_class}' where ID='{id}'"
        cursor.execute(select_querry)
        conect.commit()
        print("Đã cập nhật thành công")
    except (Exception,pyodbc.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ",error)
    
        
def get_all_student():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select SinhVien.ID, HoTen, SinhVien.MaLop, Lop.TenLop
                        from SinhVien, Lop
                        where SinhVien.MaLop = Lop.ID"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Mã số".ljust(6) + "Họ và tên sinh viên".center(30) + "Mã lớp".center(8) + "Tên lớp".rjust(8))
        for row in records:
            print(str(row[0]).ljust(6) + str(row[1]).center(30) + str(row[2]).center(8) + row[3].rjust(8))
                        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
        
    
def get_all_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from Lop where id = ?"
        params = (class_id)
        cursor.execute(select_query, params)
        
        records = cursor.fetchone()
        
        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp".ljust(6)+"Tên lớp".rjust(8))
        print("Mã lớp: ", records[0])
        print("Tên lớp: ", records[1])
        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
        
def get_all_student_by_id(stu_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from SinhVien where id = ?"
        params = (stu_id)
        cursor.execute(select_query, params)
        
        records = cursor.fetchone()
        
        print(f"Thông tin sinh viên có mã số {stu_id} là: ")
        print("Mã số: ", records[0])
        print("Họ và tên: ", records[1])
        print("Mã lớp: ", records[2])
        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
    
        
def get_all_student_by_class_id(stucl_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = "select * from SinhVien where MaLop = ?"
        params = (stucl_id)
        cursor.execute(select_query, params)
        records = cursor.fetchall()
        print(f"Danh sách sinh viên thuộc mã lớp {stucl_id}")
        print("Mã số".center(6) + "Họ và tên sinh viên".center(30) + "Mã lớp".center(8))
        for row in records:
            print(str(row[0]).center(6) + str(row[1]).center(30) + str(row[2]).center(8))
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
        
def get_all_student_by_name_class_id(name, class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = f"select * from SinhVien where SinhVien.HoTen like '%{name}%' and MaLop = {class_id}"   
        cursor.execute(select_query)
        records = cursor.fetchall() 
        print("Mã số".center(6) + "Họ và tên sinh viên".center(30) + "Mã lớp".center(8))
        for row in records:
            print(str(row[0]).center(6) + str(row[1]).center(30) + str(row[2]).center(8))
        close_connection(connection)
        
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
        



# get_all_student()
# get_all_class_by_id("1")
# get_all_student_by_class_id("2")
# get_all_student_by_id()
# get_all_student_by_name_class_id("Tòng",2)
# insert_class('5',"CTK44AB")
# del_student("12")
upd_student('11',"Lê Tuấn Nghĩa",'2')
get_all_student()