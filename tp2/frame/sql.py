class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE user_id= '%s' ";
    userinsert = "INSERT INTO users VALUES ('%s','%s','%s','%s','%s',CURRENT_DATE())";
    userdelete = "DELETE FROM users WHERE user_id= '%s' ";
    userupdate = "UPDATE users SET pwd='%s',name='%s' WHERE user_id= '%s' ";

    udatalist = """ SELECT * FROM udata
                """;
    udatalistone = "SELECT * FROM udata WHERE id= '%s' ";
    udatainsert = """INSERT INTO udata VALUES
                    (NULL,'%s','%d','%s',%d,%d,%d,%d,%d,%d,%d,%d)""";
    udatadelete = "DELETE FROM udata WHERE data_id= %d ";
    udataupdate = """UPDATE udata SET schooltype='%d',major='%s', graduy='%d',
                      age='%d', intern='%d',toeic='%d',tosp='%d', train='%d',
                      jobseek='%d',cert='%d'
                      WHERE id= '%s'
                  """;

    resultlist = """ SELECT * FROM res """;
    resultinsert = "INSERT INTO res VALUES (NULL, '%s', '%s', CURRENT_DATE())";

