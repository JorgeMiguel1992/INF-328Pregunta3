import psycopg2 as pc

a = input("Ingrese C.I. ")
conexion = pc.connect(user="postgres", password="123456",
                      host="127.0.0.1", port="5432", database="Academico")
cursor = conexion.cursor()
sql = "SELECT m.siglaM Sigla,m.nombreM Materia FROM Estudiante e,Materia m, Matricula ma where e.ci=" + \
    a+" AND e.id_estudiante=ma.id_estudiante AND m.id_materia=ma.id_materia"

cursor.execute(sql)
print("Materias Inscritas")
print("Sigla", "     Nombre")
registros = cursor.fetchall()
for registro in registros:
    print(registro[0], "  ", registro[1])
cursor.close()
conexion.close()
