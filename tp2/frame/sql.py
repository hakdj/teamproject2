class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE id= '%s' ";
    userinsert = "INSERT INTO users VALUES ('%s','%s','%s','%s','%s',CURRENT_DATE())";
    userdelete = "DELETE FROM users WHERE user_id= '%s' ";
    userupdate = "UPDATE users SET pwd='%s',name='%s' WHERE user_id= '%s' ";

    udatalist = """ SELECT a.* FROM udata a INNER JOIN users u ON a.id=u.user_id
                    WHERE u.id='%s'
                """;
    udatalistone = "SELECT * FROM udata WHERE data_id= %d ";
    udatainsert = """INSERT INTO udata VALUES
                    (NULL,'%s','%d','%s',%d,%d,%d,%d,%d,%d,%d,%d)""";
    udatadelete = "DELETE FROM udata WHERE data_id= %d ";
    udataupdate = """UPDATE udata SET schooltype='%s',major='%s', graduy='%d',
                      age='%d', intern='%d',toeic='%d',tosp='%d', train='%d',
                      jobseek='%d',cert='%d'
                      WHERE data_id= %d
                  """;

    resultlist = """ 
         SELECT a.result, a.resdate FROM res a INNER JOIN users u ON a.id=u.user_id
            WHERE u.user_id = '%s'
         """;
    resultinsert = "INSERT INTO result VALUES (NULL, '%s', '%s', CURRENT_DATE())";
