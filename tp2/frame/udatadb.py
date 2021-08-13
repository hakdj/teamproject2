from frame.db import Db
from frame.error import ErrorCode
from frame.sql import Sql
from frame.value import Udata


class UdataDb(Db):

    def insert(self,id,schooltype,major,graduy,age,intern,toeic,tosp,train,jobseek,cert):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.udatainsert % (id,schooltype,major,graduy,age,intern,toeic,tosp,train,jobseek,cert));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn);
    def delete(self,id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.udatadelete % (id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def update(self,id,schooltype,major,graduy,age,intern,toeic,tosp,train,jobseek,cert):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.udataupdate % (schooltype,major,graduy,age,intern,toeic,tosp,train,jobseek,cert,id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def selectone(self,id):
        udata = None;
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.udatalistone % id);
        c = cursor.fetchone();
        udata = Udata(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11]);
        super().close(cursor,conn);
        return udata;
    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.udatalist);
        result = cursor.fetchall();
        for c in result:
            udata = Udata(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11]);
            all.append(udata);
        super().close(cursor,conn);
        return all;

if __name__ == '__main__':
    # UdataDb().insert('hakdj',2,'physics',2019,30,1,800,4,2,2,4);

    result=UdataDb().select();
    for r in result:
        print(r);

    # try:
    #     UdataDb().update('hakdj',4,'physics',2019,30,1,800,6,6,6,8);
    #     print('OK');
    # except:
    #     print(ErrorCode.e0001);

    result=UdataDb().selectone('hakdj');
    print(result);